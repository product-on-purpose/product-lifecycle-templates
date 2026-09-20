---
status: accepted
date: 2026-09-20
decision-makers: [jprisant]
consulted: [claude]
---

# The site is a standalone property at the `github.io` path, not an umbrella section or a custom domain

## TL;DR

- **Decision, two parts.** The site is served at
  **`product-on-purpose.github.io/product-lifecycle-templates`**, and it **presents as "Product Lifecycle
  Templates" standing alone** rather than as a section of a Product on Purpose umbrella. `site` and
  `base` are set once in `astro.config.mjs` accordingly.
- **Why it needed recording at all:** the URL is the one part of the site that other people copy. It goes
  into `library.json`, the registry listing, the README, and eventually into whatever distribution venues
  this project submits to. A decision that other repositories will hold a copy of should not live only in
  a spec header.
- **Why standalone:** decision A-4 of the family site standard already chose **per-plugin sites** over one
  combined portal, on the grounds that each plugin is its own repository with its own release cadence.
  This is that decision applied, not a new one. Two of the three sibling sites already run this way.
- **The cost, named:** this is **not** the only pattern in the family. `thinking-framework-skills` serves
  from `thinking-framework-skills.productonpurpose.com`, so the family is genuinely split and choosing
  `github.io` means this project looks less branded than at least one sibling.
- **Why that cost is acceptable:** the move is **cheap and late-bindable**. GitHub Pages redirects the
  `github.io` URL once a custom domain is configured, so links published in the meantime keep working.
  This is one of the few decisions in the site track that is genuinely reversible.
- **Status:** accepted 2026-09-20. Decided by the maintainer; recorded by the agent.

## Context and Problem Statement

[`site-plan.md`](../site-plan.md) section 14 item 4 asks:

> **Naming and branding.** Does the site present as `product-lifecycle-templates`, or under a
> product-on-purpose umbrella? Affects the landing page and any future domain. Pure maintainer call, and
> not needed before S0.

The "not needed before S0" clause turned out to be **half right, and the wrong half was load-bearing.**
Branding is indeed not needed before S0. **The URL is**, because clause 14.7 requires `site` and `base` to
be set exactly once in `astro.config.mjs` and consumed everywhere else through `import.meta.env.BASE_URL`.
The skeleton could not be written without choosing.

So the item was one question in the plan and two questions in practice, and only one of them could wait.

### What the family actually does, which is not one thing

Checked directly on 2026-09-18 rather than assumed:

| Repository | Serves at |
|---|---|
| `pm-skills` | `product-on-purpose.github.io/pm-skills/` |
| `agent-skills-toolkit` | `product-on-purpose.github.io/agent-skills-toolkit/` |
| `thinking-framework-skills` | **`thinking-framework-skills.productonpurpose.com/`** |

There is **no `product-on-purpose.github.io` umbrella repository** - the org has no root Pages site to be
a section of. So "under an umbrella" was never a choice between two existing things; it would have meant
building an umbrella first.

## Decision Drivers

* **A-4 already decided the shape.** The family standard's decision A-4 chose per-plugin sites over one
  combined portal, because each plugin is its own repository with its own version and release cadence,
  and the shared preset captures the consistency benefit without cross-repo build coupling. A portal
  remains revisitable "purely as an aggregator".
* **Clause 14.7 forces the URL question early**, whatever the branding answer is.
* **The URL is the part other people copy.** Distribution submissions - still an ungranted maintainer
  decision - would publish it in third-party repositories, where a later change is not ours to make.
* **Reversibility is unusually good here** and worth spending, because almost nothing else in the site
  track is reversible.
* **One maintainer.** An umbrella is a second property to design, build and maintain.

## Considered Options

1. **`github.io` path, standalone branding.** What two of three siblings do.
2. **Custom subdomain now** (`templates.productonpurpose.com` or similar), standalone branding. What
   `thinking-framework-skills` does.
3. **Build a Product on Purpose umbrella site** and present this as a section of it.
4. **Defer**, and let the skeleton pick a placeholder.

## Decision Outcome

**Option 1.**

Option 3 is out on A-4: it is the portal that decision already rejected, and it would mean building a new
property before shipping the one that has content. It stays revisitable later as an aggregator, which is
what A-4 says it is.

Option 2 is defensible - a sibling does it - but it buys polish this project has not earned yet. **Zero
people outside the author have used this library.** A custom domain for a site nobody has visited is
effort spent on presentation ahead of substance, and the honesty rules in `site-plan.md` section 13 are
the same instinct applied to prose. It also costs DNS setup and a certificate wait before S0 can deploy.

Option 4 is the one that looked cheap and is not. A placeholder base path threaded through a generator,
guards and a route manifest is not a placeholder; it is the answer, chosen silently. **The skeleton had to
pick, so picking deliberately costs nothing over picking by default.**

### Consequences

Good:

* Conformant with A-4 by construction.
* Ships now. No DNS, no certificate wait, no second property.
* **Late-bindable.** GitHub Pages redirects `github.io` to a custom domain once configured, so a later
  move to `productonpurpose.com` does not strand published links. The change is a `CNAME`, two lines of
  `astro.config.mjs`, and a guard re-run.
* Matches the majority of the family, so a reader moving between sibling sites sees one pattern.

Bad, and stated plainly:

* **The family is split and this picks the less branded side.** A visitor comparing this site to
  `thinking-framework-skills` sees a bare `github.io` path against a real subdomain.
* **`base: '/product-lifecycle-templates'` is a long path segment** in every URL, and it is coupled to the
  repository name. Renaming the repository would move the site.
* **It defers a question rather than closing it forever.** A custom domain will look more attractive the
  moment anyone external actually reads this, and this record does not pre-approve that move.

### Confirmation

* `astro.config.mjs` carries `site: 'https://product-on-purpose.github.io'` and
  `base: '/product-lifecycle-templates'`, once, and nothing else restates them as consumed config
  (spec AC-5).
* GitHub Pages is enabled with `build_type: workflow`, reporting
  `html_url: https://product-on-purpose.github.io/product-lifecycle-templates/`.
* The built output contains no unprefixed internal `href`, verified 2026-09-18.
* Landing page `title` and Starlight `title` read "Product Lifecycle Templates" with no umbrella framing.

## More Information

* [`site-s0-spec.md`](../site-s0-spec.md) header, which recorded both calls before this record existed and
  is now superseded by it as the place they live.
* [`site-plan.md`](../site-plan.md) section 14 item 4, the open question this closes, and section 8.4, the
  base-path rule that forced the URL half early.
* [ADR 0046](0046-the-site-is-astro-starlight-under-pattern-s.md), which chose the stack and the location.
* `SITE-STANDARD.md` decision A-4 (per-plugin sites, portal revisitable as an aggregator) in
  `agent-plugins` at `standards/domains/astro-sites/`.
* **Re-open this record if** a custom domain is wanted for any sibling-wide reason, or if an umbrella
  property is ever built. Neither is blocked by this decision, and the redirect behaviour is what keeps
  the door open.
