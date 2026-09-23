# Release notes

The curated read of what changed and why it matters. For the full, unabridged record including
unreleased work, read [`CHANGELOG.md`](CHANGELOG.md); for the per-release pages written by filling this
library's own `release-notes` template, read [`docs/releases/`](docs/releases/).

Newest first.

---

## v0.13.0

**Two bundles in one release: an issue log and a definition of ready.** The issue log records problems
that have already happened on a project and who is fixing each; it makes a team say what counts as an
issue first, because the named standards define one four different ways. The definition of ready is a
team's agreement on when a backlog item is ready to start, and it ships carrying the argument about
itself: several of its own sources say a team may be better off without one, so keeping none is a
legitimate outcome.

Both research logs had every quotation checked against the source's raw text, and the check caught a
research agent misreporting the European Commission's issue-log fields. A documentation audit after the
33rd bundle also corrected the security page, which said the repository runs no server.

---

## v0.12.0

**A 31st bundle: the launch coordination checklist**, the standing list a team consults before it ships
an externally visible change. Grouped readiness checks with owners, a go/no-go gate decided in advance,
and a rollout with the condition that reverses it.

It was admitted on a source fetched and read while its spec was written, not on a prior: Appendix E of
Google's *Site Reliability Engineering* book is titled "Launch Coordination Checklist". That appendix is
licensed no-derivatives and dates from "circa 2005", so the bundle teaches the practice around the list
and adapts none of its items.

The part worth keeping is how its research was checked. Every quotation in the research log was compared
with the source's own text rather than with the research tool's summary of it, and **19 of 193 were not
there**. They were removed before anything was drafted from them.

---

## v0.11.2

**The build-cost numbers `v0.11.0` published were about twice the truth, and this release corrects
them everywhere they appeared.**

The generator counted every API response two or three times: the harness writes each response into
its transcript as several records, one per content block, and every record repeats the response's
full usage. Recounted from the same transcripts with nothing else changed, a whole bundle build costs
about 10M to 12M weighted token-equivalents, not 21M to 25M.

Each report now also says what the work would cost at Anthropic API list rates: **$33 to $41 for a
whole build**, over two thirds of it drafting, because the drafting agents ran on Opus. The weighted
unit stays, since it is what keeps two reports comparable, but it was never money, and "what did this
cost" deserved an answer in dollars.

How it hid is the part worth keeping. The decision record for build cost accepted openly that CI can
check the index but never the reports behind it. Stating that weakness did not stop it costing
something: 22 wrong reports shipped with every check green. It was found by pricing the numbers, not
by a gate.

---

## v0.11.1

**Nothing user-facing changed shape here.** No template, no bundle, no MCP tool, no install route.
What changed is what this repository says about itself, and in three places it was saying something
untrue.

The largest gap was an absence: **the library published a website and never told a human reader it
exists.** The README, CONTRIBUTING and all four documentation quadrants carried zero mentions of it.
The technical documentation was already strong and the note for agents was already correct; the human
lens was simply missing. There is now a page explaining how the site is generated, guarded and
deployed, and the README links the site itself.

Two corrections are worth naming because they are the kind this library exists to catch. **The live
landing page claimed the library spans six families; it has nine**, and had since the page shipped,
because that page is `.mdx` and sat outside the prose-count gate's file glob. The gate now reaches it
and is mutation-tested. And **this repository stated a wrong reason for a right decision**: the
comment explaining why the all-in-one Astro action is refused was factually wrong about what that
action does. The decision stands on a better reason, and the correction is left visible rather than
quietly swapped.

---

## v0.11.0

*Corrected in v0.11.2: the cost figures in this section are about twice the truth. Left as they
shipped; the correction is in the v0.11.2 section above.*

**This library refuses to call a single bundle proven without evidence, and the number it used to
decide whether a bundle was worth building had none.**

Two documents stated a per-bundle build cost and they disagreed: the runbook said "roughly 0.6-1M
tokens", the build command said "roughly 700K-1M". Neither cited a measurement. The measurement was
always available: the harness writes a per-agent transcript with a full usage block on every turn,
and nothing had ever read one.

Read, the cost is **21M to 25M weighted token-equivalents per bundle** - between 20 and 30 times the
estimates it replaces. The runbook also said the cost was "dominated by research fan-out and the
four-lens review"; measured, drafting is the largest single stage and the review is under half of
research, which points the next optimisation somewhere nobody was looking.

That number now lives in [`bundle-builds/`](bundle-builds/): one report per bundle per
`template_version`, broken down by stage, by model, by requested tier and by deliverable, generated
rather than typed, and gated in CI like every other generated artifact here. 22 reports were
backfilled.

