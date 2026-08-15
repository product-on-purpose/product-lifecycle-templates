# Distribution plan: where this library can legitimately be listed, and in what order

Status: **plan, ready to execute, except that every submission is an outward-facing act and stops for the
maintainer.** Written 2026-08-14. Traces to roadmap WP-33 (wedge outreach), the one work package in
[`roadmap.md`](roadmap.md) that creates demand rather than capturing it.

**Every venue below was verified by fetching it**, not recalled. Star counts and last-push dates are as
observed on 2026-08-14 and will drift; the policy quotes are verbatim from the named file. Re-check both
before acting on any row.

<!-- counts: bundles=26 -->

---

## 1. The finding that sets the order

The largest and best-fitting venue in this space states, in its own `CONTRIBUTING.md`, that the sequencing
most projects use is wrong:

> "Too many people think like this: (i) Build something awesome; (ii) Submit to Awesome Claude Code;
> (iii) Get accepted, because of being awesome; (iv) Get users. However, a more likely chain of events is:
> (i) Build something awesome; (ii) Get users; (iii) Submit it to Awesome Claude Code, or just focus on the
> project, and I'll notice it if it gathers enough interest. **If 'getting on the list' is any part of a
> promotional strategy for your project, you should be prepared to have a backup plan.**"
>
> `hesreallyhim/awesome-claude-code`, `CONTRIBUTING.md`

**Take this at face value.** It is not a rule that can be satisfied by writing a better submission; it is the
reviewer telling you what they will be thinking when they read one. It does not forbid submitting, and this
library **does** clear that list's written eligibility bar (section 3). It means listings are a poor primary
strategy and a reasonable secondary one.

**Self-promotion is never banned and always discounted.** Across eight lists whose contributing files were
read in full, not one prohibits submitting your own project, and several name it explicitly:

| List | Verbatim |
|---|---|
| `akullpp/awesome-java` | "Self-promotion is frowned upon and viewed critically, but your suggestion will of course be approved if the criteria match" |
| `dend/awesome-product-management` | "This list is not for self-promotion - posting links to your own articles is generally frowned upon" |
| `ziadoz/awesome-php` | A checklist item you must affirm: "Your pull request isn't for self promotion purposes" |

The operative consequence: **a self-submission is read more skeptically and its wording is scanned for sales
language.** That is why section 6 fixes the copy before section 3 sends anything.

## 2. What the research actually found about the two ecosystems

**The product-management world has almost no live surface.** Four "awesome-product-management" lists were
found last pushed between 2019 and 2023. The one live general PM list forbids self-promotion. No maintained
`awesome-adr` exists in any form. No PM newsletter, community, or "toolbox" directory was found with a
public, non-gated submission mechanism.

**The Claude and agent-skills ecosystem is young, active, and mostly ungated.** Several lists with five-figure
star counts were pushed within days of the check, and the ones with a stated maturity bar frame it as
*age-plus-activity **or** stars*, never stars alone. That distinction is what makes this library eligible
today at one star.

## 3. Tier 1: sanctioned, no social-proof gate, do these first

### 1.1 The official plugin submission form

**Venue:** `platform.claude.com/plugins/submit`, which feeds `anthropics/claude-plugins-community`
(349 stars, synced nightly). This is the mechanism by which a third-party plugin becomes installable via
`/plugin install`.

**Why first:** it is the only channel here that puts the library **where a user already is** rather than on a
page they must find. It is also the only one with **no stated minimum stars, age, or user count** anywhere in
its documented criteria. The gates are `claude plugin validate` passing and an automated security scan.

**Prerequisite:** run `claude plugin validate ./` locally and fix anything it reports. Do not submit before
it passes; the review pipeline runs the same check.

**Note:** `anthropics/claude-plugins-official` is a **different** repository with **no application process**.
Anthropic curates it at its own discretion and the submission form does not feed it. Do not attempt it.

### 1.2 `BehiSecc/awesome-claude-skills`

