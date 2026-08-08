---
status: accepted
date: 2026-07-25
decision-makers: [jprisant]
consulted: [claude]
---

# Adopt a format axis: a bundle may ship a document in more than one shape, and the gate checks each

## TL;DR

- **Decision:** Adopt a format axis orthogonal to the existing size axis, via new optional metadata keys (`default_format`, `default_format_guidance`, `additional_formats`), so a bundle can ship a document as several structurally distinct shapes, each with a named source in circulation; adopted now for `product-vision` only (canvas, narrative, PR/FAQ), with the other 15 existing bundles left un-backfilled pending evidence from product-roadmap and product-strategy.
- **Why:** the product-vision research found four named formats that are siblings, not parent and child, so no ordering of them could satisfy the existing strict-nesting rule for sizes; shipping only the canvas would also have contradicted the field's most-cited authority (Cagan), who argues against a fill-in-the-blanks canvas approach.
- **Status:** accepted 2026-07-25, corrected twice in place before shipping (per ADR 0011, the correction procedure adopted with MADR v4, at 0011-madr-v4-at-docs-internal-decisions.md): on 2026-07-26 to require `default_format_guidance` whenever `additional_formats` is present (originally the default format alone carried no guidance sentence), and on 2026-07-27 to fix the backfill count from 18 bundles to 15.

The variant model ([ADR 0002](0002-variant-model.md)) gives a bundle exactly one axis of variation: **size**.
`lean` and `full` are the same document at two depths, and gate check C enforces that with a **strict
nesting** rule, `lean` H2s must be an ordered subset of `full`'s. That rule is not incidental. It is the
formal statement that the two files are parent and child.

Building `product-vision` (catalog 1, the first strategy-docs member) surfaced a document type where the real
variation is not size at all. The research fan-out found **four named formats in circulation**, and they are
siblings rather than parent and child:

| Shape | What it physically is | Named by |
|---|---|---|
| Canvas | a one-page grid of five labelled cells | Pichler, 2011 |
| Narrative | a few pages of prose, or a storyboard, or a prototype | Cagan |
| PR/FAQ | a press release dated years out, plus a Q and A | Amazon; originator unnamed in any source read |
| Positioning sentence | one long sentence | attributed to Moore, **unverified** |

A canvas cannot be turned into a press release by adding sections. You would discard the cells and start
writing. Neither file's outline is a subset of the other's, so **no ordering of the two satisfies check C**.
The library currently has no way to say "these are two shapes of the same document."

Three further facts made this worth deciding now rather than absorbing.

**The library has already been making this choice silently, fifteen times.** `adr` ships MADR and says
nothing about Nygard, Y-statements, or Tyree and Akerman. `test-plan` ships one shape from a field with
several. Every bundle so far has quietly picked a format and then called its depth variation "size."
product-vision does not introduce the problem; it is the first type where the silent default is
*uncomfortable*.

**It is uncomfortable because the field's most-cited authority attacks the shape we would otherwise pick.**
Cagan writes that you should not *"expect to find a simple fill-in-the-blanks, paint-by-numbers, canvas or
board approach to a strong product vision"*, while Pichler has shipped exactly such a board since 2011. Under
the status quo the library ships the canvas and apologises for it in prose. That is a weak position for a
library whose entire claim is honesty.

**And check A's stray detection has a gap that this work exposed.** The check rejects an undeclared variant
file, but only one matching a **known size token**, because it iterates `ALL_SIZES`. A file named
`product-vision_template-narrative-full.md` is invisible to it. Worse, `bundle_files()` iterates the same
list, so such a file would be skipped by every whole-bundle scan: dashes, citations, link resolution. The
comment above the stray check states a broader intent than the code implements.

## Decision Drivers

- **Model what is actually there.** Format and size are orthogonal: a canvas has a short and a long version,
  and so does a narrative.
- **Never ship a file the gate has not read.** The `bundle_files()` gap means a new file could enter a bundle
  unchecked. Whatever is decided, that closes.
- **Do not triple the remaining build.** 27 types times 3 formats is not buildable, so the decision needs a
  rule about when a format is worth shipping, not just a mechanism for declaring one.
