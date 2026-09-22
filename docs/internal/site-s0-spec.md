# Spec: S0 of the site, the slice that makes it exist

Status: **DONE, 2026-09-21. All 20 acceptance criteria met, and the site is live at
<https://product-on-purpose.github.io/product-lifecycle-templates/>.** Written 2026-09-19, executed
2026-09-20 and 2026-09-21 across four pull requests (#163 spec corrections, #165 the generator, #166
the guards and deploy, and this one). Traces to [`site-plan.md`](site-plan.md) section 10 (phase S0)
and section 9 (the Node toolchain), and to the family standard `SITE-STANDARD.md` in `agent-plugins`
at `standards/domains/astro-sites/`.

**What executing it corrected in it**, kept because a spec that was wrong in four places and says so
is worth more than one that quietly agrees with the code:

| The spec said | Execution found | Where |
|---|---|---|
| The generator would be **larger** than the donor's 868 lines | **587**, because `manifest.json` already carries every per-bundle field and no YAML parser is needed | section 7 |
| Role tabs force `.mdx`, whose brace handling would mangle templates, so defer them to S1 | Built both ways: rendered output **byte-identical but for whitespace**, because templates are always fenced. Tabs shipped in S0 | section 7 note 4 |
| AC-4's mutation test would go red when an `editUrl` stamp is stripped | It **could not**: the donor guard's `existsSync` passes on the generated, gitignored fallback path. Re-specified to require git-tracked | AC-4 |
| `src/content/docs/` is gitignored | Only the `bundles/` subpath is; hand-authored pages live there and must stay tracked | AC-3, corrected before execution |

**And one criterion had no implementation at all until closeout.** AC-6's favicon guard did not
exist when #166 merged; the favicon resolved, but nothing asserted it. Writing it confirmed finding
4.3 on a real 34-page build: Starlight emits **only** `rel="shortcut icon"`, never `rel="icon"`.

Adopted decisions this spec implements rather than reopens:

| Decision | Record |
|---|---|
| Astro plus Starlight under Pattern S; this repository takes on Node | [ADR 0046](decisions/0046-the-site-is-astro-starlight-under-pattern-s.md) |
| No sequencing precondition; S0 runs whenever the maintainer wants | [ADR 0047](decisions/0047-the-usage-precondition-leaves-the-language-too.md) |
| Dependency updates follow the family Dependabot pattern; no `npm audit` gate | [ADR 0051](decisions/0051-site-dependency-updates-follow-the-family-dependabot-pattern.md) |
| Free and open source, which settles the domain question by default | [ADR 0040](decisions/0040-free-and-open-source-no-paid-tier.md) |

**Maintainer decisions taken 2026-09-17 and 2026-09-18.** The first two now live in
[ADR 0052](decisions/0052-the-site-is-a-standalone-property-at-the-github-io-path.md), which is where
they belong: the URL is the part other repositories copy, and it should not have lived only in a spec
header. Summarised here so this document reads without a detour.

- **The site is served at `product-on-purpose.github.io/product-lifecycle-templates`.** A custom domain
  under `productonpurpose.com` stays available later at low cost, because GitHub Pages redirects the
  `github.io` URL once a custom domain is configured. One sibling, `thinking-framework-skills`, already
  runs on a subdomain, so the family is not uniform here and this is a choice rather than a default.
- **The site presents as "Product Lifecycle Templates", standing alone**, matching `pm-skills` and
  `agent-skills-toolkit`. This is what decision A-4 of the family standard already chose: per-plugin
  sites, with a portal revisitable later purely as an aggregator.
- **No root `package.json`.** See section 5.1.

---

## 1. What already exists, and what does not

**Verified 2026-09-18 by building it.** This is not a paper spec. A throwaway scaffold on
`spike/site-samples` built three real Starlight pages, and every claim in section 5 that says
"verified" was observed in that build rather than reasoned from the plan.

What exists in this repository today:

- **GitHub Pages is enabled**, source `GitHub Actions`, `build_type: workflow`, serving
  `https://product-on-purpose.github.io/product-lifecycle-templates/`. No deployment has run, so the
  API reports `status: null`.
