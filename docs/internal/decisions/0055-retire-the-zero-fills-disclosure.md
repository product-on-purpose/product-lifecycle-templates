---
status: accepted
date: 2026-09-21
decision-makers: [jprisant]
consulted: [claude]
---

# Retire the zero-fills disclosure, and keep the ban on claiming a bundle is proven

## TL;DR

- **Decision.** This library **stops publishing a real-fill count** on any public surface, and stops
  requiring that it be published. The rule that a bundle stays `beta` "until one real usage cycle is
  recorded" becomes **`beta` until the maintainer judges it settled**, in all nine family contracts.
- **What is NOT retired, and this is the load-bearing half.** No page may call a bundle **proven**,
  **verified** or **validated**. That ban stays gate-enforced by `gen-site.mjs --check`, stays
  mutation-tested under AC-16, and every bundle stays `beta`.
- **The distinction the whole decision rests on:** declining to volunteer a negative number is a
  different act from asserting a positive one. Only the second would be a claim this library cannot
  support, and only the second is still forbidden.
- **No bundle is promoted.** All 30 remain `beta`. Removing a graduation *rule* is not the same as
  exercising it, and nothing here asserts any bundle is more mature than it was yesterday.
- **The earlier records are superseded, not rewritten.** [ADR 0039](0039-maintainer-discretion-replaces-the-pull-gate.md),
  [ADR 0043](0043-the-usage-gate-becomes-advisory.md) and
  [ADR 0047](0047-the-usage-precondition-leaves-the-language-too.md) each kept this disclosure
  standing. They keep saying so; a decision record is history, and history is not edited to agree with
  the present.
- **Status:** accepted 2026-09-21, at the maintainer's direction.

## Context and Problem Statement

Since `v0.1.0` this library has published a negative fact about itself on every public surface: that no
one outside the project had filled one of its templates for real work. Most recently that was a card on
the site's landing page, an `<Aside>` on all 30 generated bundle pages, a line on the bundle index, and
prose in `README.md`, `AGENTS.md` and `STATE.md`.

It was also a **requirement**, in four places: site-plan clause 13.4 ("Zero real fills is published as
zero. Not omitted, not softened, not rephrased as 'early'"), site-s0-spec AC-17, and the `status` row of
all nine family contracts, which gated `stable` on "one real usage cycle is recorded".

The maintainer has asked for the messaging and the requirement to be removed.

## Decision Drivers

- The disclosure is unusually scrupulous. Template libraries do not normally publish a usage count, and
  its absence is not a representation that usage exists.
- It had become the loudest thing on the landing page, competing with what the library is *for*.
- The graduation rule it enforced had never been exercised, and it made `stable` unreachable by any
  route the maintainer controlled, since it waited on a third party's behaviour.
- **A claim discipline and a disclosure obligation are different mechanisms** and were bundled together
  by history rather than by argument. They can be separated.

## Considered Options

1. **Retire the disclosure and the graduation rule; keep the claim ban.** Chosen.
2. **Retire everything, including the `proven` / `verified` / `validated` ban.** Rejected: that ban is
   what stops a page asserting something no evidence supports. Removing it would convert a decision
   about what to volunteer into a licence to overclaim, which is not what was asked for.
3. **Retire the public messaging, keep the graduation rule.** Rejected as incoherent: the rule's only
   observable effect was the disclosure, so keeping it would preserve the obligation while hiding it.
4. **Change nothing.** Rejected; it is the maintainer's call what their own project discloses.

## Decision Outcome

**Chosen: option 1.**

### Removed

| Surface | Was |
|---|---|
| Site landing page | A `<Card title="Zero real fills">` reading "No one outside this project has yet filled one of these templates for real work." Replaced with a card explaining what `beta` means |
| All 30 generated bundle pages | An `<Aside>` reading "Real-world fills recorded: **0**" |
| Bundle index page | "Real-world fills recorded: **0**" |
| `README.md`, `AGENTS.md`, `STATE.md` | Prose stating the count and the graduation standard |
| site-plan clause 13.4 | The requirement to publish it |
| site-s0-spec AC-17 | The same requirement, as an acceptance criterion |
| Nine family contracts | `status`: `beta` until one real usage cycle is recorded |

### Kept, deliberately

- **The `proven` / `verified` / `validated` ban**, enforced by `gen-site.mjs --check` between
  `astro build` and `upload-pages-artifact`, mutation-tested, and observed red.
- **Every bundle at `beta`.** Nothing is promoted by this record.
- **The "What this is not" section** on the landing page, and the equivalent passages in `AGENTS.md`:
  the gate proves structure and research integrity, never that a document helped anyone. That is a
  statement about what a *check* covers, not a fill count.
- **The eval record.** `evals/results/` is untouched. Four runs, three VOID, the fourth finding the
  probe gap at exactly 0.00, all still published in full.

### What replaces the graduation rule

`beta` to `stable` is now **the maintainer's judgement that a bundle has settled**. The previous rule
waited on an event outside the project's control, so in practice it was not a graduation path at all.

**The cost, named.** `stable` now rests on judgement rather than on an external signal, so it carries
less information than it used to promise. The mitigation is that it carries less *weight* too: the claim
ban means `stable` still cannot be presented as evidence that a bundle works.

### Consequences

- **A reader can no longer tell from the site how much real-world use these templates have had.** That
  is the direct effect of the decision and it should not be described as anything else.
- Nine family contracts change, and each requires a decision record for changes to itself. This record
  is that record for all nine.
- ADRs 0039, 0043 and 0047 each affirmed the disclosure. They are **superseded on this point and left
  unedited**, which is the house rule: a decision record says what was decided when, and a later record
  supersedes it.

## More Information

- The claim discipline that survives: [`site-plan.md`](../site-plan.md) section 13 clauses 1 to 3, and
  [`site-s0-spec.md`](../site-s0-spec.md) AC-16.
- What the gate actually proves: [`what-the-gate-proves.md`](../../explanation/what-the-gate-proves.md).
- The efficacy record, unchanged: [`evals/results/`](../../../evals/results/).
- **Addendum 2026-09-24, at the maintainer's direction.** The sweep in the Removed table missed live
  surfaces that still stated the fill count, or the old rule that a bundle graduates on a real usage
  cycle. They are now removed:
  - `.claude-plugin/plugin.json`'s description and the usage-report issue form;
  - `CONTRIBUTING.md` (twice), `what-the-gate-proves.md`, `filling-a-template.md`, the getting-started
    tutorial, the usage-log README and `pull-queue.md`;
  - internal status lines in `STATE.md`'s claim ledger, `plan-inventory.md`, `roadmap.md` (twice) and
    `tier2-specs.md`.

  Dated records are left as written, as this record left ADRs 0039, 0043 and 0047: released changelog
  sections, release notes, decision records, bundle history entries, eval results and dated briefs.
  The ban on calling a bundle proven, verified or validated is untouched.