**Two of the twenty-two cover a whole build.** The other twenty are marked `floor`, because they
predate a change this release also makes: every workflow agent label now carries its bundle type, so
a subagent identifies itself in the run journal instead of being inferred from its own prompt. That
inference worked for agents that write a file and failed for the ones that do not - one research run
was billed to the sibling type it was comparing against.

Four stale claims were corrected on the way, including `STATE.md` reporting twenty-seven bundles
under the heading "Built and true today" when there are thirty and its own generated marker said so
nine lines above.

---

## v0.10.0

**If you installed the MCP server and it never worked, this is the release that fixes it.**

The server could not start from a `git clone`, and had not since it shipped. `.mcp.json` located it
with a variable Claude Code sets only for plugin installs, so opened as an ordinary project the path
never resolved. The server itself was fine the whole time, which is exactly why nothing caught it:
the self-test passed, and the verification that "proved" it drove the server with its own script and
never touched the config.

The same server now speaks a **typed response envelope**. Every tool returns `{ok, data?, error?}`
and responses arrive as `structuredContent` rather than JSON text you have to re-parse. `ok` means
the call completed, never a verdict: a document that fails validation is `ok: true` with
`data.valid: false`. **This breaks anything written against the older shapes**, and it was taken now
because nothing external calls the server yet.

The library also stops publishing a real-fill count. Every bundle is still `beta`, and no page will
call one proven.

---

## v0.9.0

**The library gets a website.** All 30 bundles are readable at
<https://product-on-purpose.github.io/product-lifecycle-templates/> by anyone with a link, instead of
only by someone willing to clone a repository and open eight files per bundle.

Every page is generated from the tree, so no bundle is named by hand anywhere in the site. Five
guards run **between the build and the upload** - links, routes, edit links, a favicon, and the ban on
calling a bundle proven - so the artifact that is checked is the artifact that ships. The first of
them found a live 404 on its first run against a real build.

---

## v0.8.0

**The library grows from 27 bundles to 30, and for the first time publishes the reasoning that let
each one in.**

Three new document types: a spike report, a project or milestone retrospective, and a test summary
report. A fourth, a PI or release retrospective, was **refused on its own evidence** - SAFe's own
facilitator guide names the outputs as backlog items and no document. Two of the three that shipped
teach a dispute rather than a settled practice, because their research said they must.

---

## v0.7.0

**If you installed the MCP server during `v0.6.0` and it would not start, this release is why**, and
the fix is one command: `python3 -m pip install "mcp<2"`.

The `v0.6.0` instructions said `pip install mcp`, which since 2026-07-28 resolves to an SDK v2 that
renamed the class this server imports. The CI check that should have caught it skipped its only
SDK-dependent assertion and exited 0, so nothing had ever verified the server starts.

---

## v0.6.0

**Agents can now find a template without being told where any file lives.**

This library has always been readable by an agent - `manifest.json` says which bundle, `sections.json`
says what is inside it - but only if the agent knew to go looking. `v0.6.0` adds an MCP server with five
tools: search the catalog in your own words, fetch any of the 58 template variants, fetch the grading
rubric, validate a filled document, and strip and stamp it when it is done. It installs with the plugin,
because that route already clones the repository and the templates arrive with the server.

[ADR 0045](docs/internal/decisions/0045-the-mcp-server-is-python-and-lives-in-this-repository.md) records
the decision it was blocked on, and the argument is worth more than the answer. The 2026-07-12 audit
sketch specified a separate TypeScript npm package with an embed step packaging `templates/**` into the
artifact. **That embed step is a fifth copy of the content that no `--check` can reach**, and this
repository's entire architecture is an argument that copies go stale. So it is Python, here, and the two
tools that already existed are **called** rather than reimplemented. The cost is stated in the record:
`pm-skills-mcp` and this now serve MCP differently.

**Building it falsified three claims, and the third one was ours.** The catalog's taxonomy axis is `phase`
XOR `classification` - 17 bundles carry one, 10 the other - so the sketch's phase-only filter would have
returned plausible results while a third of the library stayed unreachable. Only four of the six declared
phase values are used by any bundle. And our own refreshed spec set a 500-token budget for search results
without measuring the field list that same spec prescribes: it costs 1,194. Moving the sizing guidance off
search, where you have not chosen a bundle yet, brought it to 685.

