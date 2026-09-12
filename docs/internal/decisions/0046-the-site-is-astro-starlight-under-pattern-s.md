---
status: accepted
date: 2026-09-11
decision-makers: [jprisant]
consulted: [claude]
---

# The site is Astro plus Starlight under Pattern S, and it brings a Node toolchain this repository does not have

## TL;DR

- **Decision:** build the library's public site as **Astro plus Starlight** in a **`site/` subdirectory** of
  this repository, with a dependency-free Node generator writing **gitignored** pages into
  `site/src/content/docs/`, deployed through the GitHub Pages artifact flow with composable steps. Adopt
  [`site-plan.md`](../site-plan.md) as the plan of record. Reject the 2026-07-17 proposal's plain Astro,
  its `glob({ base: '../templates' })` content mount, and its all-in-one `withastro/action` deploy.
- **Why:** the family site standard (`SITE-STANDARD.md` in `agent-plugins`, at
  `standards/domains/astro-sites/`) makes all three MUSTs, and the proposal **cites it zero times**. The
  content mount is not a style question: the standard records a **build test** showing that an app in
  `site/` with content at repo root fails to build, because bare Starlight component imports resolve only
  inside the app.
- **Also decided, and the part with teeth:** this repository **takes on Node**. It has no `package.json`,
  no `.nvmrc` and no Node in CI today; every tool and every gate step is Python. A site means npm, a
  committed lockfile, `npm ci`, and a second dependency-update surface, permanently. That cost is the real
  decision hiding inside "build a site", and no version of the plan had named it.
- **Status:** accepted 2026-09-11. Supersedes the proposal's section 3, 4 and 8. Closes the question
  [`plan-inventory.md`](../plan-inventory.md) row 7 has carried since 2026-07-02.

## Context and Problem Statement

Twenty-seven researched bundles are reachable only by cloning a repository. A site is the cheapest reach
multiplier the library has, and the gating decision behind it (VL-1, business model) closed on 2026-08-14
by [ADR 0040](0040-free-and-open-source-no-paid-tier.md).

A plan existed: `_local/planning/claude_2026-07-17_astro-site-plan.md`, written 2026-07-17. It could not be
built from, for two reasons that took reading it to find.

**It contradicts itself.** Section 3 argues at length for plain Astro and explains why Starlight is the
wrong choice. A banner added the same day reverses that call on new evidence, and **the body was never
updated**. A reader following the document's own argument builds the wrong thing.

**It contradicts the standard it never read.** `SITE-STANDARD.md` governs every documentation site in this
family. The proposal cites it zero times and conflicts with it in three places: the framework (14.2), the
content mount (14.1), and the deploy shape (14.6).

A third problem is the one nobody wrote down. **This repository has no Node at all**, so the plan's entire
first phase silently assumed a toolchain that does not exist here.

> **A correction carried into this record.** The previous session's log said the proposal "predates the
> standard". It does not: the standard's last commit is **2026-06-02** and the proposal is dated
> **2026-07-17**. The proposal simply never looked. That distinction matters, because "it predates the
> rules" is an excuse and "it did not check" is a process defect.

## Decision Drivers

* **The standard's MUSTs are not re-litigable by a downstream plan.** Clauses 14.1, 14.2 and 14.6 are MUST.
* **One maintainer, two sites, one stack.** `pm-skills` runs the Starlight-plus-generator pattern in
  production and is the standard's named reference implementation.
* **A build test beats an architectural preference.** Pattern W is not merely discouraged; it is recorded
  as failing to build.
* **Honesty obligations do not weaken on a public surface.** They get more tempting to weaken, so at least
  one of them should be mechanical rather than discretionary.
* **The true cost should be in the decision, not discovered during it.**

## Considered Options

1. **Astro plus Starlight under Pattern S** (this decision).
2. **Plain Astro**, as the proposal's body argues.
3. **Pattern W**: app at repo root, content mounted from `../templates` by a custom loader.
4. **A separate site repository.**
5. **No site**; keep the library clone-only.

## Decision Outcome

**Chosen: option 1.**

Option 2 is refused by clause 14.2, and its own justification does not survive contact: the custom-layout
need it cites (X-ray view, role tabs, lean/full diff) is satisfiable inside Starlight, because the X-ray
remark plugin is stack-agnostic and Starlight has a custom-page escape hatch for the rest.

Option 3 is refused by clause 14.1 and by the build test behind it. This is the proposal's actual pipeline,
and it is the single most important thing this record reverses.

Option 4 reintroduces the sync drift the library exists to refuse; the site's whole value is rendering this
repository's truth, and it should version with the content it renders.