9,960 stars, last pushed 2026-08-02. **The best category match found anywhere in this research:** it carries
a dedicated **"Collaboration and Project Management"** category, rather than requiring this library to squeeze
into "Productivity" or "Other".

Submission is fork-and-PR or an issue, documented inline in the README in three lines. No stated maturity,
star, or usage bar, so the zero-users caveat is not disqualifying by their own rules.

### 1.3 `pengqun/awesome-documentation`, as several scoped submissions

157 stars, last pushed 2026-06-20, with an active lint CI workflow. Explicitly a list of documentation
**templates**, and it already carries subsections this library maps onto: PRD, RFC, and Test Plan / Test Case
/ Test Report.

**Its rules suit this library better than a repo link would.** From its `CONTRIBUTING.md`:

> "Try to fit your item into an existing section. Open a suggestion to start a discussion about any new
> sections. Make an individual pull request for each suggestion."

So this is **not** one link to the library. It is one PR per document type into the subsection that already
exists, and a discussion issue first for anything without a home. That is more work and a better fit: each
bundle is a standalone researched artifact with its own sources and worked example, so it survives being
judged alone. A single "here is my 26-template repository" link asks a maintainer to evaluate a monolith on
trust.

**Mechanical prerequisite:** the repository requires `pre-commit` installed locally before committing.

**Start with one**, not five. Send the strongest single bundle, see whether it lands, and only then send the
rest. Five simultaneous PRs from a stranger is the shape that reads as a campaign.

## 4. Tier 2: eligible by the written rule, discounted by the reviewer

### `hesreallyhim/awesome-claude-code`

52,325 stars, pushed the day it was checked. The flagship list in this ecosystem.

**This library clears the written bar.** From its `CONTRIBUTING.md`:

> "Any resource that is recommended must either: (i) Be at least 14 days old (14 days since first commit on
> default branch) AND show signs of active development ... OR (ii) Have at least 100 stars."

The repository was created 2026-06-30 and has committed continuously since, so it clears branch (i) outright
and **the single star is irrelevant to eligibility**.

**Three mechanics that will get a submission rejected if missed:**

1. **Issue form only.** "ALL RECOMMENDATIONS MUST BE MADE USING THE WEB UI ISSUE FORM TEMPLATE ... Do not
   open a PR." Opening a PR risks a temporary block.
2. **One resource per submission.** "You may not recommend more than one resource at a time."
3. **Description, not pitch.** "Resource descriptions should be written as descriptions, not a sales pitch.
   Don't address the reader ... Don't use any emojis."

**Why this is Tier 2 rather than Tier 1**, despite being the biggest and most eligible: the same file carries
the get-users-first paragraph quoted in section 1. Submitting is permitted and honest. Expecting it to
produce users is the error the maintainer is warning about.

### `dastergon/awesome-sre`, one narrow link only

13,437 stars. Only its Post-Mortem subsection is relevant, and only to `incident-postmortem` and `runbook`.
It already links a comparable single-purpose postmortem-templates repository, which is the precedent. Pitching
anything broader to an SRE audience reads as off-topic.

## 5. Tier 3: do not submit, with reasons

| Venue | Why not |
|---|---|
| `VoltAgent/awesome-agent-skills` (30,301 stars) | **Stated bar this library fails today.** Verbatim: "Skill must have real community usage. We focus on community-adopted, proven skills. Brand new skills that were just created are not accepted. Give your skill time to mature and gain users before submitting." Submitting now signals not having read the guide. **Revisit after real adoption** |
| `anthropics/claude-plugins-official` (33,534 stars) | No application process. Anthropic's discretion; the submission form does not feed it |
| `dend/awesome-product-management` (2,309 stars) | Forbids self-promotion, has no Templates category at all, and carries a large PR backlog |
| `punkpeye/awesome-mcp-servers` (92,336 stars) | Out of category. This library ships no MCP server |
| `skillsdirectory.com` | **Integrity concern.** Claims 97,030 indexed skills with no visible ownership, "Coming Soon" placeholders in featured slots, and an inconsistent copyright year. Not a real curation surface |
| Four dead PM lists | Last pushed 2019, 2019, 2021, 2023. Star count does not make a dead list worth a submission |

