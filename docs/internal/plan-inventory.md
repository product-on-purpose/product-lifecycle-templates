# Plan inventory: what is planned, what is specified, and what is neither

> **This is a dated inventory taken on 2026-08-14, not a plan.** It does not decide anything and it does
> not sequence anything. It answers three questions that took a working session to answer from scratch:
> what does the release plan say, what does the roadmap promise in terms a user would recognise, and which
> specs could be executed tomorrow. [`STATE.md`](../../STATE.md) outranks this file wherever they disagree.
>
> It exists because that session found the answers scattered across seven documents, two of them
> untracked, and three of them stale in ways that changed the answer.
>
> **Amended 2026-08-19, four corrections and no re-dating.** The `pull-queue-spec.md` row in section 4
> still called the demand rule an open decision after
> [ADR 0039 (maintainer discretion replaces the pull gate)](decisions/0039-maintainer-discretion-replaces-the-pull-gate.md)
> had settled it; [`distribution-plan.md`](distribution-plan.md) was missing from section 4 altogether,
> which is this document's own job; and the spec counts in section 1 and under the section 4 table both
> read "six" and "four" against a table that has carried seven rows and five untracked entries since the
> day it was written. **Every other fact below still dates from 2026-08-14 and has not been re-verified.**
>
> **Amended again 2026-08-19, when WP-30 shipped.** The `spec_lp2-grade-my-doc.md` row said the wedge was
> not started and that `skills/` held only `plt-fill-template`. Both were true when written and are now
> false; section 3's skill count and section 1's tally move with them.

<!-- counts: bundles=26, adrs=40, cisteps=25 -->

**A note on the untracked references below.** Several specs and plans named here live at
`_local/audit/2026-07-10_fable-audit/` and `_local/planning/` on the maintainer's machine, and are
deliberately not in this repository ([ADR 0013, the `_local/` split](decisions/0013-local-split-and-going-public.md)).
They appear as plain paths rather than links, because `tools/check-links.py` fails the build on a tracked
file that links into `_local/`: such a link resolves for exactly one person and returns 404 for everyone
else. The honest cost is that an outside reader cannot follow those references to their source. This is
the same convention [`roadmap.md`](roadmap.md) uses, for the same reason.

---

## 1. The short version

**There is a roadmap. There is no release plan.** The roadmap is specified through M6 and the library is
currently off it by an explicit decision that has now expired. Of the eight documents inventoried in
section 4, two are fully executed, one is half executed, and five are complete and idle.

**The pattern underneath all three answers:** everything built so far delivers value to someone who has
already adopted the library. Every item that would deliver value to someone who has not is unbuilt.

## 2. The release plan does not exist as a forward document

| Surface | What it holds | Direction |
|---|---|---|
| [`docs/releases/`](../releases/) | Five notes, `v0.1.0` through `v0.3.1`, each written by filling this library's own `release-notes` template | Backward |
| [`RELEASE-NOTES.md`](../../RELEASE-NOTES.md) | The curated read of what shipped and why it mattered | Backward |
| [`CHANGELOG.md`](../../CHANGELOG.md) `[Unreleased]` | What has accumulated since the last tag | Backward |
| [`release-process.md`](release-process.md) | Six steps, versioning rules, and what the process does not do | Mechanics |

**No document names the next version or states what earns it.** A search across the release documents,
`STATE.md` and the roadmap for `v0.4`, `0.4.0` and "next release" returns exactly one hit: a roadmap line
stating that `v0.2.0` is the exit act and the next release, which is three releases out of date.

**The consequence is visible in the release history rather than hypothetical.** Both patch releases so far,
`v0.2.1` and `v0.3.1`, were cut as corrections to a defect found after tagging, not shipped as planned
increments. The cadence is currently reactive, and `release-process.md` documents how to cut a release
without anything documenting when or why.

## 3. The roadmap, in features and customer value

[`roadmap.md`](roadmap.md), milestones M0 through M6. Its sequencing thesis is **floor, then wedge, then
proof, then reach**, and its own argument is that every deep investment is discounted until the wedge
produces a usage signal, because coverage multiplies zero.

