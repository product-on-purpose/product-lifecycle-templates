# Plan: four section 9 candidates, from sweep to built bundle (2026-11-14)

**Status: revision 2, after an adversarial review.** On 2026-11-14 the maintainer asked to plan four candidates
from section 9 of [`backlog.md`](backlog.md#9-researched-types-with-no-issue-and-no-decision), review the plans
adversarially, resolve the findings, and then complete the development. This file is the plan. It decides nothing
about any type. The review's fourteen findings and their resolutions are in the last section.

Each plan is a **conditional pipeline, not a build plan.** A candidate is built only if its sweep admits it and the
maintainer accepts the placement. For a candidate the evidence declines or parks, "complete the development" means
the decline or park record, and nothing more.

**One stop is unavoidable, and the plan is built around it.** Admitting a type to a family edits that family's
contract: its Members line, its version and its change note
([`standing-standards.md`](contracts/standing-standards.md) lines 5 to 18). The repository's standing rule is that
the maintainer reads every contract edit before it merges
([ADR 0075](decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md), lines 44 to 48). The
maintainer has waived that read before, but only for a named PR, after being told what it amended. The 2026-11-14
instruction came before anyone knew which contracts would change, so it is not taken as that read. The run
therefore goes as far as drafted records and contract diffs, then stops once, at G1, for one batched read.

## The four candidates and six types

| Candidate | Types under test | Catalog | Section 9 row |
|---|---|---|---|
| C1, the diary study plan | diary study plan | 28, `diary-study-field-study-plan`, Tier 2, stage discovery | 9.4, research-docs paragraph |
| C2, the principles pair | design principles; product principles document | neither has a row | 9.2 (design principles), 9.1 (product principles) |
| C3, competitive analysis | competitive analysis | 11, `competitive-analysis`, Tier 2, stage market | 9.3 |
| C4, the canvas pair | Business Model Canvas; Value Proposition Canvas | 4, `business-model-canvas`, Tier 2; the Value Proposition Canvas has no row | 9.4 (BMC), 9.1 (VPC) |

## The pipeline

| Stage | What happens | Who | Output |
|---|---|---|---|
| S0, terms pre-clearance | The main loop reads every lead host's terms page raw before any reader starts. Done 2026-11-14 | main loop | `terms-check.json`, `terms-verdicts.json` |
| S1, sweep | Web readers, an internal reader and a critic per candidate. C1 gets a critic only (see C1) | workflow, Sonnet | JSON returns |
| S1b, second terms round | Hosts the readers wanted but could not read are cleared or barred by the main loop, and one targeted re-read runs only if an outcome depends on them | main loop, one agent at most per candidate | an addendum to `terms-verdicts.json` |
| S2, raw check and digest | The main loop raw-checks every quote from a cleared host, and writes one digest per candidate | main loop | `recheck-out.json`, `digest.md` |
| S3, drafts | For each recommended outcome: the ADR, the contract diff, the catalog row, the spec with lettered choices | main loop | one draft PR per candidate, unmerged |
| **G1, the maintainer's read** | One batched message: every outcome, every contract diff, every scope ruling, and every spec choice proposed | maintainer | rulings |
| S4, records land | ADRs, contract edits, catalog rows, `build-candidate` issues, backlog sections 2 and 9 | main loop | the draft PRs, merged on `VERDICT: merge` |
| S5, build | The `build-bundle` workflow, one bundle at a time, with the landing steps below | workflow | bundle PR |
| S6, report | `gen-bundle-build-report.py --ingest` on this machine, then the report PR | main loop | report PR |

**The terms rule.** The allowlist reaches readers as a prompt, so S0 does not make a slip impossible. What it does is
narrow the slip and catch its effects:

- Every reader receives the allowlist, and is told that a host off it goes to `not_read_under_terms` unread.
- S2 pools quotes only from allowlisted hosts.
- The digest also drops any **paraphrase** traced to a host off the allowlist, because sweep 7 let one reach its
  digest (sweep 7's digest, line 39, in the gitignored `_local/research/2026-10-29_admission-sweep-7/`).
- Every slip is reported, as the device-matrix sweep did.

**One rule for a host with no terms page.** A host has no terms page when the standard paths fail and its home page
links no terms, legal or licence page. Such a host has no clause, so it is not barred. That matches the reading of
SVPG in sweep 7 and the 2026-11-04 opportunity-assessment read. A host whose home page links a terms page that S0
did not read stays unresolved and is not read.

**Strategyzer, Wiley, HBR, Atlassian, Shopify and Crayon are barred** for this run, each by a verified clause
recorded in `terms-verdicts.json`. Two of C4's obvious leads, the Strategyzer pages and the publisher's book pages,
are therefore unreadable.

**What stops, and what does not.**

- **G1 stops**, for every admitting ADR and its contract diff, every scope ruling, and every decline. Declines are
  scope rulings ([`build-bundle.md`](../../.claude/commands/build-bundle.md), lines 113 to 114).
- **Delegation after G1** covers only what G1 has ruled on, plus the spec choices G1 has seen. Each delegated choice
  is recorded in its spec.
- **A library release stops.** Nothing here cuts a tag. A bundle's own `template_version` moves inside a bundle PR,
  as every landing does. G1 is asked to confirm that reading, because `build-bundle.md` line 116 says "Any version
  bump".
- **Two rules disagree on bundle merges.** [`bundle-pipeline.md`](bundle-pipeline.md) line 394 says to stop "for the
  maintainer read at the family boundary (batch review)". The `build-bundle` command says a green bundle PR merges on
  its own authority. G1 is asked which governs these builds. Until it answers, the pipeline rule governs, as the
  stricter one.
- **Skill descriptions.** Both skill descriptions list every type, and they now measure 1,017 and 1,022 characters
  against a 1,024-character cap. Each new bundle needs a trigger. Which trigger drops is the maintainer's call (the
  cap and that rule come from session memory, not from a repository file). G1 is asked.

**Landing steps for every build**, beyond the `build-bundle` Definition of Done:

- the README marker and family table, and `STATE.md`'s counts and family membership;
- the contract's Members line;
- the `future:` sweep of every bundle that named the new type as future work ([`bundle-pipeline.md`](bundle-pipeline.md), lines 421 to 425);
- the site honesty gate (lines 399 to 410);
- the Progress table in [`tier2-specs.md`](tier2-specs.md) (line 21), since all six types are Tier 2;
- the `build-candidate` issue relabelled `status:built`, and backlog sections 2 and 9.

**New catalog rows** follow the precedent of rows 206 to 212: the row lands at build time or by a ruling, with an
entry in `catalog.md`'s dated header list ([`catalog.md`](catalog.md), lines 6 and 62 to 67).
[Decision procedure 1](decision-procedures.md) governs correcting an existing row, which applies to row 28.

## C1, the diary study plan

**The question.** Is the diary study plan distinct from the shipped `user-research-plan`, and can `research-docs`
take it without amendment?

**What is already known, and it is most of the answer.**

- A placement pass on 2026-10-23 read NN/g's diary-studies page and User Interviews' diary-study chapter fresh. It
  ruled catalog 28 "a method-specific sibling, not an alias", at medium-high confidence. Its quotes were raw-checked:
  53 passed and 2 failed, and neither failure is load-bearing (`_local/research/2026-10-23_research-plan-placement/`,
  gitignored: `placement-digest.md` lines 6 and 53 to 61, `p3-study-candidates.json`).
- The shipped bundle states the same position: "A diary study plan is a method-specific sibling this plan's
  structure could extend" (`user-research-plan_companion.md`, line 617).
- Both hosts, nngroup.com and userinterviews.com, are cleared in S0.
- **The usability test plan is an alias of `user-research-plan`, and the diary study plan is not, for a stated
  reason.** NN/g gives the diary plan its own structure: entry timing, diary format, logging technique and a
  pre-study brief. A usability test plan is a research plan whose method is a usability test, which the contract's
  own membership text absorbs.
- The shipped templates mention a diary study once, as NN/g's example of a plan that covers several studies. That is
  not diary-planning guidance.

**The contract obstacle is the worked example, not membership.** The family binds every member's example to the
2026-05 Reporting friction study, which "interviewed 12 analysts" (`research-docs.md`, lines 147 to 156). A member
whose example "invents a different study, is out of contract". A diary study plan cannot plan an interview study.

**The cheaper path.** C1 gets no four-agent sweep. The main loop re-raw-checks P3's load-bearing quotes, and one
Sonnet critic applies the five checks to that evidence and the internal facts above.

**Named outcomes.**

| Outcome | What "complete" means |
|---|---|
| A. Distinct, joins `research-docs` with a section 4 amendment allowing a second study thread | G1 reads the amendment; row 28 narrowed to the diary study plan by procedure 1, with field study and contextual inquiry split to a new row or recorded as dropped; ADR, issue, spec, build |
| A2. Distinct, joins with an example tied to the same study | Only if the critic finds a diary component the Reporting friction study could credibly have had. Same steps as A, no example amendment |
| B. A method section of `user-research-plan` | Decision procedure 12's element test (E1 to E4) first; a bundle minor version; ADR declining the separate type; row 28's fate recorded |
| C. Evidence-insufficient | Parked, with the read that would settle it |

**Prior, medium-high confidence: outcome A.** The evidence for distinctness is already raw-checked. The open
question is the amendment.

## C2, the principles pair

**The questions.** Is a product principles document already covered by `product-strategy`? Is a design principles
document a distinct type, and where does it sit? Are the two one type?

**What is already known.**

- `product-strategy` ships three formats. Its default is the **kernel**, and neither kernel variant has a principles
  section. Only the one-pager's full variant has `## Product Principles`
  (`product-strategy_template-one-pager-full.md`, line 157).
- [ADR 0087](decisions/0087-product-discovery-plan-is-declined.md) maps Cagan's "Product Principles" component to
  `product-strategy` (line 83).
- **A correction is owed regardless of this sweep.** `product-strategy_history.md` lines 35 to 36 say the spec's
  sections, Principles included, "survive in the full variant". In the default kernel format they do not.
- The product principles document's only section 9 source is an AI prompt from Productboard, which is weak for check 1.
  The maintainer's copy of Cagan's *Inspired* is in `_local/research/2026-11-05_cagan-books/`, gitignored; the main
  loop reads it for the product principles question.

**Whether the kernel's gap matters is a library question, not a web question.** Decision procedure 12's element test
decides whether a section belongs in a shipped template ([`decision-procedures.md`](decision-procedures.md), lines
207 to 250). The sweep supplies evidence; the test is applied in S3.

**The family tests for design principles.**

- `standing-standards` says members are "written when the team decides how it will work" (lines 28 to 29). Design
  principles describe the product's experience, not how the team works. The critic tests whether that strains the
  clause.
- If sources show periodic revision, [ADR 0088](decisions/0088-platform-device-support-matrix-joins-standing-standards-as-a-foundation.md)
  says to weigh an amendment "instead of a fourth exception" (lines 164 to 166). That is a G1 stop.
- `strategy-docs` has a closed list of questions, and each new member widens it by amendment.

**Named outcomes.**

| Outcome | Product principles | Design principles |
|---|---|---|
| A | Covered by `product-strategy`; the kernel gains a section only if procedure 12 passes it | Its own type: `standing-standards` (amendment likely) or `strategy-docs` (widening) |
| B | One type, "principles", with both names | Same row; family chosen by the stronger half's evidence |
| C | Covered, as A | Evidence-insufficient, parked |
| D | Its own type | Its own type; two rows, two family decisions |

**Prior, medium confidence: outcome A.** The product principles half rests on shipped text. The design principles half
rests on evidence not yet read, and its family is open.

## C3, competitive analysis

**The question.** Is the competitive analysis admitted, and where does it fit?

**What is already known.**

- Catalog 11, stage market. The catalog's "Market / Competitive" group holds about eight unbuilt rows, so this type
  may be the first of a group, not a lone member.
- `positioning-statement`'s guide names "the competitive analysis such language would be built on" as upstream work
  separate from the positioning document (`positioning-statement_guide.md`, line 90). That argues the two are not
  duplicates. The example's line 20, which the review proposed instead, uses "competitive map" for the positioning
  map, so it says nothing about this type.

**The family question, corrected.**

| Family | Fits as written? | Why |
|---|---|---|
| `discovery-docs` | Only for a point-in-time study written once for a decision | Its members are "written once for a decision, and finished when that decision is made" (`discovery-docs.md`, lines 80 to 81) |
| `strategy-docs` | No: needs a widening | Its question list is closed, and each new member widened it by amendment ([ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md), lines 22 to 25) |
| `governance-docs` | No: needs a purpose amendment | It admits a "register, log, or dashboard" that tracks risk, open items or performance (`governance-docs.md`, line 12); ADR 0088 found an amendment needed for a non-tracking instrument |
| A new market family | Contract first | The "Market / Competitive" group may justify one; the contract is drafted, then read |

**Named outcomes.**

| Outcome | What "complete" means |
|---|---|
| A. Admitted to `discovery-docs` as written, as a point-in-time study | ADR, contract Members line (a G1 read), issue, spec, build |
| B. Admitted, family needs an amendment or widening | G1 reads the amendment, then as A |
| C. Admitted, a new family | Contract drafted, read at G1, then as A; the build waits for the read |
| D. Duplicate | ADR declining it, at G1 |
| E. Evidence-insufficient | Parked |

**Prior, medium confidence: outcome B.** Sources are likely to treat a competitive analysis as a living document,
which no family admits as written.

## C4, the canvas pair

**The questions.** Is the Business Model Canvas admissible, and where? Is the Value Proposition Canvas its own type, a
section of the BMC, or neither?

**What is already known.**

- [ADR 0083](decisions/0083-lean-canvas-joins-strategy-docs-as-a-seventh-member.md) admitted the Lean Canvas and says
  "The Business Model Canvas stays a separate candidate", bounded by the four boxes Maurya replaced. The shipped
  `lean-canvas` summary and guide route to catalog entry 4 as a different document.
- [ADR 0028](decisions/0028-adopt-a-format-axis.md) defines a format as another shape of the **same** document type.
  [ADR 0005](decisions/0005-bundle-ids-doctype-spine.md) keeps catalog types and bundles one to one. So **the BMC cannot be a format of `lean-canvas`**, and the VPC
  cannot be a format of the BMC.
- `strategy-docs` already answers "which business model could get us there" with the Lean Canvas. The BMC there needs
  a widening that names the situation each canvas serves.
- `discovery-docs` allows exactly one revise-while-testing member, `lean-ux-canvas`: "no other member takes this
  exception" (line 96). The VPC there needs an amendment.
- `methodology.md` names Osterwalder as a Tier 1 originator ("Osterwalder for BMC", line 85).

**Evidence constraints.** Strategyzer and Wiley are barred, and both are the canvases' own publishers. A licence
statement is readable on a cleared page, for example Wikimedia Commons' file page for the canvas image, which states
the image's licence. The VPC's licence may differ from the BMC's. A template that reproduces a canvas's box names
depends on its licence, so the licence is load-bearing for the build, not only for admission.

**Named outcomes.**

| Outcome | What "complete" means |
|---|---|
| A. BMC admitted to `strategy-docs` with a widening; VPC a section of the BMC bundle | G1 reads the widening; one build |
| B. BMC admitted as A; VPC its own type (amendment in `discovery-docs`, or a widening) | Two G1 reads; two builds |
| C. BMC admitted as A; VPC declined | One build, one decline at G1 |
| D. Licence or evidence fails for either | Decline or park, at G1, with the reason and the pages the maintainer could read by hand |

**Prior, low confidence.** The barred publishers make evidence thinner than the canvases' fame suggests. A short
hand-read list for the maintainer is a likely output.

## Workflow mechanics

- **One sweep workflow, `sweep8.js`**, adapted from sweep 7's script: the same schemas, admission checks, relay scope
  note and raw-check instruction, with the S0 allowlist in place of the terms list.
- **Thirteen agents, all Sonnet:** four each for C2, C3 and C4, and one critic for C1. This session's workflow-size
  guideline is ten. The candidates are independent, and one run is what makes G1 a single stop. Sweep 7 ran 20.
- **Builds run one at a time**, because the `build-bundle` command requires a clean main and no open PRs (line 48).
  Each costs $12 to $41 at list rates (line 129). Up to six types could reach a build, but only after G1.

## What this plan does not know

- Whether the Reporting friction study could credibly have had a diary component (C1, outcome A2).
- Whether design principles have a template-style source, or only published principle sets.
- The BMC's and the VPC's licences.
- Whether any competitive-analysis source treats it as a point-in-time study.
- How many of the six types survive G1, which sets the run's length and cost.

## Review record (2026-11-14)

The plan's first revision was reviewed adversarially by an Opus agent standing in for a Codex review, because the
Codex CLI is not installed on this machine. The main loop spot-checked findings 1, 2, 3, 5, 8 and 10 against the
files before applying them; each held.

| # | Severity | Finding | Resolution |
|---|---|---|---|
| 1 | high | C1 ignored raw-checked evidence already in the repo | C1 rebuilt on the P3 evidence and the four-agent sweep dropped. **The prior it proposed, A, was then overturned by the sweep**: NN/g's list puts the diary items "in your study plan", and no publisher read ships a separate diary plan, so the recommendation is B |
| 2 | high | C1-A needs a research-docs example amendment | Outcome A now carries the amendment; A2 added |
| 3 | high | Admitting ADRs all edit contracts, so "ADRs on delegation" covered almost nothing | Every admitting ADR goes to G1 with its diff |
| 4 | high | C4's format options broke ADRs 0028, 0005 and 0083 | Format outcomes removed; VPC becomes a section, its own type, or declined |
| 5 | high | C3's family analysis was wrong and incomplete | Table rebuilt from each contract; new-family and park outcomes added; prior moved to B |
| 6 | medium | Terms enforcement overstated; inconsistent no-terms rule; barred lead | Claim narrowed; paraphrase filter and S1b added; one no-terms rule; Wiley named as barred |
| 7 | medium | C2 skipped two standing-standards tests; outcome B had no family | Both tests added; every outcome names a family |
| 8 | medium | C2 asked the web an internal question; missing kernel outcome; history defect | Procedure 12 named; kernel outcome added; correction recorded as owed |
| 9 | medium | Bundle-edit outcomes skipped procedure 12 and the version-bump question | Procedure 12 added to C1-B and C2-A; G1 asked about bundle versions |
| 10 | medium | Landing steps missing; two merge rules conflict | Landing list added; conflict put to G1, stricter rule meanwhile |
| 11 | medium | Procedure 1 miscited for new rows; row 28 fate missing | Rows 206 to 212 named as the precedent; row 28 handled in every C1 outcome |
| 12 | low | "Plans diary studies today" overstated | Corrected in C1 |
| 13 | low | Wrong citation for the positioning hand-off | **Rejected on verification** (decision procedure 4): the sweep 8 critic read the proposed line 20 and found it is about the positioning map; the guide's line 90 stands |
| 14 | low | "10-agent guideline" has no repository source | Named as this session's guideline |

## G1 rulings (2026-11-14)

The maintainer answered the batched read in two messages on 2026-11-14 and 2026-11-15:

| Item | Ruling | Record |
|---|---|---|
| D1, diary study plan | Declined as a separate type; `user-research-plan` gains a conditional diary block | [ADR 0092](decisions/0092-diary-study-plan-is-declined-as-a-separate-type.md) |
| D2, product principles | A type of its own | [ADR 0090](decisions/0090-product-principles-joins-standing-standards-as-a-foundation.md), #360 |
| D3, design principles | `standing-standards`, `foundation`, with section 1 widened | [ADR 0089](decisions/0089-design-principles-joins-standing-standards-as-a-foundation.md), #359 |
| D4, product principles' family | `standing-standards`, beside design principles | ADR 0090 |
| D5, competitive analysis | `strategy-docs`, `utility`, by an eighth question | [ADR 0091](decisions/0091-competitive-analysis-joins-strategy-docs-as-an-eighth-member.md), #361 |
| D6, both canvases | A fresh read with Strategyzer open, then a decision on that evidence | Not yet run |
| D7, terms | The terms rule is lifted for public pages and the maintainer's own books | [`bundle-pipeline.md`](bundle-pipeline.md), "The terms rule" |
| D7, other items | Codex review: the maintainer will sign in to Codex later. Merging: unanswered, so the stricter batch review holds | None yet |

**One change from the G1 draft.** The draft put competitive analysis after the positioning statement in the
`strategy-docs` chain. The landed text puts it before, because `positioning-statement`'s guide names the analysis as
upstream work. This is flagged for the maintainer's read of the contract diff.