### Already true, requiring no submission

`npx skills add product-on-purpose/product-lifecycle-templates` works against any public repository
containing a `SKILL.md`, which this one has. **There is nothing to submit for that channel; it already
works.** Note the separate defect recorded in `STATE.md`: that route installs the skill without the bundles,
so it is reachable and thin.

## 6. The submission text, and why it is the load-bearing part

Three lists independently demand a plain description rather than a pitch, and self-submissions get their
wording scanned. **The copy is also a claim about the library, so `STATE.md`'s honesty discipline governs
it.** This is not a marketing decision.

**Proposed one-liner**, reusable across venues:

> A library of 26 product-management document templates, each shipping with a researched companion that
> cites its sources, a worked example, and machine-readable metadata.

It is descriptive, carries no emoji, does not address the reader, and every clause is verifiable by opening
the repository. It claims nothing about adoption, quality, or outcomes.

**What must not appear in a submission**, because the library cannot support it: "best-in-class", "proven",
"trusted by", any adoption number, and any efficacy claim. The efficacy evaluation returned **VOID** twice.
The README's own `real fills: 0 (honest)` badge is the standard the copy has to meet.

**The tension worth deciding deliberately.** That badge is the most on-brand element in the repository and it
is a visible "nobody uses this" signal on the page a list maintainer reviews. It will cost some acceptances.
Removing it would buy them back by abandoning the thing that makes the library worth finding. **Recommendation:
keep it.** Recorded here so the trade is made on purpose rather than discovered in a rejection.

## 7. Repository preparation

Verified present: description, 16 topics, Apache-2.0 in a root `LICENSE`, five tagged releases, issues
enabled with three templates, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, and a README with a
quick start. GitHub already serves an auto-generated Open Graph card.

**The repository is submission-ready. Its weakness is one star and forty-five days of age, and no amount of
polish fixes either.**

Two cheap gaps:

1. **Topics are missing this ecosystem's vocabulary.** The current 16 are PM-facing (`prd`, `adr`, `sdlc`,
   `product-management`). For comparison, `awesome-claude-code` itself carries `claude-code`, `anthropic`,
   `agent-skills`, and `claude`. Adding `claude-code`, `anthropic`, and `agent-skills` costs nothing, stays
   under GitHub's 20-topic cap, and puts the repository on the topic pages where this ecosystem browses.
2. **`homepage` is unset.** That is the slot a docs site would occupy if the site track ever ships.

## 8. What an agent can do, and what stops for the maintainer

**An agent can:** run `claude plugin validate`, draft every submission body against the copy rules in
section 6, verify each venue is still alive and its policy unchanged, prepare the per-type PR branches for
`awesome-documentation`, and add repository topics.

**Every act of submission stops for the maintainer.** Each one opens an issue or a pull request on another
person's repository, under this project's name, and is not cleanly reversible. That is the same boundary
`decision-procedures.md` draws around anything the library claims about itself.

## 9. Honest limits of this plan

**None of this creates users.** Every venue here is a listing. A listing is a chance to be found by someone
already browsing that list, which is a much weaker event than a person deciding to fill a template. The
roadmap's own framing is right: WP-33 is outreach, and outreach means named people, which no directory
substitutes for.

**Expect silence.** `awesome-claude-code` states plainly that there is "no formal submission/review process"
and that recommendations are reviewed best-effort with no guaranteed response. A submission that is never
answered is the normal outcome, not a failure to diagnose.

**The measurement problem is unsolved.** Nothing here tells you which listing, if any, produced a visitor.
GitHub traffic data is the only instrument available and it is coarse. Do not build a story about which
channel worked from stars alone.

**If this plan is executed in full and produces nothing, that is information**, and it points the same
direction the roadmap already does: the wedge (WP-30, LP-2 grade-my-doc) gives someone a reason to arrive.
Listings only tell them where the door is.
