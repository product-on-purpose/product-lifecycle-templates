# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) 1.1.0, and this
project adheres to [Semantic Versioning](https://semver.org/).

The customer-facing announcement for each release lives in [`docs/releases/`](docs/releases/) and is
written using this library's own `release-notes` template. This file is the record; that is the
announcement. The distinction is the one the `release-notes` bundle teaches: a changelog is for
people who want every change, release notes are for people who want to know what it means for them.

## [Unreleased]

### Added

- **[`docs/internal/distribution-plan.md`](docs/internal/distribution-plan.md)**, the executable plan for
  roadmap **WP-33** (wedge outreach), built from research that fetched and read every venue rather than
  recalling it. **Its central finding contradicts the brief it was written against.** The largest and
  best-fitting venue, `hesreallyhim/awesome-claude-code` (52,325 stars), states in its own `CONTRIBUTING.md`
  that the submit-then-get-users sequencing is backwards: *"If 'getting on the list' is any part of a
  promotional strategy for your project, you should be prepared to have a backup plan."* The plan is
  sequenced to respect that rather than ignore it.

  **The two ecosystems are not alike.** Product management has almost no live surface: four
  "awesome-product-management" lists were last pushed between 2019 and 2023, the one live general PM list
  forbids self-promotion, no maintained `awesome-adr` exists, and no PM community or newsletter was found
  with a public non-gated submission path. The Claude and agent-skills ecosystem is young and mostly
  ungated, and where a maturity bar exists it is framed as *age-plus-activity or stars*, never stars alone.
  **That distinction is what makes this library eligible today at one star**: it clears
  `awesome-claude-code`'s written bar (14 days plus continued commits) outright.

  Records what must **not** be submitted and why, including one venue whose stated criteria this library
  fails today by its own honest caveat (`VoltAgent/awesome-agent-skills` requires "real community usage"),
  and one that shows integrity red flags. Also records the tension the README's `real fills: 0 (honest)`
  badge creates: it will cost acceptances, removing it would abandon the thing that makes the library worth
  finding, and the recommendation is to keep it and lose the acceptances **on purpose**.

  **Every act of submission stops for the maintainer.** Each one opens an issue or a pull request on someone
  else's repository under this project's name, and is not cleanly reversible.

- **[`.claude/agents/blind-probe-author.md`](.claude/agents/blind-probe-author.md)**, a scoped subagent that
  satisfies the eval protocol's section 6 blinding rule **by construction rather than by instruction**. It
  is given **no filesystem tools at all**, no `Read`, `Grep`, `Glob` or `Bash`, so it cannot open
  `templates/`, `evals/rubrics/` or `manifest.json` because it has nothing to open them with. An agent told
  not to look can look; an agent with no read tool cannot. Path-level restriction is not something agent
  configuration can express, so tool removal is the enforceable form. **It exists because the rule
  disqualified the only author available:** probe hardening was authorised on 2026-08-10 and deliberately
  not done, since the agent holding the authorisation had spent the session reading the very material the
  rule excludes. **Authorisation is not competence to do the task correctly.** The agent carries its own
  limitation in its instructions and is required to restate it in every output: it is an *approximation* of
  a blind author, sharing a model family with the agents that wrote the templates, and no report may claim
  the stronger "written by someone who has never seen this library".
- **Spend recording in the eval harness.** The first two runs recorded **no cost data whatsoever**, so the
  question "what does a re-run cost?" had no answer for three sessions and the Workflow grant kept being
  requested for an amount nobody could state. `output-eval.workflow.mjs` now emits a `spend` block into its
  raw output, with both of its limits attached in the file: `budget.spent()` is **turn-level** output
  tokens rather than this workflow alone, so it is an upper bound; and it counts **output only**, while for
  this harness input is likely the larger half. An upper bound on half the cost beats the nothing that was
  there. `judgeRows` is emitted alongside it.

- **[ADR 0039](docs/internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md): the maintainer
  may build any template; grow-by-pull becomes an input, not a gate.** Amends
  [ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md) for Tier 2 and Tier 3. With the
  Tier-1 floor complete, zero external users, and **zero issues ever filed**, a strict pull gate was not a
  gate but a stop: 151 Tier-2 and 27 Tier-3 candidates could never be built, because no population existed
  from which a pull could arrive. That is the chicken-and-egg ADR 0021 named, one tier up and with no
  scheduled escape. **The load-bearing half does not change**: coverage and real usage stay separate honest
  numbers, "zero real fills" stays visible, and every bundle still faces the full pipeline, the four-lens
  review, and ADR 0030's admission test. **Discretion is about which types get built, never about the
  standard they are built to.** Records its own accepted cost plainly, that coverage-first is now guarded by
  judgment rather than by rule, and carries a falsifier: re-open at roughly forty bundles with still-zero
  external fills.
- **[ADR 0040](docs/internal/decisions/0040-free-and-open-source-no-paid-tier.md): free and open source
  under Apache-2.0, no paid tier.** Closes **VL-1**, open **43 days** against a three-day SLA, which never
  triggered the SLA because it carried no stated resolution cost. It had blocked the site track from
  choosing a domain or a call to action. Open core was rejected for now because it needs entitlement
  machinery before it has content, and the tier that would most plausibly carry a price is separately closed
  as "no". Names its own cost: the maintenance is funded by the maintainer's time indefinitely with no
  mechanism that scales it, which is **the counterweight to ADR 0039** having just removed the rule that
  limited how many bundles may be built.
- **[`.claude/README.md`](.claude/README.md)**, stating that the directory is maintainer-internal, why the
  build harness is a slash command rather than a skill, and the one rule that matters: **do not create
  `.claude/skills/`**, because anything placed there ships to every installer. That is not hypothetical; it
  is what [ADR 0037](docs/internal/decisions/0037-keep-the-build-harness-off-the-published-skill-surface.md)
  was written to fix.

- **[`docs/internal/pull-queue-spec.md`](docs/internal/pull-queue-spec.md)**, the executable spec for
  WP-32 (demand capture). It exists because [ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md)
  demand-gates Tier 2 and Tier 3, and the Tier-1 floor is now complete, so **the demand gate is the only
  gate left on new content and it has no door in it**. Written after verifying that the work is **half
  built, not unbuilt**, which both the roadmap's M3 table and a planning review had wrong: the three
  intake templates in `.github/ISSUE_TEMPLATE/` shipped 2026-08-07. What is missing is the mechanical
  half. **Zero issues have been filed**, the three labels those templates declare do not exist in the
  repository, `docs/reference/pull-queue.md` does not exist, and `atlas/catalog-data.json` still carries
  `built` with no `state`. One decision inside it stops for the maintainer: the demand rule.
- **[`docs/internal/plan-inventory.md`](docs/internal/plan-inventory.md)**, a dated inventory of what is
  planned, what is specified, and what is neither. It answers three questions that took a working session
  to reassemble from seven documents, two of them untracked. Its findings: **there is no forward-looking
  release plan** (no document names the next version or what earns it, and both patch releases so far were
  cut as corrections rather than shipped as increments); **four of six build specs are complete, idle, and
  untracked**, living in the gitignored audit package where no check can see them go stale; and every
  roadmap item that would deliver value to a person who has not adopted the library is unbuilt.

- **`tools/check-version-agreement.py`**, CI step 22, gating the version across `library.json` (library and
  every declared component), `.claude-plugin/plugin.json` and each declared skill's `metadata.version`.
  Listing clause **L4** requires them to agree and names its verification method as "review"; cutting
  `v0.3.1` meant hand-editing that string in six places, one of which is half of a URL. Mutation-checked
  three ways. Two of the six are deliberately not duplicated: `INDEX.md` is the Standard's own **G4**
  (verified by mutation rather than assumed), and the README badge is `check-readme-version.mjs`, which
  ships in `agent-skills-toolkit` and which CI **cloned and then never invoked**. It is now invoked.
  **CI steps: 24 to 25.**
- **[ADR 0038](docs/internal/decisions/0038-what-the-circularity-signature-obliges.md), `proposed` and not
  accepted** - the first record in this library to sit unaccepted. What the measured circularity signature
  obliges. It proposes a rule rather than a template edit, and states that **"the eval said so" is not an
  admissible reason** for changing a template.

  **Substantially revised 2026-08-10, withdrawing its own first recommendation.** That draft proposed
  adopting three of four properties; it rested on a number the protocol never gated, and treated four
  things as one kind of thing. The revision proposes an **element admission test** (E1 sourced, E2 or
  labelled as the library's own with a falsifier, E3 homed in the right artifact, E4 sized to lean) and a
  **three-track triage** routing any candidate property to a rubric row, a house convention, or a template
  element. **Two of the four leave the scope conversation at step 1**, because "this document should not
  contradict itself" makes no claim about the world and so needs no source.

### Changed

- **The eval protocol's two open instrument questions are both decided (2026-08-14), completing option D of
  [ADR 0038](docs/internal/decisions/0038-what-the-circularity-signature-obliges.md).**

  **The held-out gap is deliberately NOT gated**, and the reason is recorded so that the next person must
  beat the reason rather than simply pick a number: **a template that does exactly what it says and no more
  may be working correctly**, so there is no defensible value at which a held-out gap becomes a failure.
  Setting a target would assert that these templates *ought* to improve properties they never mention, and
  nothing establishes that they ought to. The number stays reported, since a non-gated number is not a
  suppressed one and removing it would hide the circularity signature itself. It may not be used as a pass
  or a fail, and no scope decision may be driven from it alone.

  **Held-out criteria are now drawn independently and coverage is measured afterwards.** The old method
  (search the templates for absences, then measure those absences) biased toward null by construction and
  was close to circular in its own right. The new order is: draw from the decision-usefulness literature
  without reading the template, *then* measure how many the template covers, *then* score. **This converts
  coverage from an artifact of the selection method into a finding**: "the template addresses 6 of the 20
  things the literature says matter" is a real sentence, where the old method made coverage near zero by
  construction. **Stated so it is not discovered later: this makes the next run incomparable with the first
  two on the held-out axis.** The rubric axis and the gates stay comparable.

  Also recorded: **the probe set and the held-out set are not independent instruments** (`prd-001` probes 2
  and 5 measure the same properties as two held-out criteria), and this is fixed *as part of* the rewrite
  rather than before it, because fixing overlap against criteria about to be replaced is work against a
  moving target.
- **[ADR 0038](docs/internal/decisions/0038-what-the-circularity-signature-obliges.md) accepted 2026-08-14**,
  ending the only period in this library's history when a decision record sat unaccepted. **Option C, adopt
  nothing, was rejected consciously rather than skipped**, which is what the record asked for. What is
  adopted is the rule plus the instrument fix; **no template changes as a result.** Both follow-through
  items it committed to are done in this same change: the test is written into
  [`decision-procedures.md`](docs/internal/decision-procedures.md) as **procedure 12**, so it is citable
  from any bundle rather than living inside one ADR about one eval, and the gap question is added to
  [`bundle-pipeline.md`](docs/internal/bundle-pipeline.md) as **standing research dimension 6**. That second
  one is the part that makes it systematic: *"what does a good document of this type do that this bundle
  does not ask for?"* had been asked exactly once, accidentally, three bundles into twenty-six, as a
  byproduct of building an evaluation. The dimension carries the rule that a null result is a real result
  and gets recorded, and the constraint that it must not read the bundle's own rubric before searching, for
  the same reason held-out eval criteria must not be drawn from the template.
- **`STATE.md`: D4 (regulated-industry appetite) and VL-1 (business model) both closed**, leaving D1 (the
  Layer 1 generator, correctly gated on a usage signal) and VL-3 (maintenance cadence, scheduled at M6) as
  the only open entries in that table. Three positions previously carried implicitly are now recorded under
  "Open by choice, not by oversight": the **sidecar-asset scope** question is deliberately left open, since
  deciding it now would be writing a rule with no subject; the **family-wide rubric-threshold rewording** is
  **scheduled** and explicitly not to be re-argued per bundle, after three independent reviewers raised it;
  and the **2026-08-05 agentic-era research is parked with its three false premises named**, rather than
  promoted or deleted.
- **[`docs/internal/roadmap.md`](docs/internal/roadmap.md) refreshed to 2026-08-14, in place rather than
  rewritten.** Its status column dated 2026-07-28 had claimed 18 of 27 Tier-1 types were built and that
  `v0.2.0` was the next release, **through three tagged releases**, while every counts marker in the file
  matched the tree. That is the blind spot `check-counts.py` prints on every run, costing something for
  the second time: **the check compares markers and cannot read the prose around them.** M2 is now
  recorded as done with its real exit (four releases and Gold tier, not `v0.2.0`), M3 and M4 carry dated
  per-work-package status blocks, section 4's calendar is marked overtaken with what actually consumed
  weeks 3 through 6, and section 6 records **which of its own risks fired**. Two of them did. The
  roadmap-goes-stale risk fired *and its tripwire missed it*, because the signal it watches is "STATE.md
  older than the last tag", which stayed green while this file drifted; the two are different documents.
  The historical projections are preserved rather than edited, per the correction convention this
  repository uses on decision records.
- **[`STATE.md`](STATE.md)'s "Next milestone" section reconciled with the tree.** It still said "M2, the
  machine layer, is under way" and tracked WP-25 through WP-28 toward `v0.2.0`, **while its own header
  block three screens above said the Tier-1 floor was complete**. The file contradicted itself, and the
  half that was wrong is the half that says what to do next. M2 is now recorded as complete with its real
  exit, the four WPs are broken out with verified status, and the direction is M3. **Auditing those four
  rows found a deliverable that was silently dropped:** WP-25's fill tooling was never built.
  `tools/strip-template.py` does not exist and `filled_by` appears in **zero** files under `templates/`,
  which nothing had recorded. WP-26's `fetch_status` column was superseded by
  [ADR 0029](docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md) rather than
  forgotten, and two of WP-27's named files do not exist, one of them covered elsewhere under a different
  name. **This is the same class as DF-5 (prose drifts where no marker sits)**, whose last recorded
  instance was in this same file, and it is the first time the drift was in the section that tells a
  reader what to work on rather than in one that describes what exists.
- **One of the eval's three judge seats now runs a different model from the generator.** Until now every
  seat and the generator were the same model, so nothing separated the scorer from the writer in either
  completed run; the mitigation had been skipped deliberately to protect comparability with the pilot, and
  that reason expired when the pilot's headline was withdrawn. **Stated as a partial mitigation**: every
  model reachable from the harness is a Claude model, so a shared-vendor idiosyncrasy is untouched. The
  per-seat model is emitted on every row as `judgeModel`, making "does the diverse seat actually disagree"
  a measurable question rather than an assumption.
- **`check-workflow-prompts.py` now parses every workflow script**, not just heuristically scanning it,
  and its docstring's claim that "no check in this repository can stand in for" proving a script loads is
  **corrected in place** as too strong. The reason nobody had done this: `node --check` on a `.mjs`
  workflow script reports a SyntaxError on a **completely correct file**, because the top-level `return`
  every workflow body ends with is legal inside the runtime's async wrapper and illegal in ESM. Wrapping
  the body first reproduces the runtime's framing. **The two checks are complementary and neither is
  redundant**: the 2026-08-05 defect's stray backticks *rebalanced* into valid syntax, which a parser
  cannot see by construction, while the heuristic cannot see an unbalanced brace. Both branches
  mutation-tested.
- **[`eval-protocol.md`](docs/internal/eval-protocol.md) records that the held-out gap has no validity
  gate**, and, separately, **who the judges are** - a validity-relevant fact the protocol had never
  stated. The protocol defines four gates and none of them is about it, so a value like `-0.03` is
  **neither a pass nor a fail** and no decision can be driven from it without inventing a threshold at the
  moment of deciding. Two further properties are recorded with it: the gap measures **spillover**, which
  was never established as a reasonable expectation, and held-out criteria are **selected by searching the
  templates for absences**, which biases the measurement toward a null result. Two candidate fixes are
  named and **neither is adopted**, because changing the instrument is a maintainer decision.

### Fixed

- **The 2026-07-10 audit's flagship content review is applied, five weeks late, in the half that could be
  applied without inventing sources.** It is the only substantive critique anyone has written of this
  library's *advice quality* rather than its governance, and it had sat untouched.

  **CR-5, the traceability gap, contained a trap in its own proposed fix.** The `prd` example declared
  six functional requirements against four stories: **FR-2 (list and switch views) is a `Must` and had
  no story at all.** The review proposed adding the line *"every Must/Should FR must map to at least one
  story"*, which **would have shipped a document stating a rule its own content broke.** Applied in the
  other order: the missing FR-2 story first, then the rule, which is now true. FR-6 stays uncovered and
  is named as a deliberate `Could` rather than left a silent gap. The guide's full-variant rubric gains
  the matching line.

  **CR-7, two of four notes.** The `user-stories` example carried **two `## Story` headings at the same
  level as their own parents**, so its outline read flat in a library that teaches structure; inner
  headings demoted to `###`. The `prd` companion named a "solution brief" this library does not
  template; **half that reference became resolvable since the review was written**, because PR/FAQ now
  ships as a `product-vision` format, so it links there and the solution brief is flagged out of scope.

  **CR-6 recorded as the review asked:** catalog entry 29 signals `S/M/L` and the bundle ships two
  variants. Legal under [ADR 0002](docs/internal/decisions/0002-variant-model.md), which lets the type
  decide, but documented nowhere until now. A true four-section `S` variant is **deferred until a real
  user asks**.

  **Held, with reasons, not overlooked.** CR-1, CR-2, CR-3 and CR-7's fourth note all add teaching
  claims about how practitioners work, and **the review supplies no sources for them**; writing them
  from its summary would be this library's dominant defect committed on purpose. **CR-4 is now gated by
  a rule that post-dates it**: adding an "Alternatives considered" section is an *element* addition, so
  it faces [decision procedure 12](docs/internal/decision-procedures.md), whose E1 clause wants a named
  source found by a search capable of returning "no". The review asserts "the strongest real PRDs" carry
  such a block and names none. **This is the first candidate to meet procedure 12 since it was adopted,
  and it does not pass on the evidence available.** Not rejected; unresearched.

  No `template_version` changes: the edits are to an example, a guide rubric, a companion
  cross-reference, and a history entry.

- **A claim this repository published about someone else's software was wrong.**
  [`roadmap.md`](docs/internal/roadmap.md) recorded that `skills add <repo>@<ref>` "prints the ref and
  clones the default branch anyway", concluding that nobody pinning a version through that CLI gets one.
  **`@` is not the ref separator. `#` is, and it works**, shown by a five-cell probe in which `#v0.2.1`
  returns a skill existing only at that tag and `#v0.1.0` correctly finds nothing in a tree with no
  `SKILL.md`. Withdrawn, and nothing was filed upstream because there was nothing to file. It is the third
  finding withdrawn in two days for the same reason: **one observation with no control beside it**.

## [0.3.1] - 2026-08-08

A documentation patch. No bundle content changed, no structure changed, and no gate check was added.

### Fixed

- **The `v0.3.0` tag shipped documentation that its own contents contradicted.** The doc-honesty sweep
  landed one commit *after* the tag, so the tagged tree the marketplace pins carried `AGENTS.md`,
  [`what-the-gate-proves.md`](docs/explanation/what-the-gate-proves.md),
  [`getting-started.md`](docs/tutorials/getting-started.md) and `STATE.md` all still telling readers
  **"there are no efficacy evaluations"**, inside a tree that contains `evals/results/` holding two of
  them. Those corrections are unchanged from `main`; this release is what publishes them.
- **`RELEASE-NOTES.md` still said template quality "has not been measured"** in its standing *"What this
  library does not claim"* section, three headings below its own `v0.3.0` entry reporting that two
  independent runs returned VOID. The sweep edited this file and missed its trailer.
- **[ADR 0036](docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md) called the install
  retest one that "has never been run", and said it "stays open"**, in two places, after that retest had
  been run and its consequences written into the adjacent
  [ADR 0037](docs/internal/decisions/0037-keep-the-build-harness-off-the-published-skill-surface.md).
  Marked in place with a dated correction rather than rewritten, because both statements were true when
  written.
- **Three of the four version headings in this file were not links.** `## [0.3.0]`, `## [0.2.1]` and
  `## [0.2.0]` are shortcut reference links with no matching definition, so they render as literal
  bracketed text, while `## [0.1.0]` renders as a link. `[Unreleased]` also still compared against
  `v0.1.0`. Nothing caught it: `check-links.py`'s `LINK_RE` matches inline `[text](url)` only, so a
  reference-style link is invisible to it.

### Changed

- **Version to `0.3.1` in all six places it is written**: `library.json` twice (the library and its one
  component), `.claude-plugin/plugin.json`, `skills/plt-fill-template/SKILL.md` `metadata.version`,
  `INDEX.md` (regenerated, not hand-edited), and the `README.md` shields.io badge. Listing clause **L4**
  requires the registry entry, the release tag, `library.json` and every native manifest to agree. The
  skill's `metadata.version` is **not cosmetic**: the skill fetches its templates from the release tag
  matching it, so a stale value points every installed copy at the wrong tree.

### Why this is a separate release

A published tag is not moved. The precedent is `v0.2.0` to `v0.2.1`, cut for exactly this shape and
recorded in [`release-process.md`](docs/internal/release-process.md). The alternative was leaving every
plugin user installing a tree that disagrees with itself about the one property this library is most
careful about.

## [0.3.0] - 2026-08-08

### Added

- **A `## TL;DR` block on every decision record.** Each is derived from the record's own decision section
  rather than its title, and the Status bullet carries any correction, amendment or supersession the record
  contains, so a reader who stops at the summary cannot walk away with a superseded decision.
- **An architecture pair under `docs/explanation/`**: [`architecture.md`](docs/explanation/architecture.md)
  for a reader who wants the shape in one sitting, and
  [`architecture-detailed.md`](docs/explanation/architecture-detailed.md) for someone extending the library.
- **Folder READMEs** for `templates/`, `.github/workflows/`, `docs/releases/` and each Diataxis quadrant.
  The `templates/` inventory is generated from each bundle's own `*_meta.yaml`, so its axis and variant
  columns cannot drift from the tree.
- **`RELEASE-NOTES.md`** at the repository root: the curated user-facing read, distinct from this file,
  which stays the full record.

- **The efficacy eval gained a matched treatment arm, and the pilot's headline finding was withdrawn.**
  The pilot's arms differed in **two** things at once: the control received seven discipline points, two
  naming decision-usefulness properties, and the treatment received a template and a guide and no
  discipline instruction at all, while held-out criteria scored exactly those properties. A two-variable
  difference cannot be attributed to one variable. The new **T+** arm receives the identical discipline
  block, byte-identical rather than paraphrased and held that way in CI, and judging is split into two
  panels per scenario so every gap is computed inside one comparison set.

  **Run twice, independently. The held-out gap goes from -0.51 unmatched to -0.03 matched**, with the
  matched interval spanning zero, and the two runs agree within 0.13 on every quantity. The alarming
  finding was the harness. **What replaces it is the circularity signature, now measured**: +0.85 on the
  templates' own rubric criteria beside nothing at all on criteria drawn from neither. Both runs remain
  **VOID** on discrimination. [The result](evals/results/2026-08-08_matched-rerun.md).
- **Bootstrap confidence intervals** ([`evals/harness/analyze.mjs`](evals/harness/analyze.mjs)), closing a
  protocol requirement the pilot recorded as unmet. It resamples **scenarios rather than judge-artifact
  rows**, because three judges scoring one document are not three independent observations.
- **`tools/check-export-surface.py`**, asserting that the set of skills an installer would export equals
  exactly what `library.json` declares, in both directions. See the install finding under Fixed.
- **`tools/check-eval-arm-parity.py`**, holding the two eval arm prompts byte-identical on their shared
  discipline block.
- **[`docs/how-to/installing.md`](docs/how-to/installing.md)**, the first real install guide: three routes,
  what each one actually delivers, and how to verify each worked.
- **[ADR 0037](docs/internal/decisions/0037-keep-the-build-harness-off-the-published-skill-surface.md)**,
  keeping the build harness off the published skill surface and gating the surface rather than trusting the
  layout.

### Changed

- **The four user-facing pages moved into the Diataxis quadrants** the Advanced Skill Library Standard
  requires, and every inbound link was updated. Anyone linking the old paths should re-point:

  | Was | Now |
  |---|---|
  | `docs/getting-started.md` | [`docs/tutorials/getting-started.md`](docs/tutorials/getting-started.md) |
  | `docs/filling-a-template.md` | [`docs/how-to/filling-a-template.md`](docs/how-to/filling-a-template.md) |
  | `docs/choosing-a-template.md` | [`docs/reference/choosing-a-template.md`](docs/reference/choosing-a-template.md) |
  | `docs/what-the-gate-proves.md` | [`docs/explanation/what-the-gate-proves.md`](docs/explanation/what-the-gate-proves.md) |

- **Every published `docs/**` page now carries the Standard's section 8.4 frontmatter taxonomy**
  (`title`, `description`, `audience`, `level`), including the two release notes, which keep their
  `release-notes` template frontmatter alongside it.

- **Convergent tier on the Advanced Skill Library Standard**, measured rather than declared. The library
  takes the component prefix `plt-` and its skill moves from the repository root to
  `skills/plt-fill-template/SKILL.md`, per
  [ADR 0036 (the library prefix and the skill's path)](docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md).
  **This changes the installed skill's name** from `product-lifecycle-templates` to `plt-fill-template`;
  the plugin keeps its name. The move is not a compliance chore: the Agent Skills specification requires a
  skill's `name` to match its parent directory and the Claude Code plugin loader scans `skills/`, so a
  `SKILL.md` at a repository root is not discoverable by either. **Corrected before release:** the
  "never discoverable" inference was tested on 2026-08-08 and is **false for the skills CLI**, which looks
  for a root `SKILL.md` by design and short-circuits its subdirectory search on finding one. The move was
  still required by the Standard. `npx skills add` was run for the first time on 2026-08-08 and
  **succeeds**; what it found is below.

- **The first efficacy measurement, and it returned VOID.** `evals/` now holds a three-arm blind eval
  harness, a scenario bank authored blind to the templates, per-type rubrics split into rubric criteria and
  held-out criteria, and [the protocol](docs/internal/eval-protocol.md) written before any number existed.
  The pilot ran six scenarios across three bundles.

  **The instrument works and the result is not flattering.** The hollow arm, a template filled with fluent
  generic filler, scored 1.00 overall and answered zero of five retrieval probes, so the rubric measures
  substance rather than shape. Judge agreement and control sanity both passed. But the overall gap was
  **+0.19** against a 1.0 discrimination gate, so the run is **void**, and the held-out gap was
  **negative at -0.81**. **That -0.81 was withdrawn before this released**, in the same development cycle:
  see the matched re-run below. A confound this run introduced is stated in
  [the results](evals/results/2026-08-08_pilot.md) rather than left for a reader to find. **No number from
  the pilot appears in the README, a badge, or any bundle's metadata.**

### Fixed

- **The install shipped a maintainer-internal skill, and now cannot.** `npx skills add` was run for the
  first time on 2026-08-08 and reported **two** skills, installing both. The second was the build harness,
  whose own description says it is not for library users. Nothing was done wrong to cause it: a root
  `SKILL.md` short-circuits the installer's subdirectory search, this repository had one until v0.2.0, and
  removing it switched the search on. The harness is now a slash command at
  [`.claude/commands/build-bundle.md`](.claude/commands/build-bundle.md), invisible to the installer and to
  the Standard's component discovery, verified against the real repository. **The relocation is the small
  half**; `check-export-surface.py` is what stops the next one, most likely in `.codex/skills`, which is on
  the same hardcoded scan list.
- **The `npx skills add` route installed a skill that could not do what it said.** Twelve kilobytes land:
  the skill and its README, and none of `manifest.json`, the 26 bundles, or any file the skill's own links
  point at. Its step 1 is "Read `manifest.json` at the repository root", and after an install there is no
  repository. An agent in that position usually produces a fluent document anyway, from the skill's
  description rather than from a bundle, which is exactly the artifact this library exists to replace. The
  skill now **stops and says the library is absent** rather than improvising, and can fetch the manifest
  plus the one template it needs from the release tag matching its own declared version. The Claude Code
  plugin route clones the whole repository and never had this problem.
- **`check-counts.py` read fenced code blocks as live claims** and gated dated release notes against the
  current tree, which would have forced the v0.2.0 note's true sentence "the gate grew from 15 CI steps to
  20" to become false. Fences are now blanked and `docs/releases/` is exempt by directory, printed on every
  run.
- **`check-workflow-prompts.py` was not looking at the eval harness.** It globbed `.claude/workflows/*.js`
  and found one file, so the tool written because a broken harness is invisible until it runs was not
  reading the most recently written harness. Discovery is now by shape.
- **`STATE.md` was false in the section that ends "Keep this section honest".** Five clauses had been wrong
  for three weeks: no machine-consumption path, ships no `SKILL.md`, not installable, untagged, and 6 of 205
  types against a real 26. Every marker in the file was green throughout, because none of those clauses sits
  near a marker.
- **Stale README badges.** version 0.1.0, bundles 19, Tier-1 floor 18 of 25, families 5. The counts check
  cannot see numbers inside shields.io URL parameters, and its own docstring names this exact recurrence.
- **`bash.exe.stackdump`**, a 539-byte Cygwin crash dump committed in #53, was tracked at the repository
  root and shipped inside v0.2.0 and v0.2.1. Deleted and gitignored.

### Known gaps

- **Nothing from the efficacy eval may be quoted as a quality claim.** Two runs, both **VOID**. The
  templates score well above a strong generic-prompt control on the bundles' own rubric criteria and no
  better than it on criteria drawn from neither, which is the circularity signature. Three of 26 bundles.
- **The probe instrument is saturated.** The control answered 5.00 of 5 in both sessions of both runs, so
  the probe gap can now show harm and not help. Harder probes come before the next run.
- **`check-export-surface.py` copies an upstream constant.** The installer's scanned-prefix list is
  hardcoded in a package that ships often. If it grows, the check goes stale by continuing to pass. Its own
  output says so, and the honest mitigation is to re-read the list when the installer majors.

## [0.2.1] - 2026-08-08

### Added

- **`library.json`**, binding the Advanced Skill Library Standard at version `0.12` and declaring conformance
  at tier **universal (Bronze)**. Required by clause **L3** of the Product on Purpose marketplace listing
  contract: a repository with no `library.json` is "loose components" under the Standard and **is not
  eligible for a new listing**. The tier is not self-declared: the Standard's own gate
  (`agent-skills-toolkit/scripts/check.mjs`) was run against this repository and exits 0 at universal, with
  the remaining findings belonging to the convergent tier above the declared ceiling.

### Changed

- **`.claude-plugin/plugin.json` version to 0.2.1**, because listing clause **L4** requires the registry
  entry version, the release tag, `library.json` and every native manifest to agree.

### Why this is a separate release

`v0.2.0` was tagged before the listing contract was read, and its commit does not contain `library.json`.
A published tag is not moved to fix that. This patch adds the manifest and re-cuts, so the version the
registry pins sits on a tag whose tree actually contains what the tag claims.

## [0.2.0] - 2026-08-07

**The Tier-1 floor is complete.** 26 bundles covering all 25 templatable Tier-1 document types, nine
families, 20 CI steps, 20 gated research logs across 796 sources. This release also gives the library a
front door: its first user-facing documentation and its first installable surface.

### Added

- **`incident-postmortem` and `sprint-retrospective-notes` bundles, completing `process-docs`**
  (2026-08-07, #75). Landed together because the family contract says they exist to be contrasted. **Both
  turned on a full-text count of their own canon, and both counts were zeros**: the word "timeline" appears
  **0 times** in Google's SRE book chapter 15, existing only as a heading in a separately linked appendix
  (re-verified against the live page, not taken from the research pass); and the 2020 Scrum Guide contains
  **0** occurrences of "action item", "retrospective notes" and "notes", requires no written output at all,
  and in 2020 **softened** the 2017 requirement that an improvement reach the next Sprint Backlog into a
  permission. A requirement became a permission, which is the argument for the retrospective notes document
  existing.
- **`status-report` bundle, completing the Tier-1 floor** (2026-08-07, #78). The twenty-sixth bundle and
  the last Tier-1 type. **Exactly one methodology specifies this document** (PRINCE2's Highlight Report);
  GovS 002, the UK's live cross-government project standard, looks at it and deliberately declines to.
  Its weakness is **measured rather than argued**: across the records of 56 experienced project managers,
  reports were biased 60 percent of the time and more than twice as likely to be optimistic as
  pessimistic. **The build backlog is now empty.**
- **`SKILL.md` and `.claude-plugin/plugin.json`** (2026-08-07). The library becomes installable rather
  than clone-only. Until now `npx skills add` cloned the repository and installed nothing, because both
  the skills CLI and agentskills.io take exactly one unit, the skill, and this repository shipped no
  `SKILL.md`. One missing file, not an architecture problem.
- **The first user-facing documentation this repository has had.** `docs/getting-started.md`,
  `docs/choosing-a-template.md`, `docs/filling-a-template.md`, `docs/what-the-gate-proves.md`,
  `CONTRIBUTING.md` and `AGENTS.md`. Before this, all 62 documentation files lived under `docs/internal/`:
  the library documented how it governs itself far better than how to use it.
- **[`tools/gen-research-log.py`](tools/gen-research-log.py) and its 38-assertion self-test** (2026-08-07,
  #77), CI step 20. Generates a research log's source entries from the fan-out's own output, fixing two
  bugs that **destroyed evidence silently**: dedup on raw URLs filed one source under two numbers, and a
  merge that replaced rather than unioned left one entry holding 4 of its 10 verified quotes. Every
  assertion is mutation-checked, and the mutation was run rather than asserted.
- **Decision procedure 11, "a family contract asserts something about the world"** (2026-08-07, #79). A
  contract sentence is an OBLIGATION, a CLAIM or a POSITION, and must read as which. Contracts now carry a
  dated research-confirmation line recording what survived contact with their members' research.

### Changed

- **CI runs the gate on every branch, not only `main`** (2026-08-07, #74). PR #73 opened at 22:38 and its
  `pull_request` run did not dispatch until 23:01, so for twenty-three minutes the required check did not
  exist and the PR was merged with `--admin`, overriding the repository's own no-admin-merge rule. A push
  dispatches immediately, so a feature branch now has a green required check in about thirty seconds.
- **`check-counts.py` reads every marker in a file, not just the first** (2026-08-07, #77). An author who
  knew a sentence quoted a number previously had no way to pin it, which is why prose-count drift (finding
  DF-5) recurred eight times with identical geometry. It found a defect on its first run: `README.md` said
  "All nineteen bundles currently pass" against a tree of 25, 142 lines below a green and correct marker.
- **CI actions bumped to `checkout@v5` and `setup-python@v6`** (2026-08-07). The previous versions target
  Node 20, which GitHub deprecated and is force-running on Node 24.
- **`.gitattributes` pins `*.md`, `*.yaml`, `*.yml` and `*.json` to LF** (2026-08-07, #77).

### Fixed

- **Eight unsourced claims across seven family contracts** (2026-08-07, #76, #79, #80), each relabelled in
  place under procedure 11, **none changing an obligation**. Two of three failures were labelling rather
  than error: correct content stated as though the field had discovered it. `decision-docs` was the one
  contract found clean, and clean properly, with all eight of its assertions traced to named log entries.
  **The defect has a signature phrase**: "the most common real-world failure/confusion is", unsourced in
  all three contracts that used it.
- **A stale count in `README.md`** that no marker was tracking, and a self-contradicting cell plus a stale
  ADR count in `STATE.md` (2026-08-07, #74, #77). All were the DF-5 pattern: a sentence a hundred or more
  lines from the marker at the top of its file.

### Earlier in this release

Backfilled 2026-07-26 covering 28 commits since 0.1.0. This section was empty while nine bundles, five
family contracts and fourteen decision records landed, which is recorded as finding DF-3 (gated documents stay fresh, ungated ones drift) in
[`STATE.md`](STATE.md) rather than quietly corrected: the documents this repository gates for freshness
stayed fresh, and the ones it does not gate drifted.

### Added

- **`definition-of-done` and `runbook` bundles, completing `standing-standards`** (2026-08-06). The
  twenty-second and twenty-third bundles, landed together because they share a contract and because the
  family's set-valued gating only means something with both members present. **The first family whose two
  members take different values on the same axis**: `classification: foundation` for the standard you are
  judged against, `classification: tool` for the instrument you execute. That set has carried only a check-K
  fixture since ADR 0023; this is its first live subject.
  **Both members ship a named Review Trigger section** with an owner and a condition rather than a calendar,
  and the research established that obligation twice over independently: neither the Scrum literature nor
  the SRE literature supplies a condition-based trigger, and both reach for cadences.
  **`definition-of-done`** was researched against the 2020 Scrum Guide directly, because the family contract
  names "folklore presented as standard" as this type's citation hazard. Three things everyone says about a
  Definition of Done are **not in the Guide**: that it is a checklist, that it is the team's contract, and
  that it gets stricter over time. What the Guide does say is that the **Developers** conform, and that an
  organisational standard is a **floor** teams may raise and never lower. It ships `[lean, full]` against a
  spec that called for one size, because published DoDs vary about sevenfold and the variance tracks scope.
  **`runbook`** ships the incident-scoped shape rather than the 65-header service-operations manual, on the
  family contract's own definition. Its sharpest finding is that **Google's SRE canon does not use the word
  runbook**: across seven chapters searched by full text it appears three times, every one inside a
  contributed third-party case study, and four of the chapters most likely to discuss it contain zero
  occurrences of either word. The four circulating MTTR statistics for runbooks are quarantined, none
  traceable to a method, including the percentage figures widely attributed to Google, which do not exist in
  its text.
- **A correction to the merged `acceptance-criteria` bundle.** It stated that "the development team owns the
  DoD, with the Product Owner having final say", citing a Scrum.org page its own reference entry records as
  HTTP 403 and never read. The 2020 Guide does not support it, and "development team" is vocabulary that
  edition retired.

### Changed

- **`prototype-brief` does not ship, and `discovery-docs` closes at two members**
  ([ADR 0035](docs/internal/decisions/0035-prototype-brief-fails-the-admission-test.md), **accepted
  2026-08-05**). The type was ratified as a **provisional** member by ADR 0031, conditional on its own
  research passing ADR 0030's admission test that a named source must publish it as a written document. **It
  failed.** Six research dimensions and 29 sources found prototyping practice everywhere and a commissioning
  document nowhere: GOV.UK's guidance is built around a code toolkit, which is structurally why `wireframe`
  was rejected; Google Ventures' Sprint Brief is real and named but scopes an entire five-day sprint, with
  the prototype's own plan produced mid-sprint as a storyboard; Strategyzer's Test Card is a card for
  business-model assumptions; and every assumption-test ancestor, Lean UX included, stops at a canvas or a
  worksheet. All six dimensions converged although only the first was asked the admission question.
  Shipping it anyway would have meant presenting an adjacent artifact under this type's name, the defect
  that got V2MOM rejected. The backlog drops to five, the Tier-1 floor is unchanged because this type was
  never one of the 27, and catalog entry 54's note is corrected from asserting the brief ships. The evidence
  is preserved in [`prototype-brief-admission-evidence.md`](docs/internal/prototype-brief-admission-evidence.md)
  and the record states four falsifiable conditions that would reopen it.

### Added

- **`user-persona` bundle, the twenty-first and the second `discovery-docs` member** (2026-08-05). Eight
  files, 45 researched sources of which 33 were read in full, `phase: discover`, sizes `[lean, full]`,
  `pairs_with: []`. **It defines the Recurring Analyst**, referenced across 19 files in this repository with
  no bundle having defined her, and its example is now the earliest document in the library. **The research
  changed the build spec in four places**: the anti-persona ships as a separate document rather than a
  section, "Behaviors" gets no standalone heading because none of the six published formats read carries
  one, a bounded "Quotes/Evidence" block appears in none of them, and `buyer persona` leaves the aliases
  because it is a different artifact scoped to the purchase decision. **The type's own canon could not be
  read**: *The Inmates Are Running the Asylum* chapter 9, *About Face* and *The Persona Lifecycle* were all
  unreachable, so the bundle states nothing about what they say, and Cooper is quoted from his own later
  essays instead, including that he gave the term away. The template carries a declared **evidence tier**,
  following Nielsen Norman Group's three-tier ladder, and the circulated 900 percent persona statistic is
  taught as an example of a number that traces to one uncontrolled case study isolating nothing.
- **`check-workflow-prompts.py`, gating a harness failure nothing else could see** (2026-08-05). A backtick
  written as markdown inside a workflow prompt closes the prompt's own template literal and makes the script
  unloadable. It shipped through a green PR and passed `node --check` with exit 0, because the stray
  backticks rebalanced into expressions Node tolerates. Nothing in CI parsed the workflow scripts before
  this. The check says in its own output that it cannot prove a script loads, because only invoking the
  Workflow tool proves that. Second failure of this shape after CRLF, and recorded as gotcha 7.
- **`business-case` bundle, the twentieth and the first `discovery-docs` member** (2026-08-05). Eight files,
  43 researched sources, `phase: discover`, sizes `[lean, full]`, `pairs_with: []` because no pm-skills skill
  serves this type. **One format ships**: the Five Case Model, with the SAFe Lean Business Case **deferred on a
  stated retrieval gap** rather than rejected, since only a practitioner mirror was read and not Scaled Agile's
  own page. Its central teaching point is that every standard readable in full treats the case as a **living
  document** while most use is a one-time gate, and its honest core is that **product-management literature is
  hostile or silent**: no product source found makes a positive case for the artifact. **PMBOK 7 could not be
  retrieved** despite being named a key source for this type, so the bundle states nothing about it, and the
  circulated benefits-realisation statistics (McKinsey, KPMG, PMI, Standish) are **quarantined, not cited**.
  Its worked example is the first to extend the Acme Analytics thread **backward**, dated eight days before the
  FY26 product strategy whose plans spend the investment it argues for.
- **The last three family contracts, adopted** ([ADR 0032](docs/internal/decisions/0032-adopt-standing-standards-family-contract.md),
  [ADR 0033](docs/internal/decisions/0033-adopt-process-docs-family-contract.md),
  [ADR 0034](docs/internal/decisions/0034-adopt-communication-docs-family-contract.md), **accepted 2026-08-05**):
  `standing-standards` (definition-of-done, runbook) on a **set** of `foundation` or `tool`, the first family to
  pair those two values; `process-docs` (sprint-retrospective-notes, incident-postmortem) on `phase: iterate`;
  and `communication-docs` (status-report) on `classification: utility`. **Every family in the library now has a
  ratified contract**, which is what unblocks the remaining eight bundles: a contract is a hard maintainer stop,
  so an unattended run would previously have stalled at the fourth bundle. Each carries a family-specific
  obligation that is genuinely distinct rather than boilerplate - a **review trigger** with a named owner and a
  condition for standing-standards, **teaching by contrast** for process-docs, and the **no-new-facts rule** for
  communication-docs, where every figure in an example must be read from an artifact already in the library and
  disagreeing with it is a contract failure rather than a rounding difference. `tools/test-check-k.py` gains the
  fixture ADR 0032 requires for the foundation+tool combination, before its first member lands; the suite goes
  from 69 to 80 assertions.
- **The `discovery-docs` family contract, adopted**
  ([ADR 0031](docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md), **accepted 2026-08-04**):
  `business-case`, `user-persona` and `prototype-brief` on `phase: discover`, registered in check K and
  latent until the first member lands. Two firsts. It is the first family to extend the library's worked
  thread **backward** in time rather than adding new ground: its persona defines the **Recurring Analyst**
  that sixteen files across the library already reference and no bundle has ever described. And it is the
  first contract ratified with a **provisional member** - `prototype-brief` ships only if its own research
  finds a named source publishing it as a written document, and the contract pre-commits to a two-member
  family being a legitimate outcome rather than a failure. Ratifying with the condition stated is the point:
  deciding membership after the research is when a negative answer is easiest to rationalise away. The
  contract also carries a chronology obligation, since every member points forward and the `product-roadmap`
  February-citing-June defect is easiest to repeat here, and it waives example-independence grandfathering
  entirely.
- **A templating-scope rule** ([ADR 0030](docs/internal/decisions/0030-templating-scope-markdown-documents.md),
  **accepted 2026-07-31**): this library templates artifacts whose primary form is a written document, and names the ones
  it will not template rather than leaving them silently unbuilt. Applied to catalog 52 (`wireframe`) and 54
  (`interactive-prototype`), both out of scope because their artifacts are visual and executable. Adds
  **`prototype-brief`** as a new type in `discovery-docs`: the brief that commissions a prototype is a
  document even though the prototype is not. Generalises ADR 0028's format-admission test from formats to
  types. Two counts follow and are kept apart: the **catalog floor** is 18 of 25 templatable, and the **build backlog** is 8 bundles (the 7 remaining originals plus `prototype-brief`, which is not one of the 27).
  `design-docs` is therefore never created.
- **Four family contracts, drafted and pending maintainer review**:
  [`discovery-docs`](docs/internal/contracts/discovery-docs.md) (business-case, user-persona,
  prototype-brief; `phase: discover`), [`standing-standards`](docs/internal/contracts/standing-standards.md)
  (definition-of-done, runbook; **a set** on `classification`, `foundation` or `tool`, the second family to
  need one), [`process-docs`](docs/internal/contracts/process-docs.md) (sprint-retrospective-notes,
  incident-postmortem; `phase: iterate`), and
  [`communication-docs`](docs/internal/contracts/communication-docs.md) (status-report;
  `classification: utility`, one Tier-1 member, stated rather than hidden).
- **[`decision-procedures.md`](docs/internal/decision-procedures.md)**, ten recurring judgment calls with the
  precedent that earned each one. Not an ADR: an ADR records what was decided, this records how to decide.

- **`okrs` (2026-07-30), the nineteenth bundle and the fourth `strategy-docs` member, completing that
  family** and with it one continuous worked thread from a product vision down to a bug report. One format
  ships: six candidates examined individually and five rejected, then nine further named goal-setting
  frameworks checked for a counterexample. Its honest core is a tested negative, that no study measures
  whether the OKR artifact improves outcomes, and that neither the goal-setting literature nor its published
  critics mention OKRs at all.
- **`tools/check-example-independence.py`, wired into CI**, gating a defect that had recurred four times and
  survived the convention adopted to prevent it. It failed 16 of 19 bundles on first run with **zero false
  positives on triage**, which is recorded as finding **DF-6 (worked examples reuse their own template's
  guidance text)** in [`STATE.md`](STATE.md). The 16 are grandfathered at measured ceilings that may only
  shrink, with 132 copied passages outstanding.
- **Catalog entry 6 corrected**: it had listed V2MOM as "Salesforce's named variant" of OKRs since the
  catalog was written, and Salesforce's own training material defines all five V2MOM components without
  mentioning OKRs once. Corrected with a dated note in the EC-2 pattern, across `catalog.md`,
  `catalog-data.json` and `buildout-specs.md`.

- **Nine bundles, taking the library from 6 to 15**, and completing three families:
  - `delivery-docs` completed: `product-backlog`, `sprint-backlog`.
  - `decision-docs` completed: `sdd`.
  - `governance-docs`, a new family and the first on the **classification** axis: `risk-register`,
    `raid-log`, `kpi-dashboard`.
  - `qa-docs`, a new family at phase `develop`: `test-plan`, `test-case`, `bug-report`. Their examples form
    the library's first **cross-family** chain, running from a risk to a test plan row to a test case to a
    defect to the regression that guards it.
- **Five family contracts**, each ratified before its members were built and enforced by gate check K:
  [delivery-docs](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md) (ADR 0020),
  [decision-docs](docs/internal/decisions/0022-adopt-decision-docs-family-contract.md) (ADR 0022),
  [governance-docs](docs/internal/decisions/0024-adopt-governance-docs-family-contract.md) (ADR 0024),
  [qa-docs](docs/internal/decisions/0026-adopt-qa-docs-family-contract.md) (ADR 0026),
  [strategy-docs](docs/internal/decisions/0027-adopt-strategy-docs-family-contract.md) (ADR 0027, the first
  to gate a **set** of axis values).
- **A second taxonomy axis**: a bundle declares `phase` XOR `classification`, never both, never neither
  ([ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)). The Tier-1
  family map was resolved against it in
  [ADR 0023](docs/internal/decisions/0023-resolve-the-tier-1-family-taxonomy.md).
- **A format axis, orthogonal to size** ([ADR 0028](docs/internal/decisions/0028-adopt-a-format-axis.md)):
  optional `default_format` and `additional_formats` keys let one bundle ship a document in several shapes.
  Strict nesting now applies **within** a format and is never asserted across formats, because a canvas and a
  press release are siblings rather than parent and child. The default format keeps the plain filenames, so
  adopting it in an existing bundle is a metadata addition with no renames.
- **A machine-checkable metadata schema**, `tools/meta.schema.json`, validated in CI as gate check J
  ([ADR 0016](docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md),
  [ADR 0017](docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md)).
- **A generated machine catalog**, `manifest.json`, committed to version control and kept fresh by the gate
  ([ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md)), plus a generated atlas.
- **Selection metadata** for agents budgeting context: authored `default_size` and `sizing_guidance`, and a
  generated heuristic `approx_tokens` with no tokenizer dependency
  ([ADR 0019](docs/internal/decisions/0019-selection-metadata-and-approx-tokens.md)).
- **Executable tests for gate logic that has no live subject**
  ([ADR 0025](docs/internal/decisions/0025-executable-tests-for-gate-logic.md)): `tools/test-check-k.py`
  (65 assertions) and `tools/test-check-formats.py` (64 assertions). Both run in CI and block merge. Both
  counts scale with the live tree, so they are read from the tools rather than quoted from memory.
- **Freshness gates** for the generated artifacts: `gen-manifest.py --check`, `gen-atlas.py --check`, and
  `check-adr-index.py`, each added after the corresponding drift was found in the tree rather than in theory.
- **A scope commitment**: complete the catalog's 27-type Tier-1 floor on a schedule, with grow-by-pull
  reserved for Tier 2 and Tier 3
  ([ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md)). 17 of the 27 are built.
- **`product-roadmap`**, the eighteenth bundle and the third `strategy-docs` member. Ships three formats
  from eight researched: `now-next-later` (default), the GO goal-and-metric grid, and the themes format that
  carries vision and objectives inside the document. **The five rejections matter more than the three
  admissions**: the timeline form has no named product-management defender, the release plan is a different
  artifact, the release roadmap and Kanban board are a relabel and a source-less glossary entry, and the
  opportunity solution tree and Cagan's OKR alternative were excluded because their own authors do not
  present them as roadmaps. **This closes the evidence question the `default_format` backfill was waiting
  on** (D-E): ADR 0028's rule has now discriminated twice, 2 of 5 and 3 of 8. Its honest core is a confirmed
  evidence gap, and two circulating statistics were found and deliberately excluded as untraceable.
- **`product-strategy`**, the seventeenth bundle and the second `strategy-docs` member. Ships the Rumelt
  kernel (diagnosis, guiding policy, coherent action) as its default format at lean and full, plus a
  Playing-to-Win one-pager. Its honest core is a **tested negative**: no study measures whether writing a
  product strategy document improves product outcomes, and the bundle shows the search that establishes it
  rather than assuming either direction. Three further formats were researched and rejected under ADR 0028's
  rule, which is the first evidence that the rule discriminates rather than admitting everything.
  **It is also half the evidence the `default_format` backfill was waiting on**: format variation is not
  peculiar to `product-vision`.
- **`product-vision`**, the sixteenth bundle, the first `strategy-docs` member, and the first bundle to ship
  more than one format: canvas lean and full (the default), plus a narrative and a PR/FAQ at full only. Ten
  files rather than eight. A fourth shape, the positioning sentence, was researched and excluded on
  attribution grounds. Its example opens the Acme Analytics chain that runs down through the PRD to a
  regression test.
- **The research-log contract, now gated** by `tools/check-research-logs.py` (ADR 0029, built 2026-07-28).
  Every source in a checked log must carry a contiguous unique number, an identity, a URL or an explicit
  statement of why there is none, a tier, a retrieval status from the three-token enum, and a `Supports:`
  clause. All three numbered layouts are legal, because the contract is the rule and presentation is not.
  Covered by `tools/test-check-research-logs.py` (80 assertions, mutation-checked against seven deliberate
  breakages). **12 of 18 logs and 472 of 558 sources are gated**; the six table-layout logs are exempt by
  name with a measured reason printed on every run, and tracked as finding DF-4.
  **Building it disproved the finding it was built for:** the three logs ADR 0029 called status-less carry
  the contract in full, in a third numbered layout the original audit's regexes did not match. The ADR
  carries a dated correction rather than a silent edit.
  The honest-retrieval standard is this library's central quality claim, and until this landed nothing
  verified it: the requirement bound the research workflow's JSON schema, never the markdown that schema
  produces ([ADR 0029](docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md),
  finding DF-2). `Quotable:` and `Contested/time-bound:` remain optional, because the written standard says
  so.
- **Build-out documentation**: `docs/internal/buildout-specs.md` (the per-type spec sheet and progress
  tracker) and `docs/internal/bundle-pipeline.md` (the six-phase runbook, including the honest-retrieval
  standard and the adversarial four-lens review).

### Changed

- The gate grew from nine checks to **eleven** (adding check J, meta-schema validation, and check K, family
  contract conformance).
- Check A now rejects **any** undeclared `_template-*.md` file, and `bundle_files()` scans by pattern rather
  than by size vocabulary. Previously both iterated known size tokens, so a file such as
  `x_template-narrative-full.md` failed no check **and was read by no scan**, meaning it could ship without
  ever being checked for dashes, citations, or links (ADR 0028).
- The catalog's `phase` field was renamed to `stage`, to stop it colliding with the bundle metadata's own
  `phase` (TX-2).
- The README was restyled without changing its claims.

### Fixed

- **Three documentation-drift defects found while landing `business-case`**, each shipped by an earlier PR
  that updated a count without re-reading the prose around it. The README's headline statistics table had a
  fragment of **PR #46's own commit message** spliced into it ("strategy-docs member and the first bundle to
  ship more than one format"), leaving a sentence that never closed its parenthesis; `okrs` landed in PR #53
  with **no row in its family table** while the table's heading already claimed four bundles, and the prose
  still read "Three are built; `okrs` completes it"; and both `STATE.md` and `buildout-specs.md` still said
  the remaining work included **family-contract ratifications** after PR #65 adopted the last three. This is
  the defect class `check-counts.py` names in its own output: it compares markers and cannot read the
  sentences that quote them.
- `release-notes` gained a first-release mode, so the template no longer assumes a previous version exists
  (DF-1, template 0.1.1).
- The catalog's prose said "core 28-type must-have tier" against its own machine data's 27, in two places.
  Corrected with a dated note; the Tier-1 floor count and two stale gate counts were reconciled at the same
  time.
- `bug-report` research log entry [17] declared its retrieval status as `not retrieved` rather than the
  schema's enum token `not-retrieved`.
- `risk-register` research log entry [33] carried no URL. It is a print book, and the absence is now
  documented as deliberate rather than left looking like an omission.

## [0.1.0] - 2026-07-17

First tagged release. Status `beta`: gate-green and cited to raw sources, with zero fills by anyone
but the author.

### Added

- Six governed bundles across two families, eight files each, `template_version` 0.1.0:
  - `delivery-docs`: `prd`, `user-stories`, `acceptance-criteria`, `release-notes`. Their worked
    examples chain across one feature, so the family reads as one traceable set.
  - `decision-docs`: `rfc` (propose a decision) and `adr` (record it, in MADR v4).
- `tools/check-bundles.py`, the governance gate: nine structural checks per bundle. Eight are pure
  standard library; check G (frontmatter YAML) uses PyYAML and skips honestly when it is absent
  (ADR 0014).
- `tools/check-links.py`, the link gate: every relative link and in-page anchor across every tracked
  Markdown file must resolve, and no tracked file may link into `_local/` (ADR 0013).
- `tools/known-skills.txt`, the pinned skill-ID list that `pairs_with` is validated against.
- CI on every push and pull request, with `main` branch-protected on the gate.
- `templates/methodology.md` (v0.2.3): the authoring process, the citation standard, and the
  per-bundle Definition of Done.
- `atlas/atlas.html`: a self-contained interactive map of all 205 catalog types.
- A six-step consumer quickstart in the README.
- Fourteen decision records at `docs/internal/decisions/` in MADR v4.
- Apache-2.0 license.

### Changed

- Citation standard hardened after a full integrity pass (methodology 0.2.3, section 6): one entry per
  source, honest retrieval status, blocked and paywalled sources labeled in the reference itself, and
  print books labeled as such rather than hidden inside a combined entry carrying a sibling's URL.
- Gate widened from seven checks to nine: citations are now verified in both directions, heading
  nesting compares depth as well as text, the meta is scanned for unfilled placeholders, the history
  must document the version the meta claims, and `pairs_with` / `related_templates` must resolve.
- README claims reconciled against what is true (see Fixed).

### Fixed

- 28 citation defects across the four `delivery-docs` bundles, every one of which had been passing the
  gate green. Included two wrong dates (Gherkin as 2007 rather than 2008; a 2006 Cagan essay dated
  2007), two quotations from sources that could not be read (one paywalled, one unreachable), claims
  attributed to authors who do not make them, and uncited padding.
- README overclaims: deterministic agent selection (no such path exists), a family described as
  "complete" and "verified", a stale four-bundle list, and a `docs/decisions/` path that does not
  exist and is forbidden by the org's scaffolder.
- `tools/check-links.py` did not skip fenced code blocks, so a documented Markdown-link example was
  read as a real link.

### Known gaps

Named here because the release is `beta` and the gaps are the reason:

- **No machine-consumption path.** No metadata schema, so an agent cannot select a bundle
  deterministically.
- **Not installable or listable.** `npx skills add` clones this repo and installs nothing, and
  agentskills.io has no template resource type: both take exactly one unit, the skill, and this repo
  ships no `SKILL.md` (decisions D2 and D3, resolved 2026-07-17).
- **No efficacy evals.** Template quality is argued, not measured.
- **No real usage cycle.** Every filled artifact in the repo is an authored example.
- **The gate cannot check citation truth.** It proves a citation resolves, never that the source
  supports the claim. The 28 defects above were all invisible to it.

[Unreleased]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/v0.3.1...HEAD
[0.3.1]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/product-on-purpose/product-lifecycle-templates/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/product-on-purpose/product-lifecycle-templates/releases/tag/v0.1.0