**The other half of this release is about checks that returned something rather than the right thing.**
`tools/run-gate.py` runs every step CI runs, derived from the workflow file rather than from a list anyone
maintains, and prints each step it skipped with a reason - it has no output line saying everything passed,
because a confident summary over a partial run is the failure it exists to prevent. Both install-time
descriptions were false: the plugin listing claimed 28 CI checks against 30, and `library.json` claimed 26
bundles against 27. Neither could be reached by the check that exists for exactly this, because that check
reads markers in Markdown and JSON cannot carry an HTML comment. It reads both descriptions now, and
caught both on its first run.

**And the release note you are reading found a bug.** It is the first document ever filled using
`strip-template.py` and `validate-fill.py` on something that was not a test fixture, and validation failed
immediately: a template whose H1 is entirely a placeholder - `adr` and `release-notes` both - could never
be matched, so **two of the twenty-seven bundles produced documents that structurally could not
validate**. The fixtures had all been built from `prd`, whose headings carry no placeholders. Fixed, and
the suite now builds and validates a document from every one of the 58 variants rather than merely
checking that each one resolves.

**Still zero.** No template in this library has been filled by anyone but the author. No agent outside this
repository has used the server. Nothing about efficacy changed.

---

## v0.5.0

**A 27th bundle, `epic`, and it is the first one built because the maintainer wanted it rather than
because a plan said so.**

Two decision records made that possible.
[ADR 0041](docs/internal/decisions/0041-maintainer-preference-sets-the-build-order.md) made the
maintainer's own preference set the build order, on the ground that a ranking input which has never been
non-zero cannot rank. [ADR 0042](docs/internal/decisions/0042-epic-joins-delivery-docs.md) then admitted
`epic` to the delivery-docs family, after the first attempt to build it stopped on a gate that neither of
the two records removing the *previous* gates had touched.

**The bundle's research is the part worth reading, because it argues against the easy version of the
document it ships.** The 2020 Scrum Guide contains zero occurrences of the word "epic", confirmed by
literal string search rather than by summary. XP substitutes a splitting rule, the Kanban Method has no
product-sized work unit at all, and LeSS Huge partitions one flat backlog instead. Only SAFe formalizes
the artifact. In its native habitat an epic is a tracker record, not a document, and the bundle says so on
its own catalog card rather than overselling itself.

**Nothing here changes an existing template, a meta field, or the bundle contract.** Upgrading is safe.

**The caveat, unchanged since this library existed: nobody outside this repository has filled one of these
templates.** 27 bundles is a bigger library, not a used one.
[The full note](docs/releases/v0.5.0.md).

---

## v0.4.0

**A second skill, for people who are not using the library, and four claims it was making about itself
that were not true.**

[`plt-grade-doc`](skills/plt-grade-doc/) takes a product document you already have and grades it against
that document type's own researched rubric, quoting your own text back as evidence. You do not have to
adopt a template to get something out of it. **Its first run graded this repository's own governance and
found a defect no automated check here looks for.**

The other half is less flattering and more useful. **The eval harness had never run, and not because
nobody tried.** One line missing from `.gitattributes` made it mechanically impossible on Windows: the
harness scripts had been pure CRLF since they were written, and the permission dialog rejected them as
containing control characters. Once fixed it ran, and produced this project's first real cost figure.
**Four separate claims the library published about itself turned out to be false**, each found by running
something rather than by reading it.

**The honest position is unchanged: zero fills by anyone but the author.**
[The full note](docs/releases/v0.4.0.md).

---

## v0.3.1

**A documentation patch, cut because the previous tag denied the evidence it shipped with.**

The doc-honesty sweep landed one commit after `v0.3.0` was tagged. So the tree the marketplace pins told
readers in four places that **"there are no efficacy evaluations"** while carrying two of them in
`evals/results/`. A published tag is not moved, so the correction is a release.

Two more of the same defect were found on the way and fixed here. **This file** said template quality
"has not been measured" in its standing closing section, three headings below its own `v0.3.0` entry
reporting two VOID runs. And [ADR 0036](docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md)
still called the install retest one that "has never been run", after it had been run and its consequences
written into the next record.

**Nothing you use changes.** No template, no bundle, no gate check.
[The full note](docs/releases/v0.3.1.md).

---

## v0.3.0

**Gold tier, a withdrawn finding, and two defects found by running the install nobody had run.**

The library reached **Gold (advanced)** on the Advanced Skill Library Standard, measured by the
Standard's own gate running in this repository's CI rather than declared.

**The efficacy pilot's headline was withdrawn.** Its held-out gap of -0.81, which read as evidence these
templates suppress decision-usefulness, was an artifact of the measurement: the control arm had been told
to produce decision-usefulness and the treatment arm had not. With the arms matched it is **-0.03**. What
replaces it is quieter and harder to dismiss, and is now measured across two independent runs: **+0.85 on
criteria drawn from the templates' own guide, beside nothing at all on criteria drawn from neither.** Both
runs remain **VOID**. Nothing here is evidence that the templates improve documents.