- **`.gitattributes` now pins the five file shapes the site introduces** (`*.ts`, `*.css`, `*.txt`,
  `.nvmrc`, `.gitignore`). This currently lives on `spike/site-samples` and **must land with S0**; see
  AC-14.
- Every generator and every gate step is Python. The one Node in `ci.yml` is `actions/setup-node`
  provisioning a runtime for the conformance gate, which is a program in another repository.

What did not exist when this was written, and **all of which now does**: `site/`, `scripts/`,
`package.json`, `.nvmrc`, a lockfile, `.github/workflows/site.yml`, `.github/dependabot.yml`.

> **Section 1 is kept in its original tense as a record of the starting state**, not updated into a
> description of today. The first bullet above is the one that has actually changed meaning: Pages
> reported `status: null` because nothing had deployed, and the first deployment ran 2026-09-21,
> with `build: success` and `deploy: success`.

**The shared preset does not exist either.** `product-on-purpose/astro-docs-preset` returns "Could not
resolve to a Repository", re-verified 2026-09-18. Its spec is written (`shared-preset-spec.md` in the
standards bundle) and the repository is not. So this site hand-rolls its Starlight config, which is the
standard's own sanctioned bridge, and migrating later is a dependency change rather than a copy.
**Vendoring the preset remains the rejected anti-pattern.**

---

## 2. What this is for, stated narrowly

S0 is **"it exists"**: a deployed site that renders every bundle from the tree, guarded, with nothing
hand-listed. It is not the signature experience.

The value is that 30 researched bundles become readable by anyone with a link, instead of only by
someone willing to clone a repository and open eight files per bundle.

What S0 is deliberately not is in section 8.

---

## 3. Deliverables

```
product-lifecycle-templates/
  .nvmrc                       NEW   "24"
  scripts/                     NEW   dependency-free Node .mjs
    gen-site.mjs                     reads the tree, writes site/src/content/docs/bundles/
    check-rendered-links.mjs         guard, ported
    check-route-parity.mjs           guard, ported
    check-favicon.mjs                guard, written here (the donor has no equivalent)
    verify-edit-links.mjs            guard, ported WITH a fix; see AC-4
    route-manifest.txt               the committed route baseline check-route-parity reads
    site-base.mjs                    the ONE place the base literal lives; astro.config imports it
  site/                        NEW   the Astro app
    astro.config.mjs                 site + base + accent + mermaid, set ONCE
    package.json                     engines.node lives HERE, not at the root
    package-lock.json                committed; npm ci, never a caret range
    public/favicon.png               family placeholder, a #5C7CFA compass mark
    public/robots.txt                points at the sitemap
    src/content.config.ts            docsSchema() extended
    src/styles/custom.css            accent tokens
    src/content/docs/                TRACKED; hand-authored narrative pages live here
      bundles/                       GITIGNORED generated subpath, rebuilt every build
  .github/workflows/site.yml   NEW   build + deploy, guards between them
  .github/dependabot.yml       NEW   per ADR 0051
  .gitattributes               MOD   five new pins (already written, see AC-14)
  .gitignore                   MOD   site/node_modules, site/dist, site/.astro, generated content
```

Unchanged and never built by Astro: `templates/`, `manifest.json`, `sections.json`, `atlas/`,
repo-root `docs/`, `tools/`.

### 3.1 The word "docs" now means two things

Repo-root `docs/` is governance prose and **MUST NOT** be built by Astro. `site/src/content/docs/` is
rendered website content, read by the stock Starlight `docsLoader()` called with no arguments. That
split is clause 14.1, and the standard records a build test behind it: moving the app into `site/`
while leaving content at repo-root `docs/` **fails the build**, because bare
`@astrojs/starlight/components` imports resolve only when the `.mdx` lives inside the app.

### 3.2 The language split is a MUST, not a preference

Node `.mjs` in `scripts/`, Python stays in `tools/`. Clause 14.3 states outright that new Python site
generators **MUST NOT** be introduced. That bites here precisely because every other generator in this
repository is Python.

---

## 4. Four findings from the 2026-09-18 build, and what each one changes

These are the parts the site plan does not contain. Each was observed, not reasoned.

### 4.1 The reference implementation does not guard the artifact it deploys

