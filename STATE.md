# STATE

> **The single source of current truth for this repository.** Update this file in the same commit as any milestone exit, release, or status change.
>
> Plans and briefs are dated projections. Where they disagree with this file, **this file wins**.
>
> This file exists because of audit finding G-01: the implementation plan's progress table said "Not started" for all seven phases while two of them were demonstrably complete, and it went stale within a week of being written. A plan that lies about the tree is worse than no plan. The fix is not "remember to update the plan"; it is to have one short file that is cheap to keep honest and that outranks everything else.
<!-- counts: bundles=27, tier1=25, tier1remaining=2, statebuilt=27, statecandidate=176, stateoutofscope=2, commoncandidates=58, adrs=47, cisteps=31, checkk=96, checkformats=82, checklogs=89, logsgated=21, sourcesgated=826 -->

**Last updated:** 2026-09-11 (**the door was locked, and the guard on it was asleep.** `v0.6.0`'s MCP server told every installer to run `pip install mcp`, which since 2026-07-28 installs a v2 that renamed the class the server imports, so the headline feature of the release could not start for anyone who followed its own instructions. The CI self-test `roadmap.md` called its gate **skipped** the one assertion that would have caught it and exited 0, so **no CI run had ever verified the server starts**. That is [DF-7](#findings-the-library-raised-about-itself-by-using-itself), and the fix is two-sided: pin `mcp<2`, and `--require-sdk`, which turns that skip into a failure. Anyone who installed during `v0.6.0` needs `python3 -m pip install "mcp<2"` and nothing else. **Nine claims in this repository's own documents were found to have aged into being false and were corrected**, including three in this file; the catalog-state counts among them are now facts `check-counts.py` recomputes, so the next drift fails CI rather than ageing quietly. Also landed: a tracked [site plan](docs/internal/site-plan.md) with [ADR 0046](docs/internal/decisions/0046-the-site-is-astro-starlight-under-pattern-s.md), **WP-32's pull queue** ([`pull-queue.md`](docs/reference/pull-queue.md), three labels, three issue forms), and a [Tier-2 spec sheet](docs/internal/tier2-specs.md) whose first entry, `spike-report`, is specified and **not built**.)


---

## Built and true today

| What | State |
|---|---|
| **Bundles** | **Twenty-seven bundles: all 25 templatable Tier-1 types, plus two Tier-2 types**, `rfc` (catalog 48, `must_have: false`, built early as the third `decision-docs` member) and `epic` (catalog 31, built 2026-09-02, the first bundle built under the maintainer-preference order of [ADR 0041](docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md) and admitted to its family by [ADR 0042](docs/internal/decisions/0042-epic-joins-delivery-docs.md)). **The Tier-1 build backlog is empty; Tier 2 is open at the maintainer's discretion and has no queue.** The Tier-1 floor is complete, because `prototype-brief` failed ADR 0030's admission test and does not ship ([ADR 0035](docs/internal/decisions/0035-prototype-brief-fails-the-admission-test.md)); the two numbers are different and are reconciled in [`buildout-specs.md`](docs/internal/buildout-specs.md). **Every family contract is now adopted** ([ADR 0031](docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md) through [ADR 0034](docs/internal/decisions/0034-adopt-communication-docs-family-contract.md)), so no bundle work remains. `design-docs` is never created: both its candidates are out of scope for templating ([ADR 0030](docs/internal/decisions/0030-templating-scope-markdown-documents.md)). Family `process-docs` (**complete**, phase axis): `incident-postmortem`, `sprint-retrospective-notes`. Family `discovery-docs` (**complete at two members**, phase axis): `business-case`, `user-persona`; the provisional third failed the admission test. Family `standing-standards` (**complete**, classification axis, the first family whose members take different values on it): `definition-of-done` (`foundation`), `runbook` (`tool`). Family `strategy-docs` (**complete**, classification axis): `product-vision`, `product-strategy`, `product-roadmap`, `okrs`. Family `qa-docs` (**complete**): `test-plan`, `test-case`, `bug-report`. Family `governance-docs` (**complete**, classification axis): `risk-register`, `raid-log`, `kpi-dashboard`. Family `delivery-docs` (**seven members**): `prd`, `epic`, `user-stories`, `product-backlog`, `sprint-backlog`, `acceptance-criteria`, `release-notes`. Family `decision-docs` (**complete**): `adr`, `rfc`, `sdd`. Eight files each, except `product-vision` and `product-roadmap` at ten and `product-strategy` at nine: each additional format ships one template file ([ADR 0028](docs/internal/decisions/0028-adopt-a-format-axis.md)). Status `beta`, `template_version` 0.1.0. |
| **License** | Apache-2.0, granted at the repo root. Copyright Jonathan Prisant. |
| **Governance gate** | `tools/check-bundles.py`, **eleven checks** (files, dashes, nesting incl. heading level, clean example, citations **in both directions**, meta contract + placeholder scan, frontmatter YAML validity, history-documents-version, pairs_with/related_templates resolution, **meta-schema validation**, and **family-contract conformance on either taxonomy axis**). Check K gates whichever of `phase` or `classification` a family's contract names (ADR 0015), so a standing family is one registry entry, not new check code; because that branch had no live subject until governance-docs landed, it carries a fixture-based self-test ([`tools/test-check-k.py`](tools/test-check-k.py), **96 assertions**, mutation-checked) run in CI. A second self-test, [`tools/test-check-formats.py`](tools/test-check-formats.py) (**82 assertions**), covers the format axis ([ADR 0028](docs/internal/decisions/0028-adopt-a-format-axis.md)) on the same reasoning: two formats with unrelated outlines must pass, an undeclared `_template-*.md` must fail **and** be scanned, and a size word inside a guidance sentence must not invent a variant. A third, [`tools/test-check-i.py`](tools/test-check-i.py) (**42 assertions**), covers check I's `future:` branch, added 2026-09-04 on the third recurrence of a stale forward reference (procedure 9): a `future:` label whose target the library had since built passed the gate forever, and three hand sweeps had corrected the labels without checking them. A fourth, [`tools/test-gen-sections.py`](tools/test-gen-sections.py) (**40 assertions**), covers the AG-1 guidance parser behind [`sections.json`](sections.json), the fourth generated artifact (**241 sections, 181 frontmatter fill sites**, from [`tools/gen-sections.py`](tools/gen-sections.py) with a `--check` mode in CI beside the manifest and atlas). That parser is also the repository's only mechanical reader of the Approach A guidance comments, so a malformed comment now fails a build that would previously have passed; its load-bearing assertions are adversarial because the dangerous failure is a silently wrong section list rather than a crash. A fifth guards the harness itself: [`check-workflow-prompts.py`](tools/check-workflow-prompts.py), added 2026-08-05 after a backtick written as markdown inside a workflow prompt closed its template literal and made the script unloadable, having shipped through a green PR and passed `node --check` with exit 0. Nothing parsed the workflow scripts before it, so a broken harness was invisible until someone ran it; it is the second infrastructural failure of that shape after CRLF, and like that one it is caught by a rule rather than by reading more carefully. Four further CI steps guard documents rather than bundles: [`check-adr-index.py`](tools/check-adr-index.py), [`check-changelog.py`](tools/check-changelog.py), [`check-research-logs.py`](tools/check-research-logs.py) (ADR 0029, with its own 89-assertion self-test, mutation-checked seven ways; gates 21 of 27 research logs, 6 exempt and named, see DF-4) and [`check-counts.py`](tools/check-counts.py) (DF-5, prose counts drift). Nine are pure stdlib; G uses PyYAML ([ADR 0014](docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md)) and J uses PyYAML plus jsonschema ([ADR 0017](docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md)), each SKIPping locally if its dependency is absent. **Runs in CI** on every push and PR; branch protection on `main` requires it to pass before merge. Passing on all **27** bundles (verified by running it 2026-09-04; the "nine" this line carried before 2026-07-25 was stale from the governance-docs build, and the "twenty-three" it carried until 2026-09-04 was stale from `business-case`). **Both self-test counts scale with the live tree** (a landing bundle adds registry and format assertions), so they are re-read from the tools rather than assumed: the pair moved 59/58 to 61/60 when `product-vision` landed, to 63/62 for `product-strategy`, to 65/64 for `product-roadmap`, to 82/68 by `business-case`, to 84/70 by `user-persona`, and to 88/74 by the `standing-standards` pair. They are re-read from the tools on every change, and since 2026-07-28 a marker at the top of this file is compared against the tree by `tools/check-counts.py`. |
| **Machine catalog** | [`manifest.json`](manifest.json) at the repo root: every bundle's selectable fields (`id`, `title`, `summary`, `doc_type`, `phase` or `classification`, `family`, `sizes_available`, `default_size`, `sizing_guidance`, `status`, `tags`, `aliases`) plus a generated `approx_tokens` estimate per size variant, as one structured surface an agent selects a bundle *and a size* from. **Generated** by [`tools/gen-manifest.py`](tools/gen-manifest.py) from the metas and the template files, committed, and kept fresh by CI (`gen-manifest.py --check` fails on drift or a stale README count marker). WP-22 + WP-23, [ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md), [ADR 0019](docs/internal/decisions/0019-selection-metadata-and-approx-tokens.md). |
| **Agent surface** | Two skills (`plt-fill-template`, `plt-grade-doc`), two generated artifacts ([`manifest.json`](manifest.json), [`sections.json`](sections.json)), and an **MCP server** at [`tools/mcp_server.py`](tools/mcp_server.py) declared through [`.mcp.json`](.mcp.json) ([ADR 0045](docs/internal/decisions/0045-the-mcp-server-is-python-and-lives-in-this-repository.md), 2026-09-06). Five tools; all 58 template variants addressable; `validate_fill` and `stamp_and_strip` **call** the existing Python tools rather than reimplementing them, so they cannot disagree with the CLI. Gated by 44 assertions as CI step 29. **Not validated: no agent outside this repository has used it, and no assertion scores its ranking.** Python, not the sketched TypeScript npm package, because the plugin install already clones this repository so there is nothing to embed; the cost, named in the ADR, is that `pm-skills-mcp` and this now differ. |
| **Decision records** | `docs/internal/decisions/`, forty-five ADRs (through 0045) in [MADR v4](https://github.com/adr/madr) format, plus a README index (drift-checked by `tools/check-adr-index.py`). **All accepted.** [0038](docs/internal/decisions/0038-what-the-circularity-signature-obliges.md) sat `proposed` from 2026-08-08 to 2026-08-14, the only record in this library ever to do so, and was accepted with option C (adopt nothing) consciously rejected rather than skipped. Two records were added 2026-08-14: [0039](docs/internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md) **amends grow-by-pull so the maintainer may build any template at discretion**, and [0040](docs/internal/decisions/0040-free-and-open-source-no-paid-tier.md) closes VL-1 as **free and open source with no paid tier**. Added 2026-08-22: [0041](docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md) **makes the maintainer's own preference and need set the build order**, amending 0039's retention of the queue as a priority signal, on the ground that a ranking input which has never been non-zero cannot rank; it names its own cost, that it removes the last structural brake against building content nobody uses. Added 2026-09-03: [0043](docs/internal/decisions/0043-the-usage-gate-becomes-advisory.md) **makes the usage gate advisory**, downgrading 0041's forty-bundle falsifier to a soft reminder, rewording the roadmap's risk-table entry from an instruction to an observation, and ungating M5. **It moves no honesty mechanism**: `beta` until a real usage cycle, never calling a bundle proven on a green gate, and publishing zero real fills as zero all stand. Its stated principle is that a library may grow without evidence but may not claim without evidence, and it names its own cost, that it removes the last structural pressure toward outreach. Added 2026-09-05: [0044](docs/internal/decisions/0044-the-section-schema-is-a-second-generated-artifact.md) **makes `sections.json` a second generated artifact beside the manifest**, following 0018, and makes its parser the first mechanical reader of the Approach A guidance grammar, so a malformed comment now fails a build that would previously have passed. It records three measured departures from the 22-line AG-1 sketch and corrects that sketch's extraction regex, which extracts zero of 353 WHAT fields. The last three family contracts ([ADR 0032](docs/internal/decisions/0032-adopt-standing-standards-family-contract.md), [0033](docs/internal/decisions/0033-adopt-process-docs-family-contract.md), [0034](docs/internal/decisions/0034-adopt-communication-docs-family-contract.md)) ratified 2026-08-05. Matches the org standard used by `agent-config-toolkit` and scaffolded by `jp-init-project`. |
| **Family contracts** | **All nine adopted and registered in check K**, as of 2026-08-05: `delivery-docs`, `decision-docs`, `governance-docs`, `qa-docs`, `strategy-docs`, `discovery-docs` ([ADR 0031](docs/internal/decisions/0031-adopt-discovery-docs-family-contract.md)), `standing-standards` ([0032](docs/internal/decisions/0032-adopt-standing-standards-family-contract.md), a `foundation`/`tool` set), `process-docs` ([0033](docs/internal/decisions/0033-adopt-process-docs-family-contract.md)) and `communication-docs` ([0034](docs/internal/decisions/0034-adopt-communication-docs-family-contract.md)). No bundle is now blocked on a contract. |
| **Layout** | The library lives at `templates/` (flat, by document type), the gate at `tools/`, the atlas at `atlas/`, and the planning, strategy, catalog, roadmap and decision records at `docs/internal/`. Decision HY-2 (scaffold graduation) closed 2026-07-12; the `_local/` split closed 2026-07-14 ([ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)). |
| **Atlas** | 205-type interactive catalog map at `atlas/atlas.html`. |
| **Build harness** | The runbook at [`bundle-pipeline.md`](docs/internal/bundle-pipeline.md) is executable: [`.claude/commands/build-bundle.md`](.claude/commands/build-bundle.md) drives it and [`.claude/workflows/build-bundle.js`](.claude/workflows/build-bundle.js) runs its research and review fan-outs. Review lenses read one brief, [`review-standards.md`](docs/internal/review-standards.md), which states what CI already proves so they do not re-prove it. Two report-only lints (`lint-number-provenance`, `lint-unsourced-confidence`) run at phase 3.5; a source cache (`tools/source-cache.py`, `_local/`) makes a page fetched once per bundle rather than once per agent. |
| **Methodology** | v0.2.3 (`templates/methodology.md`), status draft. Governs authoring. Section 6 now codifies the source conventions (one entry one source; honest retrieval; blocked/paywalled; books). |
| **Master catalog** | [`docs/internal/catalog.md`](docs/internal/catalog.md). 205 types, 27 at Tier 1. Cited by the methodology and by every bundle companion. **Its size calls are hypotheses, not facts** (see EC-2 below). |
| **Audit corpus** | `_local/audit/2026-07-10_fable-audit/` on the maintainer's disk. **Deliberately NOT in git** (see [ADR 0013](docs/internal/decisions/0013-local-split-and-going-public.md)); its two load-bearing artifacts were promoted to [`docs/internal/roadmap.md`](docs/internal/roadmap.md) and [`docs/internal/contracts/delivery-docs.md`](docs/internal/contracts/delivery-docs.md). |

## Nothing broken right now, and the way that changed twice in one day is the point

**This heading said "Nothing broken right now" from 2026-07-23 until 2026-08-08.** On that day the
install was executed for the first time, two defects appeared within minutes, and both were fixed in the
same session. The heading is true again. **The interesting part is not that it is true, it is that it was
false for three weeks while every check in this repository ran green**, because no check asked what a
stranger receives.

**It happened a second time, and the heading was false again from 2026-09-06 to 2026-09-11.** The MCP
server shipped with install advice that installed a version it cannot import, and the CI self-test that
was supposed to catch that skipped the assertion and reported OK. See **DF-7** below. The lesson is not
"add another check" - there *was* a check, it ran on every push, and it was green. The lesson is that a
check which degrades to a skip has no failure mode, and a gate with no failure mode is a report.

**B-1, closed. The install shipped a maintainer-internal skill.** `npx skills add` reported **2 skills**
and installed both, the second being the build harness, whose own description says it is not for library
users. The `skills` CLI scans `.claude/skills` deliberately, its skip list is hardcoded to
`["node_modules", ".git", "dist", "build", "__pycache__"]`, and it reads no ignore file, so a skill
cannot be excluded in place. The old root-`SKILL.md` layout had been suppressing it **by accident**: a
root skill short-circuits the CLI's subdirectory search, and moving the public skill to `skills/` to
satisfy ADR 0036 removed that accident. **Fixed** by making the harness a slash command at
[`.claude/commands/build-bundle.md`](.claude/commands/build-bundle.md), which is invisible both to the
CLI and to the Standard's component discovery, verified against the real repository
([ADR 0037](docs/internal/decisions/0037-keep-the-build-harness-off-the-published-skill-surface.md)).
**The move is the small half.** [`tools/check-export-surface.py`](tools/check-export-surface.py) is the
half that lasts: it fails CI whenever the set of skills an installer would export stops matching what
`library.json` declares. The CLI scans 31 prefixes including `.codex/skills`, so the next leak was always
going to be a different directory rather than a different file.

**B-2, closed. The installed skill could not do what it said.** The install placed **12 KB**, `SKILL.md`
and `README.md`, and none of `manifest.json`, the 27 bundles, or any file the skill's own links point at.
Its step 1 is "Read `manifest.json` at the repository root", and after an install there is no repository.
**This was worse than a missing feature.** An agent told to fill a template it cannot read will usually
produce a fluent document anyway, from the skill's description rather than from the bundle, which is
precisely the artifact this library exists to replace, delivered under this library's name. The eval
measured what that looks like: **1.00 out of 5, and zero of five retrieval probes**. **Fixed** by giving
the skill a precondition that stops rather than improvises, and a fetch path pinned to the release tag
matching its own declared version. The Claude Code plugin channel clones the whole tree and never had
this problem; both routes and how to verify each are now in
[`docs/how-to/installing.md`](docs/how-to/installing.md).

Recently closed:

- **The atlas built flags no longer drift.** The public atlas advertised four built bundles while twelve existed, because the `built` boolean lived in two hand-maintained copies (inline in [`atlas/atlas.html`](atlas/atlas.html) and in [`atlas/catalog-data.json`](atlas/catalog-data.json)), generated by nothing and checked by nothing. Fixed the same way ADR 0018 fixed the manifest: [`tools/gen-atlas.py`](tools/gen-atlas.py) derives `built` from the bundles on disk (via each meta's `catalog_ref`), makes `catalog-data.json` the single source of truth, regenerates the atlas.html island to match it, and `--check` fails CI on drift. Both files now show twelve built. Same defect class as audit finding G-01; closed 2026-07-23.
- **The ADR index no longer drifts.** 0022 and 0023 had landed without an index row in `docs/internal/decisions/README.md`. [`tools/check-adr-index.py`](tools/check-adr-index.py) now fails CI if any `NNNN-*.md` record has no index row (or an index row points at no file).
- **CI runs, and is green.** The gate had never once run (private repo, out of Actions minutes; every run died in 3s with zero steps). The repo went **public** on 2026-07-16, and the first real CI run passed. `main` is **branch-protected**: direct pushes blocked, the `gate` check required (strict), force-pushes and deletions blocked, linear history required.
- **M0 is merged.** PR #2 landed the credibility floor, the ADR bundle, and the `_local/` split. PR #1 was auto-closed by the history rewrite.
- **PB-1 (history exposure) is resolved.** `_local/` was purged from every commit (verified 0 paths in history, and `Not Found` on the remote) before going public, so publishing did not expose the audit corpus or session logs. The 29 files remain on the maintainer's disk, backed up at `E:/tmp/_local-backup-20260714`. ADR 0013 is now `accepted` and **confirmed** (its success condition, CI green on `main`, is met).

The reason this section exists at all: STATE.md is here because of audit finding G-01, *a plan that lies about the tree is worse than no plan*. Between 2026-07-13 and 2026-07-14 it had started doing exactly that (claiming CI passed when it had never run). That is fixed, and the section is kept as the place the next breakage gets recorded first. On 2026-07-22 it earned its keep: the atlas drift was found by checking this file's own claims against the tree, written down here rather than left quietly wrong, and then closed on 2026-07-23 by a generator and a `--check` so it cannot recur silently.

**On 2026-08-08 it earned its keep in the opposite direction, and the lesson is sharper.** The two defects
above were found by *running the install*, not by checking this file against the tree. Every check was
green and every marker matched while the section three headings down claimed the library shipped no
`SKILL.md` and was not installable. **Checking a document against the tree finds drift; it cannot find a
thing that has never been executed.** The install had sat unrun for three weeks, and it took thirty
minutes and produced two real defects and one refuted finding.

## Not built (deliberately visible)

- ~~No version tags. No CHANGELOG.~~ **Shipped 2026-07-17: [v0.1.0](CHANGELOG.md) is tagged**, with a [release note](docs/releases/v0.1.0.md) written by filling this library's own `release-notes` lean template. First dogfood artifact.
- ~~**Distribution: installable as of 2026-08-07, not yet listed.**~~ **Listed 2026-08-08.** [`SKILL.md`](skills/plt-fill-template/SKILL.md) and [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) ship, so the repository is now a valid skill and a valid plugin rather than a clone-only tree; this closes the gap recorded here since 2026-07-17, which was correctly diagnosed as **one missing file, not an architecture problem**. **The marketplace entry exists**: the Product on Purpose registry lives in a separate repository (`product-on-purpose/agent-plugins`) and has listed this library since 2026-08-08, at registry `1.55.0`. **What remains is not the entry but keeping it current.** Registry entries pin a commit SHA, so a listing goes stale silently as this library moves ahead of it, and nothing in either repository fails when it does. Re-pinning is a deliberate cross-repository act and stops for the maintainer. The registry version and plugin count are deliberately not restated here beyond that dated snapshot, because they live in another repository where no check in this one can see them drift (DF-5).
- ~~No family contract adopted.~~ **Five families have adopted contracts, across both taxonomy axes and both axis cardinalities.** [delivery-docs](docs/internal/contracts/delivery-docs.md) (2026-07-20, #24, [ADR 0020](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md)) and [decision-docs](docs/internal/contracts/decision-docs.md) (2026-07-21, [ADR 0022](docs/internal/decisions/0022-adopt-decision-docs-family-contract.md)) gate the `phase` axis; [governance-docs](docs/internal/contracts/governance-docs.md) (2026-07-22, [ADR 0024](docs/internal/decisions/0024-adopt-governance-docs-family-contract.md)) gates the `classification` axis, the first to do so; [qa-docs](docs/internal/contracts/qa-docs.md) (2026-07-25, [ADR 0026](docs/internal/decisions/0026-adopt-qa-docs-family-contract.md)) gates `phase: develop`, the second family to use that value; [strategy-docs](docs/internal/contracts/strategy-docs.md) (2026-07-25, [ADR 0027](docs/internal/decisions/0027-adopt-strategy-docs-family-contract.md)) gates a **set**, `classification` of either `foundation` or `utility`, the first family to need one. All are enforced by gate check K (the family's axis value or value set, status, size shape, and that the contract resolves); all fifteen built bundles conform, and qa-docs went from contract-with-no-members to a complete three-member family in the same week. The registry (`FAMILY_CONTRACTS`) generalized to a fifth family, a second axis, **and a value set**, as one entry each with no new check code. Methodology stays descriptive in all three, not gated ([ADR 0020](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md) lesson).
- ~~No metadata schema, so no machine-consumption path.~~ **Shipped 2026-07-17 onward (#20, #22, #23):** every meta validates against [`tools/meta.schema.json`](tools/meta.schema.json) in CI (check J), and [`manifest.json`](manifest.json) is the machine catalog an agent selects a bundle and size from. Installability (a `SKILL.md`) is the remaining gap, above.
- ~~**No efficacy evals.** Template quality is currently argued, not measured.~~ **Measured 2026-08-08, and the result was VOID twice.** The gap the audit weighted most heavily (finding D-04) is now closed as an *instrument* question and open as a *finding*: the templates score **+0.85** on criteria drawn from their own guide and **-0.03** on criteria drawn from neither, which is the circularity signature. Three bundles of twenty-six. [The result](evals/results/2026-08-08_matched-rerun.md).
- **No real usage cycle. Zero fills by anyone but the author.** Every filled artifact in the repo is an authored example. The catalog's own tier rule gates Tier 2 on "survives one real usage cycle", so by its own standard nothing here has graduated.

## Open by choice, not by oversight

- **The rejected review finding, 2026-07-25 (bug-report).** The four-lens review flagged the guide's
  self-grade rubric threshold ("Under 10 out of 16 and the report will come back with questions instead of a
  fix") as an unsourced predictive claim. **Rejected, with a reason:** it is a self-grading heuristic in an
  operator card, not a research claim, and **all three qa-docs guides plus the earlier families use the same
  construction** ("will not survive contact with the release", "will not survive its first re-run"). Changing
  one member would make the family inconsistent for no gain in honesty. Recorded here rather than silently
  dismissed, because it is a fair observation about house style: if the maintainer wants these thresholds
  reworded as explicit heuristics, that is a **family-wide edit across every guide**, not a bug-report fix.
  This is the first review finding in the qa-docs family that was not applied.

- **The rubric threshold, re-raised independently 2026-07-28 (product-roadmap).** The Codex adversarial pass
  flagged the guide's "Under 12 out of 18 and this roadmap will be read as a commitment you did not make" as
  an unvalidated predictive claim sitting a few lines below the bundle's own statement that no study links
  any roadmap practice to outcomes. **This is the same finding rejected on 2026-07-25 for `bug-report`**, and
  it is rejected again on the same recorded ground: the construction is house style across every guide in the
  library, and changing one member makes the family inconsistent for no gain in honesty. **Two independent
  reviewers now having raised it is the point worth recording.** It has stopped being one reviewer's taste.
  The family-wide edit, rewording every guide's threshold as an explicit heuristic rather than a prediction,
  is a real piece of work that should be scheduled rather than re-litigated per bundle. What *was* fixed here
  is the narrower part of the same finding: the rubric graded `go` and `themes` against a Dependencies row and
  a Review Trigger row that neither format ships, so choosing a non-default format cost four points for
  sections that do not exist. Those rows are now scoped to `now-next-later`.

- **The format-admission rule has a third criterion that ADR 0028 does not contain.** Found by the Codex pass
  on `product-roadmap`. [ADR 0028 (the format-axis rule)](docs/internal/decisions/0028-adopt-a-format-axis.md)
  admits a format that is **structurally distinct and in circulation with a named source**. Two of
  `product-roadmap`'s six rejections rest on a further test, *does the artifact's own author present it as a
  roadmap*, and that test has never been applied backwards: `product-vision` ships a PR/FAQ admitted under the
  two written criteria, and Amazon does not present the PR/FAQ as a product vision. So either the rule gains a
  third criterion explicitly or `product-roadmap` is stricter than its siblings. **Recorded, not resolved**,
  and stated in the bundle's own companion section 4 rather than left implicit. It belongs to the
  `default_format` backfill (decision D-E in [`buildout-specs.md`](docs/internal/buildout-specs.md)), which
  already needs its own ADR, because settling a 27-type rule inside a bundle PR is the mistake ADR 0028 was
  careful not to make.

- **B-08, the `_working/` folder.** `templates/_working/` still holds the A/B/C guidance-style prototypes, even though its own README line 6 orders its deletion once the decision was made, and the decision *was* made (Approach A, see [`docs/internal/decisions/0006-guidance-style-approach-a.md`](docs/internal/decisions/0006-guidance-style-approach-a.md)). The maintainer chose on 2026-07-12 to keep it. Recorded here so it reads as a decision rather than a miss.

- **The sidecar-asset scope question, left open on purpose (2026-08-14).** Whether a bundle may ship a
  non-Markdown companion file (a `.csv` fixture, a `.json` schema) is **not decided**, and the word
  `sidecar` appears nowhere in `docs/`. [ADR 0030](docs/internal/decisions/0030-templating-scope-markdown-documents.md)
  settles what this library **templates**, not what a bundle may **carry**. It was proposed as a
  prerequisite by the 2026-08-05 research and is deliberately not taken, because **deciding it now would be
  writing a rule with no subject**, which is the mistake [ADR 0028](docs/internal/decisions/0028-adopt-a-format-axis.md)
  was careful to avoid by adopting the format axis narrowly. It reopens the moment any bundle needs a
  fixture.

- **The family-wide rubric-threshold rewording, now scheduled rather than re-litigated (2026-08-14).** The
  two entries above record the same finding raised by two independent reviewers, and it was raised a third
  time in review since. **It is now scheduled as one family-wide edit** across every guide, to run after
  the [decision procedure 12](docs/internal/decision-procedures.md) work settles, because
  [ADR 0038](docs/internal/decisions/0038-what-the-circularity-signature-obliges.md) notes that adding
  rubric rows makes this open question bigger rather than smaller. **The rule from here: it is not
  re-argued per bundle.** A reviewer raising it again gets pointed at this line.

- **The 2026-08-05 agentic-era research, parked with its errors named (2026-08-14).** A 58 KB strategy
  document at `_local/audit/2026-08-05_ai-skills_claude-fable-research.md` on the maintainer's disk,
  referenced by nothing in this repository. **It is parked rather than promoted, and rather than deleted.**
  Three of its load-bearing premises are false because it was written against a stale snapshot of this
  repository: it describes 15 bundles and 27 decision records against today's 26 and 40, it recommends
  shipping a `SKILL.md` that shipped 2026-08-07, and its section 9 asserts that the format axis
  "is NOT adopted" when [ADR 0028](docs/internal/decisions/0028-adopt-a-format-axis.md) had been adopted
  **ten days before the research was written**. The research underneath is good and the sourcing is real;
  what failed is that it read `STATE.md` as a snapshot rather than reading the tree. **Its single best idea
  is already reachable** through decision procedure 12, which is the test any AI-era section would face.

## Findings the library raised about itself, by using itself

**DF-7, 2026-09-11. The CI self-test that `roadmap.md` called the MCP server's gate had never once
verified that the server starts.** The workflow installed `mcp` unpinned. The SDK released v2 on
**2026-07-28**, renaming `FastMCP` to `MCPServer`, which is the class `tools/mcp_server.py` imports - so
every CI run from the day WP-51 shipped (2026-09-06) resolved a 2.x the server cannot import. The suite
handled that exactly as designed: `test-mcp-server.py` **skipped** its one SDK-dependent assertion,
printed `OK 43 assertion(s) passed`, and exited 0. The run on 2026-09-08 was green on those terms.

**The skip was correct behaviour and that is the whole finding.** Skipping loudly when a dependency is
absent is right on a contributor's machine and wrong in CI, where a missing dependency IS the failure.
Nothing distinguished the two contexts, so the gate quietly shrank by one assertion - the only assertion
that touched the SDK - and kept reporting OK. **A suite that can shrink without failing does not have 44
assertions; it has 43 and a promise.** Fixed two ways, because the pin alone would only fix today's
break: `mcp<2` in the workflow, and `--require-sdk`, which turns that skip into a non-zero exit. Both
were mutation-checked - the suite was run against `mcp 2.2.0` in a throwaway venv and confirmed to fail.

This is the **third** appearance of one shape: DF-5 below is the same defect in prose counts, the install
findings are the same defect in what a stranger receives, and the v0.6.0 release note found it in
`validate-fill.py`. **A check that returns SOMETHING is not one that returns the RIGHT thing** - and the
corollary this finding adds is that *reporting* is not *enforcing*. The user-facing half shipped too:
`pip install mcp`, the command the error message and `installing.md` both gave, installed the broken
major version for the whole of `v0.6.0`.

**DF-1, the first dogfood finding, 2026-07-17. The lean `release-notes` template has no first-release
mode.** Found the only way this class of defect ever gets found: by filling the template for real, to
write [this repository's own v0.1.0 release note](docs/releases/v0.1.0.md).

"Improved" and "Fixed" are defined relative to a previous release, and a `0.1.0` has none. Worse, the
template's own fill rule ("if a section does not apply, write 'None in this release'") would produce a
first release note declaring that nothing was improved and nothing was fixed, which is false in
spirit: plenty was, it simply was never *released* before. The bundle already cites the source that
solves this (Keep a Changelog treats a first release as entirely "Added") and failed to carry the
guidance across.

**FIXED 2026-07-17 in `release-notes` 0.1.1**, once v0.1.0 was tagged and the fix could no longer
contradict the artifact that produced it. Both variants and the guide now carry an explicit
first-release rule: delete the comparative sections rather than filling them, stated as an override
(it contradicts the rule directly above it), with the reasoning given and the escape hatch named
(real users on an untagged `main` did experience change, so the sections may carry that if the
Summary says what "improved" is measured against). Recorded in
[`release-notes_history.md`](templates/release-notes/release-notes_history.md).

**This is the library's first template change driven by evidence from use rather than from review**,
which is the entire argument for the usage loop, demonstrated on a sample size of one.

The dogfood is worth more than the release. Six bundles have been argued to be good; this is the first
evidence of one meeting a real task, and it took exactly one use to find a real gap. That is the case
for the usage loop (roadmap M3) in one data point.

**DF-2, 2026-07-25. The research log has three formats, and the gate has never checked any of them.**
**CLOSED 2026-07-28 for the ten logs the check covers, after the finding itself was corrected.**
Found by auditing whether every source in every log carries its annotation. Of the fifteen bundles in the
tree on that date, six use numbered prose entries; six use a numbered markdown table; three
(`product-backlog`, `sdd`, `sprint-backlog`) group sources under `###` subsections with no per-source
retrieval status a checker can see. The honest-retrieval standard
([`bundle-pipeline.md`](docs/internal/bundle-pipeline.md) phase 1) requires `title, author_or_org, url, tier,
retrieval_status, supports` for each source, but that contract binds **the research workflow's JSON schema**,
not the markdown log the workflow produces. Nothing carried it across, and fifteen bundles shipped without
it being verified once.

Two real defects surfaced and are fixed: `bug-report` [17] wrote its retrieval status as `not retrieved`
rather than the enum token `not-retrieved`, and `risk-register` [33] (a print book) carried no URL, now
documented as a deliberate absence rather than left looking like an omission.

**The audit's own near-miss is the more useful finding.** The first pass reported **76 defects**; the real
number is **2**. The checker demanded `Contested/time-bound` and `Quotable` on every entry, and the documented
standard makes both **optional**. Trusting it would have meant editing 74 entries that were already correct,
in a diff that would have looked like diligence. Two rules earned: **verify the rule before enforcing it**,
and **a check that finds no subject must say so rather than pass** - the nine table-format logs reported
"complete" when they meant "nothing to check".

**DECIDED 2026-07-27, [ADR 0029](docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md)
(gate the research log's contract, not its layout).** The framing that settled it: "three layouts" was the
symptom, not the defect. Two of the three carry every required field and differ only in presentation; the
real gap is that **three bundles record no per-source retrieval status in any readable form**, so for those
the central claim is not merely unverified but unverifiable. So the gate enforces the **contract**
(number, title, author, url, tier, retrieval status, `Supports:`) and accepts any numbered layout, exactly
as `sizes_available` has accepted two vocabularies since [ADR 0010](docs/internal/decisions/0010-meta-declares-size-contract.md).
`Quotable:` and `Contested/time-bound:` stay optional, because the written standard says so. Cost: convert
**three** logs (`product-backlog`, `sdd`, `sprint-backlog`), not nine or ten. A print-source exemption is
documented for unfetchable books, taken from the `risk-register` [33] case.

**BUILT 2026-07-28, and building it proved the finding above wrong.**
[`tools/check-research-logs.py`](tools/check-research-logs.py) runs in CI with 48 mutation-checked fixture
assertions ([`tools/test-check-research-logs.py`](tools/test-check-research-logs.py)). Writing it required
reading every source in the tree, and **the three bundles this finding accused of carrying no retrieval
status carry it in full.** They use a **third numbered layout** (`n. **[Tier N] Author. "Title."** url -
**status** - Supports: ...`) under `###` dimension headings, and each of their 73 sources has the same
three-token enum the prose logs use. All three open with a retrieval-status legend. **The audit matched two
regexes, found neither, and wrote down the absence as a fact** - against the rule this same section had
already earned: an unverified absence is a to-do, not a finding. That makes three times this class has
appeared here, and the first two were caught by review rather than by measurement.

Measured across all **430** sources on 2026-07-28: prose 7 logs / 271 sources, list 3 logs / 73 sources,
table 6 logs / 86 sources. Prose and list carry url, tier, enum status and `Supports:` throughout, minus six
entries that said `Corroborates` or `Additional support:` and one cross-reference missing its URL, all now
relabelled without changing a claim. **The table logs carry neither a URL nor an enum token, for any
source.** So the gap was the opposite of the record: no conversions were needed, and the six logs the
finding never mentioned are the ones that fail. See **DF-4**.

The check gates 12 of 18 logs and 472 of 558 sources, accepts all three numbered layouts, fails a log it
cannot parse rather than passing it quietly, and prints both its exemptions and its own limits every run.

**DF-5, 2026-07-28. The counts in this file drift every single time a bundle lands, and this is the fourth
occurrence.** Found by an adversarial review of the `product-strategy` change, which caught this file still
reporting sixteen bundles, 61 and 60 self-test assertions, and 10 of 16 gated research logs, hours after all
five numbers had changed. The same class hit the session log, `product-vision`, and the two self-test counts
before it. **The pattern is exact: every count this repo GENERATES is fresh, and every count it retypes into
prose is stale.** The README's bundle count is the counter-example that proves it, because it carries a
`<!-- bundle-count: N -->` marker that `gen-manifest.py --check` compares against reality, and it has never
drifted since.

**CLOSED 2026-07-28 by [`tools/check-counts.py`](tools/check-counts.py)**, after a fifth occurrence: a
README badge had been sitting at 11 of 27 Tier-1 types while the real figure reached 17, and the freshness
banners in [`roadmap.md`](docs/internal/roadmap.md) and [`plan.md`](docs/internal/plan.md), both added on
2026-07-26 specifically to manage staleness, had themselves gone stale on their decision-record count within
two days.

Each participating document now carries a marker listing the repository facts it quotes:
`<!-- counts: bundles=25, tier1=24, adrs=35 -->`. The check recomputes each from the tree and fails on
disagreement. **It says plainly what it cannot do**: it compares markers, not prose, so a green run means no
number has changed since an author last confirmed the text, never that the text is right. Its failure
message says "re-read the document", not "edit the marker", because editing the marker alone would recreate
the defect with extra steps.

Five documents are marked: STATE.md, README.md, roadmap.md, plan.md and buildout-specs.md.

**SIXTH OCCURRENCE, 2026-07-28, found by the `product-roadmap` review, and it is the most instructive one.**
The change that built `check-counts.py` listed the README badge among the things it fixed. It fixed the
**Tier-1 floor** badge and left three other numbers stale **in the same file**: the bundles badge said
**12** against 18, the families badge said **3** against 5, and the summary table said **25 ADRs** against 29.
The Tier-1 badge's own `alt` text still read "11 of 27" while the image it labelled read 17. STATE.md
meanwhile said "twenty-seven ADRs (through 0027)". **Every one of these sat 115 lines away from a marker the
check reads and passes.** CI was green throughout, correctly: the check compares markers, says so on every
run, and this is exactly the blind spot it declares. The lesson is not that the check is weak. It is that
**a gate that names its limit still needs a reader to cover that limit**, and the review layer is where that
happens. Also corrected: the bundle's own format arithmetic said "eight candidates, five rejected" while
naming **six** distinct rejections, an error that originated in the research fan-out and propagated
unchallenged into the research log, the companion, the history file, STATE.md and the commit message. Three
plus six is nine.

**And one channel the check cannot reach at all:** the session log's `=== STATE ===` block described the
unmerged branch tip as though it were `main`, wrong on four of five figures. Session logs live in gitignored
`_local/`, outside the check's universe, and that block is what the next session reads first.

**SEVENTH OCCURRENCE, 2026-08-06, and it is the same sentence as the sixth.** Found by reviewing the previous
session's log against the tree rather than by any check. The Decision records row said **"thirty-four ADRs
(through 0034)"** while thirty-five existed. That is the sentence the sixth occurrence above records as having
read "twenty-seven ADRs (through 0027)": same file, same row, corrected once, stale again eight records later.
The Bundles row separately said **"the remaining work is seven bundles and no contracts"** while contradicting
itself three sentences earlier with the correct figure of three.

**Both mechanisms are worth recording, because the first is the one this section's own text warns against.**
The paragraph above states that the check's failure message says "re-read the document", not "edit the
marker", *because editing the marker alone would recreate the defect with extra steps*. PR #71 (the
`prototype-brief` admission record, [ADR 0035](docs/internal/decisions/0035-prototype-brief-fails-the-admission-test.md))
bumped this file's marker from `adrs=34` to `adrs=35` and left the sentence fourteen lines below it reading
thirty-four. CI was green, correctly. The Bundles row failed differently and worse: PR #73 (the
`standing-standards` pair) **rewrote that entire row**, got the new backlog right in one sentence, and left
the superseded figure standing three sentences later inside the text it was editing.

**A sweep of all five marked documents on 2026-08-06 found no other live drift.** README's "six bundles" is
delivery-docs' real membership and `buildout-specs.md` agrees with itself in both its table and its prose. So
the defect is not spreading. It is recurring in one file, in the two rows every bundle PR touches, which is a
narrower and more tractable shape than the first six occurrences suggested. The second mechanism is also the
one no marker check could ever reach: **a row that disagrees with itself**, where both figures are prose and
neither is a marker, so there is nothing for a checker to compare.

**DF-6, 2026-07-30. Sixteen of nineteen worked examples are their own template's guidance text relocated,
and the convention adopted to prevent it does not work.** This is the largest defect the library has found in
itself.

A template's guidance comments carry `GOOD:` and `WEAK:` snippets illustrating each section. The worked
example is supposed to demonstrate the template **independently**. When the example is the hint reworded, a
reader who has read the comments learns nothing from the example, and the bundle ships two copies of one
idea while appearing to ship two artifacts.

**It recurred four times, and the third and fourth are the ones that matter.** `product-strategy` had it in
seven of eight sections. The fix adopted then was a convention: *use a different scenario in the guidance
comments than in the worked example*. `product-roadmap` then shipped it in three of eight sections, one
sentence verbatim. `okrs` then shipped it **with the different scenario actually in place** - a hiring
platform in the comments, Acme Analytics in the example - because the reuse lives in the **sentence
skeleton**, not the subject. Every noun was swapped and the skeleton survived intact, including a literal
reused number. **Scenario separation is necessary and not sufficient, and no amount of author discipline
fixes a defect the author cannot see themselves committing.**

**[`tools/check-example-independence.py`](tools/check-example-independence.py) now gates it**, and it runs in
CI. It extracts every GOOD and WEAK snippet from a bundle's templates, extracts the example's prose, and
reports shared word runs; eight or more informative words is a copied passage.

**On first run it failed 16 of 19 bundles, which is the finding.** All 16 were triaged by reading them
against their raw comment blocks, and **there were zero false positives.** The check was also found to
**under-report**: at least two known verbatim copies escape because an inserted article breaks the run below
threshold. No document-type exemption was warranted; the Connextra story skeleton, Given/When/Then, and MADR
headings all fall below the informative-word floor, and every surviving run carries invented proper nouns,
figures or IDs. The worst cases are total: `acceptance-criteria` copied five of its six guidance sections
verbatim including a whole Given/When/Then scenario, `adr`'s example title is character-identical to its
hint, and `product-vision`'s single example is patched together from the hints of all four of its formats.

**The sixteen are grandfathered at a measured ceiling that may only shrink**, in the pattern
`check-research-logs.py` established: named, with a reason, printed loudly on every run, and never a pass.
132 copied passages are outstanding. A bundle not on the list fails on its first copied passage, and a listed
bundle fails if its count rises. The mechanism deletes itself when the map empties.

**Two bugs in the check itself were found by the same triage and fixed before it shipped**: n-grams were
being built across the join between two snippets, matching text no hint contained (67 ghost runs), and one
copied passage was reported as many overlapping windows because suppression compared strings rather than
positions. Fixing both dropped the reported lines from 159 to 132 **without changing which bundles fail**.

**DF-4, 2026-07-28. Six research logs cannot satisfy the retrieval contract, and it took writing the check
to find out.** `acceptance-criteria` (10 sources), `adr` (22), `prd` (12), `release-notes` (10), `rfc` (20)
and `user-stories` (12) use the numbered-table layout. **Not one of those 86 sources carries a URL**, and no
retrieval cell carries an enum token; the column holds prose such as "Fetched and verified 2026-07-16",
"URL confirmed live 2026-07-16; body not re-verified claim by claim" and "BLOCKED. HTTP 403 to automated
fetch". The prose is often *more* informative than a token. It is also unparseable, and without a URL the
source is not traceable at all: a reader cannot get from the log to the thing it cites.

These six are the library's oldest bundles, and they predate the honest-retrieval conventions that
methodology 0.2.3 codified after the WP-10 citation pass. That is the same shape as DF-3: the parts of the
tree written before a rule existed are the parts that do not follow it.

**Exempted by name in [`tools/check-research-logs.py`](tools/check-research-logs.py), with the measured
reason and the date, and printed on every run.** Not weakened away: the contract stays whole and these six
are visibly outside it. **Closing DF-4 means re-fetching 85 sources**, because a URL cannot be invented and
a retrieval status cannot be claimed for a fetch nobody performed. That is a research job of roughly one
bundle's cost, and it is deliberately not being done in the same change that ships the gate.

**DF-3, 2026-07-26. The documents this repo gates for freshness stayed fresh; the ones it does not gate
drifted.** Found by checking whether the roadmap and release plan had been updated with the format-axis
decision. They had not, and neither had anything else: `CHANGELOG.md`'s `[Unreleased]` section was **empty**
across **28 commits**, nine bundles, five family contracts and fourteen decision records since `v0.1.0`.

This is close to a controlled experiment, inside one repository, with one author and one period. **Gated for
freshness:** `manifest.json`, the atlas, the ADR index, all three fresh, and each check written only after
the corresponding drift had already been found in the tree. **Not gated:** `CHANGELOG.md` (stale by 14
decision records), `roadmap.md` and `plan.md` (stale by 8 each). The only variable is enforcement.

The irony is exact: this file's own charter says the fix for a plan that lies about the tree "is not
*remember to update the plan*; it is to have one short file that is cheap to keep honest." The repository
proved itself right and then did not apply the lesson to its changelog.

**FIXED 2026-07-26.** `[Unreleased]` is backfilled, and [`tools/check-changelog.py`](tools/check-changelog.py)
now fails CI if any post-0.1.0 decision record is missing from it. The check found a real omission on its
first run: **ADR 0021 was absent from the backfill I had just written by hand.** It is deliberately shallow,
proving only that nothing is missing rather than that any entry is good, and it prints that limitation on
every run.

## Findings the library raised about its own ecosystem

Building a bundle turns out to be an audit of everything the bundle touches. The ADR bundle
(2026-07-14) surfaced two defects outside this repo; the RFC bundle (2026-07-16) surfaced a third.
All are **recorded, not silently patched**, because a template library that quietly edits its
neighbors is worse than one that reports.

| # | Finding | Where it lives | Status |
|---|---|---|---|
| **EC-1** | **`develop-adr` (pm-skills) ships a Nygard-format ADR template**, diverging from the MADR v4 convention the org standardized on for its own decision records (mandated by `jp-init-project` SKILL.md lines 8 and 98, adopted here by [ADR 0011](docs/internal/decisions/0011-madr-v4-at-docs-internal-decisions.md), and verified in use by `agent-config-toolkit`). An agent invoking that skill inside an org repo produces records in the wrong format. This bundle follows MADR and ships a Nygard-to-MADR mapping table in `adr_guide.md` so the two interoperate. **Reported to pm-skills 2026-07-16** as a durable audit ([PR #238](https://github.com/product-on-purpose/pm-skills/pull/238), `docs/internal/audit/2026-07-16_adr-format-divergence.md`): reported, not patched, because the skill's output format is a genuine decision (it is a public product; Nygard is the best-known ADR format; the MADR mandate governs the org's *own* records). **Two corrections, 2026-07-16.** (1) This row previously claimed MADR v4 was "in use by `agent-config-toolkit` and `thinking-framework-skills`". The second half was false: `thinking-framework-skills` has no tracked `docs/internal/decisions/` and no MADR reference at all. The mandate is real; adoption is partial. (2) The path given was `.claude/skills/...`, which is gitignored in pm-skills; the tracked source is `skills/develop-adr/references/TEMPLATE.md`. Re-checking also surfaced a second locus the original finding missed: pm-skills' `docs/internal/audit/README.md` plans "e.g., Nygard format ADRs" for a `docs/internal/decisions/` folder that does not exist yet. | `pm-skills`, `skills/develop-adr/references/TEMPLATE.md` | Reported 2026-07-16; decision open, for the pm-skills maintainer |
| **EC-2** | ~~Master catalog entry 64 (ADR) classifies the type as single-size ("S only").~~ **RESOLVED 2026-07-16.** MADR ships a minimal and a full template, so the type earns two weights. The catalog entry is corrected (now `S/L`, with a dated correction note), and a catalog-header note now states that all size calls are hypotheses. The bundle ships `lean` + `full`. | [`docs/internal/catalog.md`](docs/internal/catalog.md), entry 64 | **Resolved** |
| **EC-4** | **pm-skills covers no testing or QA work at all.** Verified 2026-07-25 by enumerating every tracked skill (`git ls-files 'skills/*/SKILL.md'`, 68 skills): none produces a test plan, a test case, or a bug report, and none carries a QA-facing job. The two near-misses are not counter-examples: `tool-design-sprint-test-and-score` is design-sprint usability testing, and `deliver-edge-cases` is a specification artifact, though its own description does name "during QA planning" and "when preparing QA test plans" as uses, which makes it the one honest `pairs_with` a `qa-docs` member can claim (now pinned in `tools/known-skills.txt`). This is a whole-stage gap, not a missing skill: `atlas/catalog-data.json` carries **13** types at `stage: testing` (3 Tier-1, 10 Tier-2) and the org's skill library addresses none of them. Same class as EC-3, one level up. Found while adopting the qa-docs contract ([ADR 0026](docs/internal/decisions/0026-adopt-qa-docs-family-contract.md)). | `pm-skills` (absent skills) | Open, for the pm-skills maintainer |
| **EC-3** | **No `develop-rfc` skill exists in pm-skills.** The org ships `develop-adr` (a skill for the decision *record*) but nothing that generates an RFC (the *proposal* that precedes it), even though the RFC comes first in the sequence. An agent can be told to record a decision but not to propose one. The RFC bundle's `pairs_with` is therefore empty and the template is filled by hand. Not a defect in existing code, a gap in coverage. | `pm-skills` (absent skill) | Open, for the pm-skills maintainer |

Worth noting what EC-2 implies: **the catalog's size calls are hypotheses, not facts.** One of the
27 Tier-1 entries has now been checked against primary evidence and did not survive. The other 26
have not been checked. Expect more corrections as bundles get built, and treat the catalog's
`size_variant` column as a starting guess rather than a specification. The catalog now says this
about itself, in a header note.

## Gate coverage, stated honestly

The gate automates roughly **half** the methodology's Definition of Done (audit finding D-01). Seven checks run; the research-tracing, guidance-comment-structure, companion-skeleton, guide-structure, and history-content clauses have **zero** automation and are human-verified. Gate hardening is roadmap WP-11 in milestone M1, now partly done (see below).

One honest qualifier: the gate covers about half the DoD. Since M0 it **does** run in CI on every push and PR, and branch protection requires it to pass before merge, so for the half it covers, "enforceable, not aspirational" is finally true rather than aspirational.

**The YAML gap is closed (2026-07-16).** The ADR bundle had shipped with invalid YAML in both template frontmatters (`decision-makers: [{{decision_makers}}]` parses as a flow mapping with an unhashable key) and **the gate passed it green**, because it read `sizes_available` with a regex and never parsed YAML as YAML. Check **G (frontmatter YAML)** now closes that: the meta and every template/example frontmatter must parse, which forces placeholders to be quoted. This needed a YAML parser, which the stdlib lacks, so [ADR 0014](docs/internal/decisions/0014-gate-may-use-pyyaml-for-frontmatter-validity.md) grants the gate one dependency (PyYAML) for this one check; the other six stay pure stdlib and G SKIPs (honestly, not as a pass) if PyYAML is absent locally. CI installs it, so G is enforced. Verified by reintroducing the original bug and watching G fail.

**What remains of WP-11 is the hard half: citation-tracing.** Check E confirms a companion's inline citations *resolve* to anchors; nothing checks that the anchored source *supports the claim*. That is the failure mode that produced ~15 defects in the ADR bundle across three review rounds, it is still entirely human-verified, and it may not be fully mechanizable. Tracked as the open remainder of WP-11.

**WP-10 (citation integrity pass) is done, 2026-07-16, and it is the strongest evidence yet for the paragraph above.** All four delivery-docs bundles were verified against raw sources; every one had been passing the gate green the whole time. **28 defects across four bundles**, including three the gate is structurally incapable of seeing:

- **Two factual errors.** Gherkin is 2008 (Cucumber, Hellesoy), not 2007, and the word "Gherkin" appears nowhere in the Dan North article it was cited to. Cagan's "Revisiting the Product Spec" is 2006, not 2007, in a sentence whose whole point was how long he has held the position.
- **Two unverifiable quotations**, both now de-quoted: one from a paywalled post ("This post is for paid subscribers"), one from a domain that times out. Neither could ever have been checked.
- **Claims attributed to authors who do not make them.** Bill Wake does not say stories are "sized to fit inside one iteration" (he says "at most a few person-weeks"); Ranorex was cited five times and supports two.
- **Uncited padding the gate cannot catch**, exactly as predicted: check E fails an inline citation with no anchor but **never an anchor with no citation**. PRD refs 8 and 12 had zero citations each.

**The audit itself was wrong once.** WP-10 instructed "Keep a Changelog corrected to 1.1.2 with root URL". The spec site serves **1.1.0** as canonical and redirects `/en/1.1.1/` and `/en/1.1.2/` back to it; the repo tags the audit likely read are site releases, not spec versions. The existing citation was already correct. **Following the roadmap on faith would have introduced the defect class WP-10 exists to remove.** The roadmap row was withdrawn and corrected instead. A finding is a claim, and claims get checked.

**The durable fix shipped with it:** methodology 0.2.3 codifies four source conventions ([§6.1](templates/methodology.md#61-one-entry-one-source-no-combined-entries) one entry one source, [§6.2](templates/methodology.md#62-retrieval-status-must-be-honest) honest retrieval, [§6.3](templates/methodology.md#63-blocked-and-paywalled-sources) blocked/paywalled, [§6.4](templates/methodology.md#64-books-and-pre-web-sources-no-url) books), and the Definition of Done gained five checks so they are conditions of shipping rather than advice. **Combined entries were the single largest root cause**: they destroy traceability, launder sources with no URL behind a sibling's link, and attach claims to sources that do not make them.

## Next milestone

**M1 is complete (2026-07-17): [v0.1.0](CHANGELOG.md) is tagged.** All five work packages landed; the
table below is the record. Two open questions that gated M2 were also closed the same day: TX-1 (the
second taxonomy axis, [ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md))
and TX-2 (the catalog `phase` -> `stage` rename). Plus DF-1, the first dogfood finding, found by use and
fixed in `release-notes` 0.1.1.

**M2 is complete (2026-08-07), and its exit was larger than this section used to describe.** Its first items landed 2026-07-17, with WP-20's graduation confirmed already done. **The Tier-1 floor build-out ([ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md)) was adopted after the roadmap was written and folded into this milestone**, so M2 spanned four releases (`v0.2.0` through `v0.3.1`) rather than the single `v0.2.0` the roadmap names, and ended with the library at **Gold (advanced)** on the Advanced Skill Library Standard, measured in CI:

| WP | What | State |
|---|---|---|
| **WP-20** | HY-2 decision + graduation | **Done (2026-07-12, [ADR 0009](docs/internal/decisions/0009-scaffold-graduation-flat-templates.md)).** The flat `templates/` scaffold graduated before M2, so WP-22's machine surfaces are built against final paths, satisfying the roadmap's ordering note. Confirmed 2026-07-17; the only unmet deliverable was a redirect note in the gitignored `_local/`, which is not a tracked artifact. |
| **WP-21** | Metadata schema (`tools/meta.schema.json`; gate check J validates every meta against it) | **Done 2026-07-17 (#20).** The schema encodes `phase` XOR `classification` (ADR 0015) and codifies the 18 fields the six metas carry; check J enforces it in CI, adversarially tested against a 37-case battery hardened by an independent red-team. [ADR 0016](docs/internal/decisions/0016-adopt-machine-checkable-metadata-schema.md) (the schema), [ADR 0017](docs/internal/decisions/0017-gate-may-use-jsonschema-for-meta-validation.md) (the jsonschema dependency). The worked RFC example [RFC-0001](templates/rfc/rfc_example.md) *was* this proposal and is now accepted, written from into ADR 0016. |
| **WP-22** | Machine catalog (`manifest.json`; `tools/gen-manifest.py`; freshness check) | **Done 2026-07-17 (#22).** `manifest.json` is generated from the metas and committed; `gen-manifest.py --check` fails CI on drift or a stale README count marker (audit C-03). Delivers RFC-0001's second artifact. [ADR 0018](docs/internal/decisions/0018-machine-catalog-generated-manifest.md). |
| **WP-23** | Selection metadata (`default_size`, `sizing_guidance`, `approx_tokens`) | **Done 2026-07-18 (#23).** Authored `default_size` (checked against `sizes_available` by check F) and `sizing_guidance` in every meta; a generated `approx_tokens` estimate per variant in the manifest (stdlib chars/4 heuristic, no tokenizer dependency). [ADR 0019](docs/internal/decisions/0019-selection-metadata-and-approx-tokens.md). |
| **WP-24** | Family contract (`delivery-docs`) + gate check | **Done 2026-07-20 (#24).** The `delivery-docs` contract ([docs/internal/contracts/delivery-docs.md](docs/internal/contracts/delivery-docs.md)) is adopted and enforced by check K (phase/status/size shape + contract resolves). Check K's first run found the contract's `methodology: generic` rule contradicted three members' honest values, so methodology was made descriptive, not gated ([ADR 0020](docs/internal/decisions/0020-adopt-delivery-docs-family-contract.md)). Methodology-specific *packs* (Scrum/XP/SAFe collections) reserved as a Tier-2 future. |
| **WP-25** | Fill tooling (`tools/strip-template.py`; `filled_by`/`fill_method` fields) | **Was the one M2 item quietly dropped rather than delivered; shipped late, under another number.** The sentence that stood here until 2026-09-11 said "`tools/strip-template.py` does not exist", which was true when verified on 2026-08-14 and **false from 2026-09-05**, when WP-50 shipped it alongside `validate-fill.py` in #125. The roadmap's WP-50 row recorded that; this row did not, so the two documents disagreed for five weeks. What the 2026-08-14 check found is still worth keeping: `filled_by` appeared in **zero** files under `templates/`, and still does, because it is stamped onto a *filled copy* and never onto a template. The skill `plt-fill-template` covers the fill path a user actually walks, so the gap is narrower than it looks, but the deliverable named here was never built and nothing recorded that. Its spec survives as the untracked `spec_lp1-use-template-flow.md` and it is roadmap **WP-50**, in M5. |
| **WP-26** | Freshness automation v1 | **Half done.** The link check shipped and is CI-blocking ([`tools/check-links.py`](tools/check-links.py)), and the research-log gate shipped as [`check-research-logs.py`](tools/check-research-logs.py). The `fetch_status` column this WP named appears in **zero** research logs: [ADR 0029](docs/internal/decisions/0029-gate-the-research-log-contract-not-its-layout.md) gates the log's *contract* rather than its layout, and the retrieval conventions live in methodology section 6 instead. The column was superseded, not forgotten. |
| **WP-27** | Docs tree | **Done, and past its own scope.** `CONTRIBUTING.md` exists and the repository now carries a full four-part documentation tree (`docs/tutorials/`, `docs/how-to/`, `docs/reference/`, `docs/explanation/`), shipped 2026-08-07. Two files this WP named by path do not exist: `docs/reference/gate-checks.md`, whose ground is covered by [`docs/explanation/what-the-gate-proves.md`](docs/explanation/what-the-gate-proves.md), and `docs/reference/metadata-schema.md`, which has no equivalent. |
| **WP-28** | Release v0.2.0 | **Done.** Tagged, with a release note written by filling this library's own `release-notes` template. Four further tags have shipped since. |

**Direction, updated 2026-08-22: the floor is complete, M3 is under way, and the build order is now the maintainer's own.** [ADR 0021](docs/internal/decisions/0021-complete-the-tier-1-floor.md) amended grow-by-pull **for the Tier-1 floor only**, and that floor is now complete: 26 bundles cover all 25 templatable Tier-1 types, every family contract is adopted, and the build backlog is empty. **The override has therefore expired on its own terms**, and the roadmap's original ordering (floor, then wedge, then proof, then reach) resumes. **Tier-2 and Tier-3 are no longer demand-gated, and as of 2026-08-22 they are labelled rather than undifferentiated.** [ADR 0039](docs/internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md) made discretion govern whether a type may be built; [ADR 0041](docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md) makes the maintainer's preference and need govern the order, because the queue has received zero issues since it shipped and a ranking input that has never been non-zero cannot rank. Every catalog type now carries a generated `state`: **27 `built`, 176 `candidate`, 2 `out-of-scope`** (`wireframe` and `interactive-prototype`, per [ADR 0030](docs/internal/decisions/0030-templating-scope-markdown-documents.md)). **`candidate` means eligible and unranked, not queued**, and no *bundle* is scheduled. (One non-bundle track now is: the site, planned in [`docs/internal/site-plan.md`](docs/internal/site-plan.md) and adopted by [ADR 0046](docs/internal/decisions/0046-the-site-is-astro-starlight-under-pattern-s.md) on 2026-09-11. Nothing is built, and its own section 10.1 asks that everything past the skeleton wait on one real fill.) **58 of the `candidate` types are marked `rarity: common`**, so the pool is real: what is missing is a decision about each, not permission. *(Counts corrected and gated 2026-09-11: this sentence had read 26/177/61, wrong in all three, and the 61 was never true at any point - the catalog said 59 the day it was written. All four numbers are now facts `check-counts.py` recomputes from `atlas/catalog-data.json`, so the next drift fails CI instead of aging quietly. This is DF-5 for the sixth time.)*

**M3, first usage and wedge, is under way, and as of 2026-09-11 it gates nothing** ([ADR 0047](docs/internal/decisions/0047-the-usage-precondition-leaves-the-language-too.md)). It was described here as the milestone the library "has deferred at every opportunity", which read as an accusation and worked as a gate; ADR 0043 had already removed the usage precondition from policy on 2026-09-03 and the prose had not followed. **WP-30** (LP-2 grade-my-doc, the wedge itself) was **built 2026-08-19** after its build spec sat complete and idle since 2026-07-10, and it is **built, not validated**: most of its acceptance criteria need documents this repository does not have, and no external document has been graded. Two of its four work packages are still unstarted: **WP-31** (one real fill) and **WP-33** (outreach, the only work package that creates demand rather than capturing it). The fourth, **WP-32** (demand capture), is **half built**: the three intake templates in `.github/ISSUE_TEMPLATE/` shipped 2026-08-07 and have received zero issues, and the remainder is specified in [`pull-queue-spec.md`](docs/internal/pull-queue-spec.md).

Coverage and real usage stay separate, honest numbers: still **zero real fills**, and no bundle is called "verified" until that changes. **That is the honesty gate, and [ADR 0047](docs/internal/decisions/0047-the-usage-precondition-leaves-the-language-too.md) deliberately left it standing while removing the scheduling one.** Nothing waits on a usage signal; nothing is *claimed* without one either. All 27 bundles are `beta`.

Full definition: [`docs/internal/roadmap.md`](docs/internal/roadmap.md), whose status column was refreshed 2026-08-14. What is specified versus merely planned: [`docs/internal/plan-inventory.md`](docs/internal/plan-inventory.md).

### M1 record

| WP | What | State |
|---|---|---|

| WP | What | State |
|---|---|---|
| **WP-10** | Citation integrity pass (A-01..A-06) | **Done.** All four delivery-docs bundles verified against raw sources; 28 defects fixed; methodology 0.2.3 codifies the source conventions so the class does not recur. One WP-10 instruction was itself wrong and was withdrawn rather than executed. |
| **WP-11** | Gate hardening v1 | **Done, except the half that may be impossible.** All six named items shipped 2026-07-17: reverse citation direction, meta placeholder scan, history-documents-version, `pairs_with` against a pinned skill list, `related_templates` resolution with the `future:` convention, and heading comparison on (level, text) tuples. Seven checks became nine, each adversarially tested to prove it fails when it should. **The first run of the new padding check failed the `rfc` bundle**, catching three uncited references the author had noticed and rationalised away the day before. Citation-tracing (does the source *support* the claim?) remains open and may not be mechanizable. |
| **WP-12** | Decision closure (D2, D3) | **Done 2026-07-17.** Both resolved by test and by reading the spec, and both answer the same question: **the ecosystem's unit is the skill, not the template.** The CLI installs nothing from this repo because it ships no `SKILL.md`; the spec has no template resource type at all. The pair took under an hour once attempted, having sat open 18 days against a three-day SLA. |
| **WP-13** | Consumer quickstart | **Done 2026-07-17.** Six literal steps, leading the README. Claim reconciliation found the front door claiming deterministic agent selection that does not exist, a family called "verified" days before 28 defects were found in it, a stale four-bundle list omitting all of `decision-docs`, and a `docs/decisions/` path that is both nonexistent and org-forbidden. |
| **WP-14** | Release v0.1.0 (dogfooded release note) | **Done 2026-07-17.** CHANGELOG in Keep a Changelog 1.1.0, [release note](docs/releases/v0.1.0.md) filled from the library's own lean template, tag pushed. **The dogfood worked as intended: it produced DF-1 on its first use** (see below). |

Full definition: [`docs/internal/roadmap.md`](docs/internal/roadmap.md).

## Open decisions, with ages

### Decision triage, 2026-08-21, the first one

**This is the monthly decision-triage half of VL-3 (maintenance cadence), started ahead of its M6
schedule.** Running it does **not** resolve VL-3: the cadence ADR that would fix a schedule and create
calendar entries is still WP-61 in M6 and still stops for the maintainer. What starts here is the practice,
because **the SLA rule below has existed since 2026-07-17 and nothing has ever swept against it.**

| Item | Open since | Age | Stated cost | Verdict |
|---|---|---|---|---|
| **D1**, build the Layer 1 generator | 2026-06-29 | **53 days** | n/a | **Not eligible, and correctly so.** D1's cost is not effort, it is evidence: it needs a real customization to observe, which is WP-33's output. **Deferring it is the decision**, re-affirmed here rather than left to drift |
| **VL-3**, maintenance cadence | 2026-07-02 | **50 days** | n/a | **Not eligible on cost, and half-actioned by this table.** The quarterly source pass stays at M6. The monthly half needed no decision to start |
| [`guide-rubric-spec.md`](docs/internal/guide-rubric-spec.md) **section 4 item 2**, whether the checklist guides convert to scored rubrics | 2026-07-27 | **25 days** | **Unstated.** In practice: convert one and read it | **Not triggered, and that is the finding.** See below |
| [`pull-queue-spec.md`](docs/internal/pull-queue-spec.md) **section 4 open question**, does an unattributed request count as a pull | 2026-08-14 | **7 days** | **Unstated.** A recommended answer is already written | **Not triggered**, same reason |
| **D5**, the demand-rule ADR | 2026-08-14 | **7 days** | M | Not an SLA item; it is a deliverable that stops for the maintainer. Its content is now written, since `pull-queue-spec.md` section 4 was rewritten 2026-08-21 |

**What the first triage found, and it is the reason to run one.**

**The SLA has a loophole, it is load-bearing, and this repository already documented it once without
noticing it was general.** The rule binds "any open decision whose stated resolution cost is under two
hours". VL-1 (business model) sat **43 days** against it, and the entry recording its resolution says
plainly that this happened because it carried **no stated resolution cost, which is why it never triggered
the SLA**. That was written as a fact about VL-1. **It is a fact about the rule**, and two more items are
sheltering under it right now: both open questions above have no stated cost, so neither can ever breach a
rule that only measures items that name one. **An estimate is the trigger, so omitting the estimate is the
exemption.**

Not fixed here. Amending the SLA is a change to how this library governs itself, which stops for the
maintainer, and **naming the loophole on the day the first sweep found it is what a triage is for**. The
minimal repair, if wanted: an open question with no stated cost is triaged as **under two hours until
someone says otherwise**, which inverts the default so silence costs attention rather than buying time.

**One scope gap, surfaced by the same sweep.** `guide-rubric-spec.md` section 4 item 2 names **four**
checklist guides. The tree has **twelve** guides carrying a checklist with no scale and no threshold,
counted 2026-08-19 by testing every guide for a scored-rubric table rather than from a list. The spec's
scope was set against a **16-guide** tree on 2026-07-27 and the tree now holds **26**. The four it names
are still in the twelve; the other eight were never in anyone's scope. **This is not drift in the spec, it
is the population growing out from under it**, and it makes the open question larger than the spec presents
it.

**Next triage due 2026-09-21**, if the cadence holds. Nothing enforces that date, which is the honest state
until WP-61 lands.


| ID | Decision | Open since | Cost to resolve | Scheduled |
|---|---|---|---|---|
| D1 | Build the Layer 1 generator, or not | 2026-06-29 | n/a | Correctly gated on a usage signal |
| ~~D2~~ | ~~Does `npx skills add` install this repo~~ **RESOLVED 2026-07-17: no.** Tested: the CLI clones the repo and installs **nothing**, reporting "No valid skills found. Skills require a SKILL.md with name and description." Verified against a control (`skills add product-on-purpose/pm-skills` succeeds), so the CLI and the org path both work; **this repo is the gap, because it ships no `SKILL.md`.** Unlock is known and cheap: ship one (roadmap LP-2). | 2026-06-29 | 30 min | **Resolved** |
| ~~D3~~ | ~~agentskills.io resource type for templates~~ **RESOLVED 2026-07-17: there is no template resource type.** The [Agent Skills specification](https://agentskills.io/specification) defines exactly **one** unit: a skill, i.e. a directory containing `SKILL.md` (`name` and `description` required; `name` must match the parent directory). **Templates are explicitly an optional bundled asset inside a skill**, not a resource of their own: `assets/` "Contains static resources: Templates (document templates, configuration templates)". A template library is therefore only listable by being wrapped in a skill. | 2026-06-29 | 1 hour | **Resolved** |
| ~~D4~~ | ~~Regulated-industry tier appetite~~ **RESOLVED 2026-08-14: no, for now, and deliberately.** Tier-3 regulated content (FDA design controls, ISO 14971, SOC 2, GDPR) is **not** pursued. The reason is not lack of interest but an obligation this library has not committed to: regulated templates carry a **currency burden**, meaning the regulation text must be re-verified at authoring time and on a cadence forever, and the QMSR retitle effective 2026-02-02 is the standing example of what happens when it is not. A blank-but-wrong regulated template is worse than none. **Re-opens on a pull from a real regulated team**, at which point the burden is being accepted for a named reason rather than speculatively. Note that [ADR 0039](docs/internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md) does **not** unblock this: maintainer discretion governs which types get built, and this tier is closed on a separate ground. | 2026-06-29 | n/a | **Resolved** |
| ~~TX-1~~ | ~~Does this library need a second taxonomy axis?~~ **RESOLVED 2026-07-17: yes, `phase` XOR `classification`** ([ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)). Not a judgment call but a verified partition: parsing all **68** tracked `SKILL.md` in pm-skills gives **30** phase-only, **38** classification-only, **0** both, **0** neither. The Tier-1 set already contains phase-less types (Risk Register, RAID Log, Status Report, Definition of Done). WP-21 will require `phase XOR classification`. (The old row's "89 of 175 / 86" counts were inflated ~2.5x by counting gitignored `.claude/skills/` build copies; the canonical count is 68. ADR 0003 carries the correction.) | 2026-07-12 | ~1 hour | **Resolved** |
| ~~TX-2~~ | ~~The catalog's `phase` field is a different vocabulary from the bundles' `phase`, under the same name.~~ **RESOLVED 2026-07-17 (#18): the catalog field was renamed to `stage`, so `phase` is now unambiguous library-wide.** The catalog/atlas `phase` had ~30 values (`ideation`, `strategy`, `governance`, `communication`, ...); the bundle/pm-skills `phase` has six (`discover`...`iterate`), with near-collisions (`discovery`/`discover`, `definition`/`define`, `measurement`/`measure`). That is a document *stage*, not a lifecycle phase. Decided 2026-07-17 (alongside [ADR 0015](docs/internal/decisions/0015-second-taxonomy-axis-phase-xor-classification.md)): **rename the catalog's field to `stage`** so `phase` is unambiguous library-wide, before WP-21 writes a schema that has to name which `phase` it means. Mechanical but spanned `atlas/catalog-data.json`, `atlas/atlas.html` (an interactive app), and the catalog prose, so it shipped as its own verified change. | 2026-07-17 | ~1 hour | **Resolved** |
| ~~VL-1~~ | ~~Business model~~ **RESOLVED 2026-08-14 ([ADR 0040](docs/internal/decisions/0040-free-and-open-source-no-paid-tier.md)): free and open source under Apache-2.0, no paid tier**, functioning as an authority funnel rather than a product that charges. Open core was rejected for now because it needs entitlement machinery before it has content, and the tier that would most plausibly carry a price is D4, closed above. **This unblocks the site track**, which could not choose a domain or a call to action without it. It had been open **43 days** against a three-day SLA, with no stated resolution cost, which is why it never triggered the SLA. | 2026-07-02 | n/a | **Resolved** |
| VL-3 | Maintenance cadence | 2026-07-02 | n/a | M6 |

**Decision SLA** (audit finding E-05): any open decision whose stated resolution cost is under two hours is resolved within three working days, or explicitly re-dated with a reason. **This is the rule, and it lives here until a CONTRIBUTING.md exists to hold it.**

**D2 and D3 are closed as of 2026-07-17**, 18 days after they were opened and long past the three-day SLA the rule states. Recording that plainly rather than quietly marking them done: the SLA was breached by a factor of six, and the pair took **under an hour** to settle once actually attempted. That is the lesson worth keeping. Both were cheap; both sat open for weeks; and both turned out to answer the same question.

**What D2 and D3 turned out to share.** They were logged as two decisions and are really one fact: **the ecosystem's unit of distribution is the skill, not the template.** The CLI installs skills (`SKILL.md` required); the spec defines skills (templates are an *asset inside* one). This library ships no `SKILL.md`, so today it is **not installable or listable by either route**, and no amount of metadata changes that. The blocker is a single missing file, not an architecture problem, which makes the "agent-native" claim's remaining debt smaller and more concrete than it looked.

> **Corrected 2026-08-08.** The paragraph above is the state on 2026-07-17 and is kept as written. Two of
> its clauses have since been overtaken and one of them was wrong in a way worth naming. The library
> shipped a `SKILL.md` on 2026-08-07 and **the install was executed for the first time on 2026-08-08 and
> succeeded**, so "not installable" is closed. But the second half, *templates are an asset inside a
> skill*, was read as settled and was never tested: the CLI installs **only the skill directory**, so the
> 27 bundles the skill is a wrapper for do not travel with it. The unit of distribution being the skill
> was correct. The inference that shipping a skill therefore distributes the library was not, and it stood
> unexamined for three weeks because the retest that would have shown it sat open.

**Consequence for the roadmap:** WP-52 (distribution wiring) was scheduled "per D2/D3 outcomes". The outcome is now known, so it is no longer research: it is "ship a `SKILL.md` that exposes the bundles as skill assets" (roadmap LP-2), whose name must be lowercase, hyphenated, and match its directory, with a description under 1024 characters. The reference validator `skills-ref validate ./my-skill` exists to check it.

## The claim, and what it is currently worth

The front door claims a **governed, best-in-class, agent-native reference implementation**. As of today:

- **Earned:** researched, dual-reader, nesting-disciplined, provenance-stamped content that the named competitors (curated awesome-lists) do not attempt.
- **Now true, as of M0:** licensed, decision-recorded, CI-enforced (the gate runs on every push and PR, and branch protection requires it before merge), and living at an address that describes it (`templates/`, not `_local/templates/`).
- **Still on credit:** "reference implementation". Twenty-seven of 205 types, and **zero external users**: nobody but the author has filled a template, so by the catalog's own tier rule nothing has graduated. Efficacy is measured rather than argued as of 2026-08-08, and the first measurement returned **VOID** ([`evals/results/`](evals/results/)), which is a weaker position than "unmeasured" rather than a stronger one.
- **Newly earned, and narrower than it sounds:** "agent-native". [`manifest.json`](manifest.json) is the deterministic selection surface (2026-07-17), and the skill installs: `npx skills add product-on-purpose/product-lifecycle-templates` was run for the first time on 2026-08-08 and rerun 2026-08-21 with both skills present, succeeding both times. **What it installs is about 47 KB of instructions and none of the library**, so the install is verified and the installed artifact is not yet useful on its own. See the retest record in [`docs/internal/roadmap.md`](docs/internal/roadmap.md).

Keep this section honest. It is the fastest way to tell whether the roadmap is working.

**It was not honest between 2026-07-17 and 2026-08-08, and that is worth more than the correction.** This
bullet claimed no machine-consumption path existed, that the library shipped no `SKILL.md` and was
therefore not installable, and that it was untagged at 6 of 205 types. Every one of those had been false
for weeks: the manifest landed in July, three tags exist, and the count was off by twenty. Nothing caught
it. `check-counts.py` runs green on this file because every **marker** matches the tree, and not one of
those five false clauses sat near a marker. The check prints that limitation on every run; this is what
the limitation costs when nobody acts on it. **The section that exists to be the source of truth is the
one with no generator behind it**, which is the eighth recurrence of finding DF-5.