| Milestone | The feature, in a user's terms | Who it is for | Real status, 2026-08-14 |
|---|---|---|---|
| M0 Credibility floor | A fresh clone survives inspection | Anyone evaluating | Done |
| M1 Integrity | `v0.1.0`, every citation verified | Adopters | Done 2026-07-17 |
| M2 Machine layer and Tier-1 floor | A deterministic selection surface, 26 bundles, nine family contracts | Adopters and their agents | **Done in substance.** The roadmap's own status column still reads "18 of 27 types are built" and names `v0.2.0` as the next release |
| **M3 Wedge** | **Point a skill at a PRD you already wrote and get a report card against a researched rubric.** Plus the first real fill, the pull queue, and outreach | **Someone who has never used this library** | **Not started.** Zero fills. Three of four acceptance criteria unmet |
| M4 Proof | Per-bundle eval scorecards; conformance levels L1, L2, L3; CI regression on the eval gap | Anyone deciding whether to trust the quality claim | **Partly started.** Protocol written, harness built, two runs completed, both **VOID** on discrimination, three bundles of 26 measured |
| M5 Reach | Interview-driven fill flow, an MCP server, full distribution | Agents and their operators | Not started, correctly gated on M3 |
| M6 Scale by pull | The next family on demand, quarterly freshness, a contribution pipeline | Contributors | Not started |

### The one thing this table is for

**The library is off its own roadmap by a decision that has expired.**
[ADR 0021 (complete the Tier-1 floor)](decisions/0021-complete-the-tier-1-floor.md) deliberately overrode
the floor-then-wedge ordering for the Tier-1 set only, on the argument that a six-bundle library is too
thin to earn a pull. That was a knowing trade and it is now cashed: the floor is complete and the build
backlog is empty. **The override covered the Tier-1 floor and nothing else, so the roadmap's original
ordering resumes at M3 on the roadmap's own terms**, not as a matter of preference.

### What a user can actually get today

Twenty-six researched bundles, a machine-readable `manifest.json`, four user-facing how-to documents, and
**two installable skills**, `plt-fill-template` and, since 2026-08-19,
`plt-grade-doc`. The Claude Code plugin channel clones the tree and works. The skills-CLI channel installs
instructions and none of the 26 bundles, and each skill fetches what it needs at run time from the release
tag matching its own declared version.

## 4. Spec inventory

| Spec | The feature | State | What blocks it |
|---|---|---|---|
| `spec_machine-metadata.md` (untracked) | Metadata schema, manifest, the gate alphabet | **Executed.** ADRs 0016 through 0019 | nothing, done |
| **`spec_lp2-grade-my-doc.md`** (untracked) | **The wedge: grade an existing document, return a report card** | **Executed 2026-08-19** as [`skills/plt-grade-doc/`](../../skills/plt-grade-doc/), with two deviations stated in the skill: the `plt-` prefix, and a grader-supplied 0/1/2 scale for the checklist-rubric guides, eleven of them since `acceptance-criteria` converted on 2026-08-21 | **Built, not validated.** Most of the spec's acceptance criteria need documents this repository does not have, and no external document has been graded |
| `spec_ev1-efficacy-evals.md` (untracked) | Efficacy evaluation | **Half executed.** [`evals/`](../../evals/) holds the harness, rubrics and two completed runs | The Workflow tool grant, plus three protocol decisions in [`eval-protocol.md`](eval-protocol.md) |
| `spec_lp1-use-template-flow.md` (untracked) | Interview-driven fill, the guidance-comment grammar, `strip-template.py` | **Complete, not started.** Partly pre-empted by `plt-fill-template` | M5, gated on M3 |
| `spec_ag2-mcp-server.md` (untracked) | MCP server: five tools, three resources, token budgets | **Complete, not started** | M5, gated on M3 by design |
| [`guide-rubric-spec.md`](guide-rubric-spec.md) | Guide rubric house style, and the backfill across every guide | **Says "spec, ready to execute" in its own header**, adopted 2026-07-27 | Nothing. It was scoped as an opportunistic backfill and has not been swept |
| [`pull-queue-spec.md`](pull-queue-spec.md) | Demand capture, WP-32 | **Written 2026-08-14. The one decision it stopped for was taken the same day.** [ADR 0039 (maintainer discretion replaces the pull gate)](decisions/0039-maintainer-discretion-replaces-the-pull-gate.md) made the queue a priority signal rather than a precondition | **No decision.** Section 4 was rewritten from a permission gate into a prioritisation rule on 2026-08-21, closing that WP-32 build task. **The rest of the spec is sequenced behind deliverable D5, the demand-rule ADR, which stops for the maintainer** |
| [`distribution-plan.md`](distribution-plan.md) | Wedge outreach, WP-33: a venue-by-venue submission plan | **Written 2026-08-14. Complete, and nothing has been submitted.** Built from research that fetched and read every venue rather than recalling it | **No decision and no build.** Every act in it opens an issue or a pull request on a third party's repository, so its own section 8 stops all of them for the maintainer |