Clause 14.11 is explicit: guards run "in **both the PR build and the deploy build** (so the deployed
artifact, not only the PR, is checked)."

`pm-skills` runs all four guards, enforcing and unconditional, on push to `main` - but inside
`validation.yml`, against a **separate build** of the same commit. `deploy-pages.yml` builds again and
uploads without any guard. The two workflows race, and **a guard failure does not stop a deploy.** The
artifact that is checked is not the artifact that ships.

**What this spec does instead:** the guards run inside `site.yml`, between `astro build` and
`upload-pages-artifact`. One build, guarded, then uploaded. Simpler than the donor, and it meets the
clause without an argument about whether two builds of one commit are the same artifact.

### 4.2 The family Node floor is below what the dependency tree demands

`npm install` warns `EBADENGINE: undici@8.10.2 requires node >=22.19.0`. Clause 14.8's floor is
`>=22.12.0`. The build succeeds on 22.12.0 anyway, which makes the floor **misleading rather than
broken**: an installer on 22.12 gets a warning and working software, until undici reaches a path that
needs 22.19.

**What this spec does:** declares `engines.node: ">=22.19.0"` in `site/package.json`, a deliberate
departure from clause 14.8's literal value, recorded here rather than made silently. The `.nvmrc` pin
of `24` is unaffected and already protects CI. **The clause is stale family-wide and is being raised in
`agent-plugins` separately.** If the standard moves, this value re-aligns with it rather than the
reverse.

### 4.3 Starlight emits `rel="shortcut icon"`, not `rel="icon"`

The favicon is a 14.9 MUST because Starlight emits an icon link on every page unconditionally, so a
missing one is a 404 everywhere. Verified: it resolves 200 on all four built pages including
`404.html`, and is base-prefixed correctly.

**But the attribute is `rel="shortcut icon"` when a PNG is configured.** A guard grepping for
`rel="icon"` reports a false failure. This is exactly the guard-robustness class clause 14.11 makes
normative, and it belongs in the guard's own test.

### 4.4 `.gitattributes` covered none of the file shapes the site introduces

`git add` warned CRLF on `.ts`, `.css`, `.txt`, `.nvmrc` and `.gitignore`. **`.nvmrc` is the dangerous
member:** CI reads it through `node-version-file`, so a CRLF checkout hands `setup-node` a version
string with a trailing carriage return.

This is the `*.mjs` lesson repeated. That pattern was missed until 2026-08-21, when the eval harness
could not start because its files had been pure CRLF since the day they were written - under a comment
describing the exact failure its own pattern did not cover. **A new toolchain brings new extensions;
pin them when it lands, not after something will not start.**

---

## 5. What the 2026-09-18 build already proved

Recorded so S0 does not re-litigate settled mechanics:

- **Pattern S builds.** Content inside the app, stock `docsLoader()`, 4 pages, Pagefind index and
  sitemap generated, zero console errors.
- **`editUrl` stamping works** (site-plan 4.2). A bundle page's Edit link resolved to
  `templates/spike-report/spike-report_template-lean.md`, its true source, rather than auto-deriving to
  a gitignored path.
- **The base path needs no manual handling.** No unprefixed internal `href` appeared anywhere in the
  built output; Starlight consumed `base` from `astro.config.mjs` throughout.
- **MDX is available transitively** via `@astrojs/starlight`, so Starlight components work in `.mdx`
  without adding `@astrojs/mdx` as a direct dependency. If it is ever added directly, clause 14.2
  requires it **after** `starlight`.
- **The donor's real dependency set is larger than the site plan's table.** It also carries
  `@astrojs/markdown-remark` and `overrides` pinning `mermaid` and `devalue`. An override exists to
  dodge something; **copy an override only with its reason recorded**, and drop it if the reason no
  longer applies. `@astrojs/markdown-remark` becomes a direct dependency only if a remark plugin is
  written, which is the deferral in section 8.

### 5.1 No root `package.json`

The donor has one, and it exists **only** to hold a `js-yaml` devDependency for one validator script.
Every validator in this repository is Python, so a root `package.json` here would be a file whose
entire job is to hold one line. `engines.node` goes in `site/package.json`, matching the donor's actual
placement rather than site-plan section 9 item 1.