Option 5 is the status quo, and it is what "the presentation layer for 27 bundles that no one can currently
browse" has meant for two months.

### Version set

Pin the family-current resolved set, which is what `pm-skills` resolves today: `astro ^7.2.4`,
`@astrojs/starlight ~0.41.7`, `astro-mermaid ~2.1.0`, `sharp ^0.35.3`, `engines.node >=22.12.0`, `.nvmrc`
of `24`, read in CI through `node-version-file`.

**The standard's Astro-6 language is dated; the Node floor it derives is not.** `SITE-STANDARD.md` says
"Astro 6 requires Node `>=22.12.0`" and was written 2026-06-02. The family has since moved to Astro 7.
Clause 14.8 requires the resolved set to match family-wide and to be pinned by **committed lockfile plus
`npm ci`**, not by a caret range, so matching pm-skills is what conformance means in practice rather than
a departure from it.

### Consequences

**Good.**

* The site starts conformant by construction rather than earning conformance later.
* Starlight supplies the sidebar, Pagefind, theming, `editLink`, `lastUpdated` and sitemap registration
  that the proposal would have hand-built.
* Gitignored-and-rebuilt generated content has **no drift surface**, because nothing generated is committed.
* The zod mirror of `tools/meta.schema.json` survives as a genuine second gate **on the read side**.

**Bad, and stated plainly.**

* **This repository takes on an entire second toolchain.** npm, a lockfile, `npm ci`, Node version pinning,
  and a dependency-update surface it has never had. Every gate step today is Python.
* **The shared preset does not exist.** Decision A-2 of the standard says each site consumes
  `@product-on-purpose/astro-docs-preset` as a git-tag dependency. Verified 2026-09-11:
  `gh repo view product-on-purpose/astro-docs-preset` returns "Could not resolve to a Repository". So this
  site hand-rolls its Starlight config now and migrates later as a dependency swap. **Vendoring it once it
  exists remains the rejected anti-pattern.**
* **The guards are a local port, not shared infrastructure.** Clause 14.11 sanctions exactly this bridge,
  because deferring a MUST to unbuilt infrastructure leaves it unmet for an unbounded time.
* **Effort was under-described by roughly an order of magnitude.** The proposal's "1 to 2 days" for its
  first phase is withdrawn rather than adjusted. Measured against the donor, the Node surface is
  **1,500 to 2,000 lines** written or adapted: pm-skills' `gen-site.mjs` alone is **868 lines** and its four
  guards total **628**.

### Confirmation

Conformance is checked by [`site-plan.md`](../site-plan.md) section 12, clause by clause.

**That checklist is explicitly provisional, and this record says why.** `SITE-STANDARD.md` section 3 states
that its clauses "land in `STANDARD.md` as a new Section 14" and that numbering is allocated at land time.
**Verified 2026-09-11: Section 14 has not landed.** The family Standard in `agent-skills-toolkit` at the tag
this repository pins (`v1.10.0`, tracked as `standard: 0.12` in `library.json`) carries **sections 1 through
12 and no more**. This site therefore conforms to a **domain standard pending amendment**, and any claim
that it conforms to "Standard Section 14" would be false today. When Section 14 lands, the numbers are
re-checked against the landed text and this record is amended if they moved.

## More Information

**One honesty rule becomes mechanical.** `gen-site.mjs --check` scans its own emitted output and fails the
build on `proven`, `verified`, `validated`, and any percentage adjacent to a bundle id, outside an
allow-listed context so the STATE ledger can keep quoting those words to disown them. The other rules
(bundles stay `beta` until a real usage cycle; zero real fills published as zero) stay prose, and
[`site-plan.md`](../site-plan.md) section 13 says so rather than implying all four are enforced.

The reason for building it rather than writing it down is five days old. The MCP server's CI self-test
degraded to a skip when its dependency could not be imported, printed OK, and hid a server that could not
start for the whole of `v0.6.0` - **DF-7** in [`STATE.md`](../../../STATE.md). A rule with no failure mode
is a report. Every guard ported under clause 14.11 must be run against a deliberately broken fixture and
observed to fail before it is trusted.

**Sequencing is a preference, not a gate.** [`site-plan.md`](../site-plan.md) section 10.1 records that S0
may run as a parallel track and that S1 and later should wait on one real fill (WP-31), because zero real
usage is this library's binding constraint and a site is the most attractive available way to defer it
again. [ADR 0043](0043-the-usage-gate-becomes-advisory.md) made the usage gate advisory, so this binds
nothing; it is the roadmap's own priority, written where a future session will see it.