**Five of the eight documents in this table are untracked, and all five of those are build specs.** They
live in the gitignored audit package, are cited by name in the roadmap because they cannot be linked, and
are covered by no check in this repository. (This sentence read "four of the six" until 2026-08-19. It was
wrong on the day it was written: the table has carried seven rows and five untracked entries from the
start, and nothing checks a count written in prose.) They cannot
go stale loudly, only quietly. That is ADR 0013's recorded cost appearing as an operational one, and it is
the strongest argument for promoting the two that are closest to execution.

## 5. What needs a spec and has none

Ordered by what unblocks the most other work.

| # | Needs a spec | Why it matters | Current state |
|---|---|---|---|
| ~~1~~ | ~~The ADR 0038 follow-through~~ | ~~Writing the element admission test into `decision-procedures.md`, and adding the gap question to `bundle-pipeline.md`~~ | **Done 2026-08-14.** [Procedure 12](decision-procedures.md) and [research dimension 6](bundle-pipeline.md). Never needed a spec; the ADR was the spec |
| 2 | **The eval protocol amendments** | Three separate changes: a validity gate for the held-out gap, a redesign of held-out selection, and independence between the probe set and the held-out set | Named in `eval-protocol.md` section 4. Each stops for the maintainer. No spec |
| 3 | **The references and selection layer** (WP-70 through WP-75) | A method-selection guide, a relationship map, a glossary, an anti-pattern catalog. The 2026-07-17 phases plan calls this the only content-shaped work permitted while the wedge is stalled, because it is selection infrastructure rather than coverage | Proposed in `_local/planning/claude_2026-07-17_next-phases-plan.md`, never ratified. Verified unbuilt: no references directory exists, and `state` and `resource_type` appear zero times in `tools/meta.schema.json`. Needs its ontology ADR first |
| 4 | **The flagship content review findings** (CR-1 through CR-7) plus the 2026-08-05 agentic-era recommendations A1 and A2 | The only substantive critique of the library's advice quality as opposed to its governance. CR-1 (the missing AI-era debate in the PRD bundle) and A1 (a PRD AI-era section) are the same work, reached independently three weeks apart | Unapplied. Verified: `AI` appears zero times in `templates/prd/prd_companion.md`, and no `Alternatives Considered` section exists anywhere in that bundle. Both sources are untracked. Gated behind ADR 0038 |
| 5 | **The family-wide rubric-threshold rewording** | Two independent reviewers flagged the guides' predictive threshold sentences as unsourced claims. `STATE.md` records that the family-wide edit "should be scheduled rather than re-litigated per bundle" | Recorded as open by choice. It has since been re-litigated per bundle twice. No spec |
| 6 | **The sidecar-asset scope decision** | Whether a bundle may ship a non-Markdown sidecar. A prerequisite for any dataset or evaluation bundle. [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) settles what the library templates, not what a bundle may carry. Verified: `sidecar` appears zero times under `docs/` | Proposed in the 2026-08-05 research. Genuinely open |
| 7 | **The site track** | The presentation layer for 26 bundles that no one can currently browse | Two plans in `_local/planning/`, unratified, hard-gated on decision VL-1 (business model) |