`.nvmrc` still lives at the repo root, because CI reads it from the checkout root via
`node-version-file`.

The donor runs **two separate npm projects with two lockfiles, not npm workspaces.** Here that
collapses to one project, in `site/`.

---

## 6. Acceptance criteria

Numbered so an autonomous session can report against them, and so "done" is not a judgment call.

- [x] **AC-1.** `site/` builds with `npx astro build` and emits `dist/` with a page for every bundle in
      `manifest.json`. No bundle is hand-listed anywhere.
- [x] **AC-2.** `scripts/gen-site.mjs` is dependency-free Node `.mjs`, reads `templates/`,
      `manifest.json`, `sections.json` and `atlas/catalog-data.json`, and writes into
      `site/src/content/docs/`. No new Python site generator exists (clause 14.3).
- [x] **AC-3.** **Only the generated subpath is gitignored**, currently
      `site/src/content/docs/bundles/`, and a clean checkout plus `npm ci && npm run build` produces the
      site (clause 14.4, preferred model). Hand-authored narrative pages live in
      `site/src/content/docs/` too and **MUST stay tracked**.

      > **Corrected 2026-09-20, and this criterion was wrong as first written.** It said
      > "`site/src/content/docs/` is gitignored", which would make every hand-authored page
      > untrackable. The donor settles it: `pm-skills` ignores **five specific generated paths**
      > while **tracking 127 hand-authored pages in the same directory**. The error survived writing
      > the spec because the site plan describes the generated-content model in prose and the prose
      > does not distinguish the directory from the generated subtree - it was caught by reading
      > `pm-skills/.gitignore` rather than anything written about it, and by the spike's own two
      > narrative pages turning out never to have been committed.
- [x] **AC-4.** Every generated page sets `editUrl` to its true source file, or to `false` where it has
      no single source. **Mutation-checked:** removing the stamp makes `verify-edit-links.mjs` exit
      non-zero (clause 14.11, site-plan 4.2).

      > **Amended 2026-09-20 after reading the donor guard, and the criterion was untestable as first
      > written.** The donor's `verify-edit-links.mjs` validates each target with `existsSync` (line 93),
      > a filesystem check. Strip the stamp from a generated bundle page and Starlight falls back to a
      > `filePath`-derived URL at `site/src/content/docs/bundles/<x>.md`. That file **is on disk** - the
      > generator just wrote it, in CI as much as locally - so `existsSync` returns true and the guard
      > **passes**, while the link 404s on GitHub because AC-3 gitignores that path. The mutation this
      > criterion requires would never have gone red. This is DF-7 (the gate that skipped its own
      > assertion and printed OK) in a new place.
      >
      > **The ported guard MUST therefore assert the target is git-tracked, not merely present**: build a
      > `Set` from one `git ls-files` call and test membership. It MUST also carry the donor's
      > `MIN_EDIT_LINKS` occurrence floor, which exists so the guard fails on 0/0 rather than passing when
      > editUrl emission breaks entirely. Both are required before AC-12's `editUrl` fixture counts as
      > satisfied.
- [x] **AC-5.** `site` and `base` appear exactly once as consumed config, in `astro.config.mjs`. Any
      validator needing the base imports it from `scripts/site-base.mjs`. The two sanctioned exceptions
      are a test value-pin and `public/robots.txt` (clause 14.7).
- [x] **AC-6.** A favicon resolves **200 on every built page including `404.html`**. The guard asserting
      this matches `rel="shortcut icon"` as well as `rel="icon"`, and **has a test proving it catches a
      removed favicon** (clause 14.9, finding 4.3).
- [x] **AC-7.** `.github/workflows/site.yml` has a build job and a deploy job. The deploy job `needs`
      build and is gated to `environment: github-pages`. Actions pinned to `upload-pages-artifact@v5`
      and `deploy-pages@v5` (clause 14.6).
- [x] **AC-8.** **The guards run between `astro build` and `upload-pages-artifact`, in the same job**, so
      the guarded artifact is the deployed artifact (clause 14.11, finding 4.1).
- [x] **AC-9.** A PR-triggered, non-deploying job runs the **same build recipe** as the deploy build, as
      an event-gated tail rather than a second recipe (clause 14.6).
