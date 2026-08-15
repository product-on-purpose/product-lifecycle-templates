# Plan inventory: what is planned, what is specified, and what is neither

> **This is a dated inventory taken on 2026-08-14, not a plan.** It does not decide anything and it does
> not sequence anything. It answers three questions that took a working session to answer from scratch:
> what does the release plan say, what does the roadmap promise in terms a user would recognise, and which
> specs could be executed tomorrow. [`STATE.md`](../../STATE.md) outranks this file wherever they disagree.
>
> It exists because that session found the answers scattered across seven documents, two of them
> untracked, and three of them stale in ways that changed the answer.

<!-- counts: bundles=26, adrs=38, cisteps=25 -->

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
currently off it by an explicit decision that has now expired. Of six executable build specs, one is
fully executed, one is half executed, and four are complete and idle.

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
one installable skill, `plt-fill-template`. The Claude Code plugin channel clones the tree and works. The
skills-CLI channel installs 12 KB of instructions and none of the 26 bundles, and fetches templates at
fill time from the release tag matching its own declared version.

## 4. Spec inventory

| Spec | The feature | State | What blocks it |
|---|---|---|---|
| `spec_machine-metadata.md` (untracked) | Metadata schema, manifest, the gate alphabet | **Executed.** ADRs 0016 through 0019 | nothing, done |
| **`spec_lp2-grade-my-doc.md`** (untracked) | **The wedge: grade an existing document, return a report card** | **Complete, ready, not started.** `skills/` holds only `plt-fill-template` | Nothing. It is the highest-value idle asset in the repository |
| `spec_ev1-efficacy-evals.md` (untracked) | Efficacy evaluation | **Half executed.** [`evals/`](../../evals/) holds the harness, rubrics and two completed runs | The Workflow tool grant, plus three protocol decisions in [`eval-protocol.md`](eval-protocol.md) |
| `spec_lp1-use-template-flow.md` (untracked) | Interview-driven fill, the guidance-comment grammar, `strip-template.py` | **Complete, not started.** Partly pre-empted by `plt-fill-template` | M5, gated on M3 |
| `spec_ag2-mcp-server.md` (untracked) | MCP server: five tools, three resources, token budgets | **Complete, not started** | M5, gated on M3 by design |
| [`guide-rubric-spec.md`](guide-rubric-spec.md) | Guide rubric house style, and the backfill across every guide | **Says "spec, ready to execute" in its own header**, adopted 2026-07-27 | Nothing. It was scoped as an opportunistic backfill and has not been swept |
| [`pull-queue-spec.md`](pull-queue-spec.md) | Demand capture, WP-32 | **Written 2026-08-14, one decision open** | The demand rule, which stops for the maintainer |

**Four of the six build specs are untracked.** They live in the gitignored audit package, are cited by name
in the roadmap because they cannot be linked, and are covered by no check in this repository. They cannot
go stale loudly, only quietly. That is ADR 0013's recorded cost appearing as an operational one, and it is
the strongest argument for promoting the two that are closest to execution.

## 5. What needs a spec and has none

Ordered by what unblocks the most other work.

| # | Needs a spec | Why it matters | Current state |
|---|---|---|---|
| 1 | **The ADR 0038 follow-through**, if accepted | Writing the element admission test into [`decision-procedures.md`](decision-procedures.md) as a numbered procedure, and adding the gap question to [`bundle-pipeline.md`](bundle-pipeline.md) as a standing research dimension. The second half is what makes it systematic rather than a one-off | Named inside [ADR 0038](decisions/0038-what-the-circularity-signature-obliges.md). No spec |
| 2 | **The eval protocol amendments** | Three separate changes: a validity gate for the held-out gap, a redesign of held-out selection, and independence between the probe set and the held-out set | Named in `eval-protocol.md` section 4. Each stops for the maintainer. No spec |
| 3 | **The references and selection layer** (WP-70 through WP-75) | A method-selection guide, a relationship map, a glossary, an anti-pattern catalog. The 2026-07-17 phases plan calls this the only content-shaped work permitted while the wedge is stalled, because it is selection infrastructure rather than coverage | Proposed in `_local/planning/claude_2026-07-17_next-phases-plan.md`, never ratified. Verified unbuilt: no references directory exists, and `state` and `resource_type` appear zero times in `tools/meta.schema.json`. Needs its ontology ADR first |
| 4 | **The flagship content review findings** (CR-1 through CR-7) plus the 2026-08-05 agentic-era recommendations A1 and A2 | The only substantive critique of the library's advice quality as opposed to its governance. CR-1 (the missing AI-era debate in the PRD bundle) and A1 (a PRD AI-era section) are the same work, reached independently three weeks apart | Unapplied. Verified: `AI` appears zero times in `templates/prd/prd_companion.md`, and no `Alternatives Considered` section exists anywhere in that bundle. Both sources are untracked. Gated behind ADR 0038 |
| 5 | **The family-wide rubric-threshold rewording** | Two independent reviewers flagged the guides' predictive threshold sentences as unsourced claims. `STATE.md` records that the family-wide edit "should be scheduled rather than re-litigated per bundle" | Recorded as open by choice. It has since been re-litigated per bundle twice. No spec |
| 6 | **The sidecar-asset scope decision** | Whether a bundle may ship a non-Markdown sidecar. A prerequisite for any dataset or evaluation bundle. [ADR 0030](decisions/0030-templating-scope-markdown-documents.md) settles what the library templates, not what a bundle may carry. Verified: `sidecar` appears zero times under `docs/` | Proposed in the 2026-08-05 research. Genuinely open |
| 7 | **The site track** | The presentation layer for 26 bundles that no one can currently browse | Two plans in `_local/planning/`, unratified, hard-gated on decision VL-1 (business model) |

## 6. Open decisions, and what they hold up

Taken from `STATE.md`, which remains authoritative for this table.

| ID | Decision | Open since | Holds up |
|---|---|---|---|
| ADR 0038 | What the circularity signature obliges | 2026-08-08 | Every element-level template change, which is items 1 and 4 above |
| D1 | Build the Layer 1 generator, or not | 2026-06-29 | Nothing. Correctly gated on a usage signal |
| D4 | Regulated-industry tier appetite | 2026-06-29 | Tier-3 regulated, permanently, until answered |
| VL-1 | Business model | 2026-07-02 | The site track, item 7 |
| VL-3 | Maintenance cadence | 2026-07-02 | M6. Scheduled there |

The **decision SLA** recorded in `STATE.md` says any open decision whose resolution cost is under two
hours is resolved within three working days or explicitly re-dated with a reason. Three of the five above
carry no stated cost and no re-dating, which is the same shape as the D2 and D3 breach that `STATE.md`
records at a factor of six.

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