- **Backward compatibility is nearly free here**, and worth taking: 15 bundles should not need a content
  change.
- **A capability may precede its subject.** D-C ([ADR 0023](0023-resolve-the-tier-1-family-taxonomy.md)) added
  set-valued axis support before any family used it, on the reasoning that the capability is correct whichever
  way the taxonomy lands and an unused code path costs nothing. The same logic applies here.

## Considered Options

- **Option A: one format per bundle, alternatives described in prose.** The status quo, made explicit.
  Rejected. It ships the library's highest-visibility family understating its own subject, and it leaves the
  Cagan objection answered with an apology rather than an artifact. It is, however, forward-compatible with
  the chosen option, which is why it was the fallback.
- **Option B: ship a single size and cover the rest in the companion.** Rejected for the same reason, plus it
  removes a worked long form from the type that needs one most.
- **Option C: one bundle per format** (`product-vision-board`, `product-vision-narrative`,
  `product-vision-prfaq`). Rejected. It breaks the document-type spine
  ([ADR 0005](0005-bundle-ids-doctype-spine.md)), under which a bundle id is a bare document-type handle and
  not a format handle. One catalog type would map to three bundles and 24 files, every bundle currently
  pointing at `product-vision` would have to choose which of the three to point at, and the
  `related_templates` graph roughly triples. It is also the only option that is expensive to reverse.
- **Option D: add a format axis.** Chosen.

## Decision Outcome

**Adopt a format axis, expressed in two new optional metadata keys, enforced by the existing gate.**

```yaml
sizes_available: [lean, full]   # unchanged meaning: the sizes of the DEFAULT format
default_format: canvas          # optional: names what the plain template files are
default_format_guidance: "..."  # when to reach for the default format
additional_formats:             # optional: further formats, shipped as further files
  - id: narrative
    sizes: [full]
    guidance: "when to reach for this one instead"
```

**Correction, 2026-07-26, before the first bundle shipped.** This decision originally paired
`default_format` with nothing, so every *additional* format carried a `guidance` sentence and the **default
format carried none**. An agent reading `manifest.json` would have been told when to use the narrative and
the PR/FAQ and nothing at all about the canvas, which is two options described out of three. The schema now
requires `default_format_guidance` whenever `additional_formats` is present, mirroring how `default_size` has
always been paired with `sizing_guidance`. Every format a bundle ships now carries exactly one guidance
sentence, and no format is described only by its absence from a list. Recorded here rather than silently
patched because the asymmetry was in the decision, not just the implementation.

**The default format keeps the plain filenames.** `<id>_template-lean.md` is the default format's lean
variant, exactly as today. Additional formats take a compound token, `<id>_template-<format>-<size>.md`. This
is the design choice that makes adoption cheap: migrating the other 15 bundles is **adding one key**, with no
file renames and no broken paths.

**Strict nesting moves inside a format.** For each format, its smaller variants must nest in its larger ones.
**No nesting relationship is required or checked between formats**, which is the entire point.

**`additional_formats` requires `default_format`.** If a bundle ships more than one shape, it must say which
shape the plain files are, or a reader cannot tell.

**The governing rule, without which this is unshippable:** a format is shipped only when it is **structurally
distinct** from the default **and** in circulation **with a named source**. Under that rule product-vision has
three, product-roadmap probably has two, and roughly twenty of the 27 Tier-1 types declare a `default_format`
and nothing else. A format that is merely a stylistic preference is a companion paragraph, not a file.

**On the word.** "Format" beat *form* (which in document-land means a thing you fill in, and every template
here is fillable), *shape* (which collides with `size_shapes` in check K's registry), and *genre* (precise but
tonally wrong for the audience). `output_formats` is **reserved** for file types, so the two senses never
collide.

**Adoption is incremental and deliberately narrow.** This ADR lands the capability and adopts it for
`product-vision` only. The other 15 bundles are **not** backfilled now. They will be backfilled once
`product-roadmap` and `product-strategy` have shown whether their format variation is as real as vision's,
which is the evidence that should drive a 27-type commitment rather than a single researched data point.