- [x] **AC-10.** CI reads the Node version via `node-version-file: .nvmrc`, never a hardcoded literal
      (clause 14.8).
- [x] **AC-11.** The version set is pinned by a **committed lockfile plus `npm ci`**, not by caret ranges
      (clause 14.8). `site/package.json` declares `engines.node: ">=22.19.0"` per finding 4.2.
- [x] **AC-12.** **Every ported guard has been run against a deliberately broken fixture and observed to
      fail** before being trusted: a broken internal link, a removed route, a stripped `editUrl`, and an
      empty-but-existing `dist`. A guard that has never gone red is a report, not a gate (DF-7).
- [x] **AC-13.** `.github/dependabot.yml` exists, targets `npm` at `/site`, weekly, grouped, `minor` and
      `patch` only, with a `dependencies` label and a `chore(deps)` prefix. **No `npm audit` step is
      added to CI** (ADR 0051).
- [x] **AC-14.** `.gitattributes` pins `*.ts`, `*.css`, `*.txt`, `.nvmrc` and `.gitignore` to `eol=lf`,
      and **`git add` of the full site tree emits zero CRLF warnings** (finding 4.4). This change
      currently sits on `spike/site-samples` and must land with S0 rather than only on that branch.
- [x] **AC-15.** No rendered page states a count as a literal. Every number derives from `manifest.json`
      or `sections.json` at build time (site-plan section 11; DF-5 applied to a new surface).
- [x] **AC-16.** `gen-site.mjs --check` **fails the build** on the strings `proven`, `verified`,
      `validated`, and on any percentage adjacent to a bundle id, outside an allow-listed context.
      **Mutation-checked** by planting one and observing a red build (site-plan 13.1).
- [x] **AC-17.** No page calls any bundle proven, and every bundle shows `beta` (site-plan section 13).

      > **Amended 2026-09-21 by [ADR 0055](decisions/0055-retire-the-zero-fills-disclosure.md).** This
      > criterion also required that "zero real fills is published as zero rather than omitted or
      > softened". That clause is retired and the site no longer publishes a fill count. The two
      > clauses that remain are the ones that prevent a **false** claim; the retired one required a
      > **negative** one, which is a different thing. The `proven` / `verified` / `validated` ban
      > stays gate-enforced and mutation-tested under AC-16.
- [x] **AC-18.** `site.yml` is a separate workflow from `ci.yml`, and the content gate remains the only
      required check until the site is stable (site-plan 8.1).
- [x] **AC-19.** The existing gate still passes: `python tools/run-gate.py` reports 0 failed.
- [x] **AC-20.** The site deploys, and `https://product-on-purpose.github.io/product-lifecycle-templates/`
      serves the landing page over HTTPS.

---

## 7. Effort and sequencing

**Stated in lines against a measured donor, deliberately not in days.** Every effort number this
repository has published in days has been wrong.

| Component | Donor | Here |
|---|---|---|
| `gen-site.mjs` | 868 lines | **smaller, 450-600**; see the revision note below |
| Four guards | 628 lines | roughly 450, mostly adaptation and their tests |
| Config, workflow, section 3 items | - | small |

Call it **1,100 to 1,500 lines written or adapted.** Multi-week at this project's observed cadence.