**`npx skills add` was executed for the first time**, three weeks after the skill shipped, and produced
two defects. It installed a **maintainer-internal build harness** alongside the real skill, because
removing the root `SKILL.md` in v0.2.0 removed a short-circuit that had been suppressing the installer's
subdirectory search. And it installed **12 KB with none of the 26 bundles**, so the skill was reachable
and inert. Both are fixed: the harness is no longer a skill, a check now asserts that what ships equals
what the manifest declares, and the skill stops rather than writing a document it has no template for.

**If you install this library, read [`docs/how-to/installing.md`](docs/how-to/installing.md).** There are
two routes and they do not give you the same thing.

---

## v0.2.1

**The library became listable.** The Product on Purpose plugin registry refuses to list a repository that
ships no `library.json`, treating it as loose components rather than a library. This release adds that
manifest, binding the [Advanced Skill Library Standard](library.json) and declaring a tier.

**The tier was measured rather than declared.** The Standard ships its own conformance gate. Run against
this repository it exits 0 at tier **universal** and prints a real backlog above that ceiling. Declaring a
tier without running the gate would have been this library's own dominant defect, committed into a
governance registry.

**Why this is a separate release from v0.2.0.** The registry pins a commit SHA and requires it to sit on a
release tag whose tree contains the manifest. `v0.2.0` was tagged before its listing contract was read, so
its tree has no `library.json`, and a published tag is not moved. The cost of reading a downstream contract
late is one extra release, and the lesson is now written down in
[`release-process.md`](docs/internal/release-process.md).
[The full note](docs/releases/v0.2.1.md), backfilled 2026-08-09 and dated as such.

## v0.2.0

**The Tier-1 floor is complete.** Every templatable must-have type in the 205-type catalog now ships as a
governed bundle, across nine complete families, and the build backlog is empty. Coverage was the binding
constraint from the beginning of this library; it no longer is.

**The library got a front door.** Before this release every documentation file was maintainer-internal:
the repository documented how it governs itself far better than how to use it. Four user-facing pages now
exist, reachable from the README:
[getting started](docs/tutorials/getting-started.md),
[choosing a template](docs/reference/choosing-a-template.md),
[filling a template](docs/how-to/filling-a-template.md), and
[what the gate proves](docs/explanation/what-the-gate-proves.md).

**It became installable.** A `SKILL.md` and a plugin manifest close a gap that had been open since
2026-07-17, during which `npx skills add` against this repository cloned it and installed nothing.

**Eight unsourced claims across seven family contracts were corrected.** A back-audit tested every
contract assertion against the research logs of the members actually built. Two of every three failures
were **labelling rather than error**: correct content stated as though the field had discovered it. The
result is a new decision procedure requiring every contract sentence to declare which mood it is in, and
none of the corrections changed an obligation.

## v0.1.0

**The first tagged release.** Four bundles and the governance gate that admits them. The gate is the point:
a bundle is not a folder of files that look right, it is a folder that passes eleven checks, and the
checks were written before the bundles were.

---

## What this library does not claim

Every release above describes coverage and governance, both of which are checkable. **None of them claims
the templates are good.**

Quality has been measured **four times**. Two independent runs on 2026-08-08 over three of the bundles
then in the library returned **VOID** on the discrimination gate, as did a single-scenario run on
2026-08-21. What those runs did show is the **circularity signature**: a clear gap on criteria drawn from
the templates' own guide, beside nothing at all on criteria drawn from neither
([the result](evals/results/2026-08-08_matched-rerun.md)).

**The fourth run, on 2026-09-03, is the first that is not void.** All four validity gates pass and the
bootstrap is non-degenerate for the first time, so it produces a countable gap rather than a shrug
([the result](evals/results/2026-09-03_two-scenario.md)). **What it does not produce is a verdict on this
library.** It covers **two scenarios of one bundle**, `prd`, out of twenty-seven. It also returned a probe
gap of exactly **0.00**, which is ambiguous between "the template does not help a reader" and "the
scenarios were too easy", and the protocol currently specifies neither harder scenarios nor a weaker
generation model to tell those apart.

So the position is narrower than "measured" and better than "unmeasured": **the instrument now works well
enough that a null result is informative, and it has been pointed at one bundle.** No template in this
library has been filled in anger by anyone but its author, and the honest scope of the quality claim is
written up in [what the gate proves](docs/explanation/what-the-gate-proves.md).
