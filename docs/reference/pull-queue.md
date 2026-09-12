---
title: "The pull queue"
description: "How a request for an unbuilt type is weighed, the four states a catalog type can be in, and the live issue views"
audience: "both"
level: "beginner"
tags:
  - reference
  - pull-queue
  - governance
---

# The pull queue: how a request is weighed, and what it is not

This page states the rule, defines the four states a catalog type can be in, and links the live views.
**It is not a copy of the queue.** The queue is GitHub issues, and a committed mirror of it would go stale
on the next filed issue with nothing in this repository able to see that it had.

---

## Read this part first, because it is the part people get wrong

**A recorded request does not rank the queue, and a rank is not a schedule.**

The build order is set by **the maintainer's own preference and need** ([ADR 0041 (maintainer preference
sets the build order)](../internal/decisions/0041-maintainer-preference-sets-the-build-order.md),
2026-08-22). Requests are recorded, kept visible, and may be weighed as evidence that a type is wanted.
They do not set position, and their absence blocks nothing.

That is a deliberately unflattering thing to publish, and it is published because the alternative is worse.
The earlier rule ranked by pull count. **The queue has received zero issues since it shipped, and an input
that has never been non-zero cannot rank anything** - so a pull-ranked queue would have been a ranking
mechanism with no ranking input, which is a more elaborate way of saying "the maintainer decides" while
implying that you have a vote.

**A queued type is not a commitment.** If you read a position here as a delivery date, you are reading a
preference as a promise. This library has one credibility asset, which is that it does not claim what it
has not earned.

---

## The four states

Every one of the 205 catalog types carries a generated `state` in
[`atlas/catalog-data.json`](../../atlas/catalog-data.json). It is **derived from the tree** by
`tools/gen-atlas.py`, not hand-maintained, and CI fails on drift.

| State | Meaning |
|---|---|
| `built` | A bundle exists on disk. Derived from the directory being there, so it cannot be claimed |
| `candidate` | Eligible and **unranked**. Not queued, not scheduled, not refused. This is most of the catalog |
| `queued` | Recorded in `atlas/state-overrides.json` as something the maintainer intends to build. Still not a date |
| `out-of-scope` | Refused, with a reason. `wireframe` and `interactive-prototype`, per [ADR 0030](../internal/decisions/0030-templating-scope-markdown-documents.md): their artifacts are visual and executable, not documents |

**`candidate` means eligible and unranked, not queued.** The distinction is the whole point of the field:
before it existed, every unbuilt type looked identically undifferentiated, and a reader could not tell a
type nobody had considered from one that had been examined and refused.

**A bundle on disk outranks any override.** If a type has a directory, its state is `built` and a
conflicting override is a hard error, not a silent loss. That is why the state cannot drift into a claim.

---

## What is weighed, and what is not

1. **A request is recorded and stays visible. It does not itself change rank.** Named means attributable:
   a person or a team, not an anonymous vote. The maintainer may weigh a request as evidence that a type
   is wanted, and is not obliged to.
2. **The maintainer's own preference and need are the ranking criterion.** Each build carries a recorded
   one-line rationale ([ADR 0039 (maintainer discretion replaces the pull gate)](../internal/decisions/0039-maintainer-discretion-replaces-the-pull-gate.md)).
3. **The active-practice test is a quality bar on the build, not a trigger for it.** It applies whenever a
   Tier-2 methodology pack is built, using the methodology field from the request form as evidence. Failing
   it changes what gets built and how it is scoped, never whether the type could be considered.
4. **Tier-3 regulated is blocked, and it is the one rule here that is still a permission rule.** Not
   because nobody has asked, but because that tier carries an obligation this library has not committed to:
   regulation text must be re-verified at authoring time and on a cadence, forever. Decision D4 closed
   2026-08-14 as a deliberate no on that ground, and neither ADR 0039 nor ADR 0041 unblocks it, because
   both govern how build order is chosen and this tier is closed on a maintenance obligation instead.

> **One tension, stated rather than hidden.** D4 says Tier 3 "re-opens on a pull from a real regulated
> team", and a pull is exactly what ADR 0041 says does not govern the order. The reopening condition is
> written in a currency this page no longer ranks in. Restating it in preference terms is open.

---

## The one real pull, which was a self-pull

**`adr` is the standing example, and it is the maintainer's own.** It was built early because this
repository's governance needed decision records, not because anyone asked for it.

That is recorded here rather than in the catalog data, and the reason is worth a sentence: the spec that
designed this queue asked for `adr` to be seeded as `state: queued`. **By the time the state field shipped,
that had become impossible** - `state` is derived from disk, `adr` has a bundle, and an override
contradicting a built bundle is a hard error. Writing `queued` on a built type would have been a false
value in a generated file, which is the exact defect the field was added to remove. So the example lives on
this page, where it teaches the same thing without lying in the data.

**Under ADR 0041 a self-pull is the normal case rather than something needing a disclaimer.** An empty queue
that has never held anything teaches a reader nothing about how the queue works; one entry labelled
honestly teaches them exactly what counts.

---

## The live views

These are searches, not lists. They are what the queue actually is.

- [**New type requests**](https://github.com/product-on-purpose/product-lifecycle-templates/issues?q=is%3Aissue+label%3Anew-type) - `label:new-type`
- [**Usage reports**](https://github.com/product-on-purpose/product-lifecycle-templates/issues?q=is%3Aissue+label%3Ausage) - `label:usage`
- [**Corrections**](https://github.com/product-on-purpose/product-lifecycle-templates/issues?q=is%3Aissue+label%3Acorrection) - `label:correction`

**As of 2026-09-11 all three are empty**, and that is published rather than omitted. Zero requests is a
fact about this library's reach, not about the queue's design.

## Filing something

Use the [issue forms](https://github.com/product-on-purpose/product-lifecycle-templates/issues/new/choose).
Three exist, and they want different things:

- **Request a new document type.** It has to pass [ADR 0030](../internal/decisions/0030-templating-scope-markdown-documents.md)'s admission test: a named source must publish it as a **written document**. The form asks what you write *instead* today, and that field is required, because a request from someone who writes no such document is a preference and a request from someone who writes one badly is a pull.
- **Usage report.** The most valuable issue anyone can open here, and the rarest. Nothing in this library has been filled by anyone but its author.
- **Correction.** The fix rule is *delete the claim or label it honestly, never hunt for a citation that would justify it.* If a claim is unsupported, saying so **is** the fix.