> **Revised down 2026-09-20 after reading the donor in full, having first estimated "larger".** Four
> things shrink it, three of them measured rather than assumed:
>
> 1. **No YAML parsing.** `manifest.json` is already generated by `tools/gen-manifest.py` from
>    `templates/*/*_meta.yaml` and carries every per-bundle field the pages need (`id`, `title`,
>    `family`, `phase`, `doc_type`, `status`, `summary`, `tags`, `aliases`, `sizes_available`,
>    `approx_tokens`, `sizing_guidance`) plus a top-level `count`. The donor's ~60-line hand-rolled
>    frontmatter parser and its whole `classifySkill` fallback chain collapse into one `JSON.parse`.
>    The `count` field also satisfies AC-15 (no literal counts) for free.
> 2. **No route-manifest emission.** The donor emits none. Its `check-route-parity.mjs` reads a
>    **committed baseline** (`scripts/route-manifest.txt`, 428 lines, one route per line) snapshotted
>    from a finished build. Ours is snapshotted once after the first green build and committed.
> 3. **No remark plugin**, per the section 8 revision below.
> 4. **Role tabs are not in S0.** They appeared only in this table and in no acceptance criterion. They
>    force `.mdx` output, which brings JSX brace-escaping into pages that render templates full of
>    `{{placeholders}}`. Deferred to S1; S0 emits `.md` with `<details>` disclosure, which is what the
>    donor does for its own multi-artifact pages.
>
>    > **Item 4 was wrong, and it was wrong in the way this spec's own section 4 warns about: it
>    > reasoned about a build instead of running one.** Corrected 2026-09-20 when the generator was
>    > written. The hazard is real only for UNFENCED content, and templates are always fenced. The
>    > same excerpt was built both ways and the rendered bodies were **byte-identical but for
>    > whitespace**; across all 30 bundles the guides carry **zero** braces and zero tags, and the
>    > 1,907 tag-like strings in companions are `<a id="ref-N">` citation anchors, which MDX treats
>    > as intrinsic elements. So `.mdx` costs nothing, and S0 ships **`.mdx` with role tabs**, which
>    > also matches `spike-report.mdx`, the hand-built reference page the 2026-09-18 spike left in
>    > the tree. The deferral was removing a feature to avoid a cost that does not exist.

**Three pull requests, not one:**

1. **Skeleton** - the section 3 files that are not the generator, plus `dependabot.yml` and the
   `.gitattributes` pin. Small, reviewable, and it lands the decisions as files.
2. **Generator plus narrative pages** - the long pole. One coherent artifact by one author; this is the
   part that does **not** parallelise, and splitting it across agents produces an incoherent generator.
3. **Guards, `site.yml`, Pages live** - the three guard ports are independent files with independent
   fixtures, and this is the part that does parallelise.

---

## 8. What this spec deliberately does not do

- **The X-ray view and the lean/full diff.** S1. They are the signature, and they are not what "it
  exists" means.
- **`og:image`.** Clause 14.9 says a site SHOULD ship without it until the preset exists, rather than
  hand-roll a throwaway placeholder. Unlike the favicon it emits no reference, so its absence is a
  clean no-op.
- **`remark-resolve-links.mjs`. Decided 2026-09-20: skipped, and the condition this line waited on is
  now met.** The donor's link output is known - it emits relative `.md` links throughout
  (`[name](name.md)`, `](../skills/<group>/<name>.md)`), and its 178-line plugin exists to convert those
  into slug URLs at build time, inherited from three retired Python generators. Our generator is new and
  authors every link it emits, so it emits **base-absolute slug URLs directly** and the plugin is never
  needed. The hand-authored side is **verified clear**: the two tracked narrative pages
  (`site/src/content/docs/index.mdx` and `families/decision-docs.mdx`) contain zero relative `.md` links.
  One caveat remains, and it is smaller than the plugin: cross-bundle links living inside **template
  bodies** still need a rewrite pass of roughly 30-50 lines inside the generator, the analog of the
  donor's `rewriteInternalPaths`.
- **Migrating to the shared preset.** It does not exist. When it does, the migration is a dependency
  change, not a copy.
- **Any claim that a bundle helps anyone.** The gate proves structure and research integrity. Zero real
  fills stays zero on every surface.

---

## 9. Risks, stated honestly

| Risk | Mitigation |
|---|---|
| A ported guard that cannot fail | AC-12: every guard run against a broken fixture before being trusted. This repository shipped a self-test that skipped its only real assertion and printed OK for the life of a release (DF-7) |
| Counts on rendered pages drift | AC-15: nothing is a literal. This is DF-5, which has now recurred six times, applied before the surface exists rather than after |
| The conformance clause numbers move | Site-plan section 12 already flags them as provisional: the family Standard's Section 14 **has not landed**, and the pinned toolkit at `v1.10.0` carries sections 1 through 12 only. Re-check the table when it lands |
| Node rots unattended in a Python repository | Lockfile plus `npm ci` pins it; ADR 0051's Dependabot config surfaces bumps weekly |
| The site displaces other work | ADR 0047 removed the sequencing rule deliberately. This is the maintainer's call each time, not a gate |