**Check A's stray detection is widened as part of this change.** It now rejects any
`<id>_template-*.md` the meta does not account for, rather than only files matching a known size token, and
`bundle_files()` returns the additional-format files so that every whole-bundle scan reads them. This closes
the gap described above, which existed before this ADR and would have persisted without it.

### Consequences

* Good: the library can, for the first time, show one document in several shapes. For product-vision that
  means the same worked Acme Analytics vision as a canvas, as a narrative, and as a PR/FAQ, which is the most
  instructive artifact this bundle can offer.
* Good: the Cagan objection is answered structurally. The library ships the canvas he criticises **and** the
  narrative he advocates, and the disagreement becomes a choice the reader makes with both in hand.
* Good: fifteen silent format choices become declarable. `adr` can say `default_format: madr`, which tells a
  reader what was picked and implies what was not, in the same spirit as `retrieval_status` in a research log.
* Good: a real gate gap closes. Files with an unrecognised token were previously unchecked by every scan.
* Good: `related_templates` is unaffected. A format is not a bundle, so the cross-link graph does not change,
  which was Option C's largest hidden cost.
* Neutral: two new keys are optional, so every existing bundle validates unchanged and the gate stays green
  through the capability landing.
* Bad, and the risk to watch: **format proliferation**. The governing rule above is the only thing standing
  between this decision and an unbuildable floor. If a future bundle ships a format that is a style
  preference rather than a structurally distinct artifact with a named source, the rule has failed and should
  be tightened, not quietly ignored.
* Bad: the manifest and atlas grow a dimension, and any consumer reading `sizes_available` alone now sees an
  incomplete picture of what a multi-format bundle ships.
* Bad, and stated plainly: **for as long as the backfill is deferred, the library is inconsistent in what it
  discloses.** product-vision will name its format; `adr` will not, despite having made the same kind of
  choice. That is a known interim, recorded here so it is not mistaken for an oversight.

### Confirmation

Enforced by `tools/check-bundles.py`, run in CI by `.github/workflows/ci.yml`, with branch protection on
`main` requiring the `gate` job. Specifically: check A derives every expected file from `sizes_available` plus
`additional_formats` and rejects any unaccounted `_template-*.md`; check C runs the nesting rule per format
and asserts nothing across formats; check J validates the two new keys and the `additional_formats` implies
`default_format` dependency.

Because the logic has branches no live bundle exercises yet (a bundle with two additional formats, a format
whose sizes differ from the default's, a stray compound-token file), it also gets **executable tests** per
[ADR 0025](0025-executable-tests-for-gate-logic.md), in `tools/test-check-formats.py`, run in CI and blocking
merge. `product-vision` is the first live confirmation.

## More Information

This extends [ADR 0002](0002-variant-model.md), which remains correct about what it decided: sizes are
`lean`/`full` with strict nesting and descriptive filenames. Nothing about the size axis changes. This ADR
adds a second, orthogonal axis alongside it and scopes the nesting rule to operate within a format rather
than across a bundle.

The trigger was the `product-vision` research fan-out, logged at
`templates/product-vision/product-vision_research-log.md`, which found the four shapes and the Cagan/Pichler
disagreement. (Named as a path rather than linked, because this decision lands before the bundle does and a
link would be dead until it arrives.) That log also records why the
positioning-sentence shape is **not** shipped as a format: the template attributed to Moore could not be
verified in any source read, and a positioning statement answers a different question than a vision does.
Three formats ship; the fourth is described in the companion with its attribution problem named.

The build order consequence is recorded in
[docs/internal/buildout-specs.md](../buildout-specs.md): the strategy-docs family is built with this
capability available, and the 15-bundle backfill is tracked there rather than assumed.

**Correction, 2026-07-27, before this record merged.** Three sentences above said the backfill covers
**18** bundles. It covers **15**: sixteen bundles exist once `product-vision` lands and `product-vision`
is the one that declares a format, so fifteen do not. The 18 came from counting directories under
`templates/`, which holds two that are not bundles (`_working` and `.impeccable`). Corrected in place
rather than left standing, because unlike the `default_format_guidance` correction above this was an
error in a count, not in the decision.