## 6. Open decisions, and what they hold up

Taken from `STATE.md`, which remains authoritative for this table.

**Three of these five closed on 2026-08-14**, the day after this file was written, which is worth noting
because it is what a worked decision backlog looks like rather than a failure of the inventory.

| ID | Decision | Open since | State |
|---|---|---|---|
| ADR 0038 | What the circularity signature obliges | 2026-08-08 | **Closed 2026-08-14: accepted**, with option C rejected consciously. Both follow-through items done: procedure 12, and research dimension 6 |
| D4 | Regulated-industry tier appetite | 2026-06-29 | **Closed 2026-08-14: no, for now**, on the regulation-currency burden. Reopens on a pull from a real regulated team |
| VL-1 | Business model | 2026-07-02 | **Closed 2026-08-14 ([ADR 0040](decisions/0040-free-and-open-source-no-paid-tier.md)): free and open source, no paid tier.** Unblocks the site track, item 7 above |
| D1 | Build the Layer 1 generator, or not | 2026-06-29 | **Open, and correctly so.** Waiting on a usage signal. The one open decision the audit did not fault |
| VL-3 | Maintenance cadence | 2026-07-02 | **Open.** Scheduled at M6, which is fine for the quarterly source pass. The monthly decision-triage half is arguably worth starting sooner |

**A separate decision, [ADR 0039](decisions/0039-maintainer-discretion-replaces-the-pull-gate.md), was
taken the same day and was not on this list**, because it was not an open decision: it is an amendment the
maintainer initiated. It removes the demand gate on Tier-2 and Tier-3 builds, which **changes item 3 in
section 5 above**: the references layer no longer needs a pull to be legitimate, only a rationale.

The **decision SLA** recorded in `STATE.md` says any open decision whose resolution cost is under two
hours is resolved within three working days or explicitly re-dated with a reason. **The three that closed
had been open 6, 46 and 43 days.** None of them triggered the SLA, and the reason is mechanical rather than
negligent: **the SLA keys on a stated resolution cost, and all three carried `n/a` in that column**, so no
clock ever started. That is the same shape as the D2 and D3 breach `STATE.md` records at a factor of six,
and it is a defect in the rule rather than in the following of it.

## 7. What this document does not do

It does not sequence, prioritise, or decide. It does not amend the roadmap, and where it disagrees with
`STATE.md`, `STATE.md` wins. It takes no position on ADR 0038, on the demand rule in
[`pull-queue-spec.md`](pull-queue-spec.md), or on whether the 2026-08-05 research package should be
promoted at all.

Its one editorial claim is the sentence in section 3: that the ADR 0021 override has expired on its own
terms because its stated scope, the Tier-1 floor, is complete. That is an argument, and it is marked as
one.

## 8. How this document will go stale

**Every fact here was read from the tree on 2026-08-14, and most of them have no gate behind them.** That
is finding DF-3 (gated documents stay fresh, ungated ones drift) and this file is squarely in the ungated
category, exactly as `roadmap.md` is.

Two mitigations, both partial:

- The counts marker at the top is compared against the tree by
  [`check-counts.py`](../../tools/check-counts.py), so a changed bundle or decision-record count fails CI
  rather than ageing quietly here. **That gate reads markers and never the prose around them, and it says
  so on every run.** The prose in sections 3 through 6 is not gated by anything.
- Every "verified" claim in sections 4 and 5 names the command or the file that produced it, so a reader
  can re-run the check rather than trusting the sentence.

**The specific claims most likely to be wrong first**, in order: the spec inventory in section 4, because
executing any one of them changes a row; section 5 item 3, because ratifying the phases plan would move it
wholesale; and the release-plan gap in section 2, which closes the moment anyone writes down what `v0.4.0`
is for.
