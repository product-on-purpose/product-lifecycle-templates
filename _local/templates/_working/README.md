# Template robustness: three treatments to compare

**Purpose.** Pick *how* the richer author guidance should live in the blank
`_template-*.md` files. You already chose the scope ("Templates + linking + methodology").
This working folder exists only to help you choose the guidance **style** before I roll
it across all four bundles. Nothing here ships. Delete `_working/` once you have decided.

## How to read this folder

Open each of these three files in a Markdown preview to feel how the guidance renders
(the difference between them is mostly invisible in raw source and obvious on render):

- [`approach-A_enriched-comments.md`](approach-A_enriched-comments.md)
- [`approach-B_visible-scaffolding.md`](approach-B_visible-scaffolding.md)
- [`approach-C_hybrid.md`](approach-C_hybrid.md)

Each contains the **same three PRD sections** (Summary, Problem, Functional requirements),
so only the style differs. Summary and Problem show the prose treatment; Functional
requirements shows the table treatment (per-field hints, priority legend).

## What all three add

Today each section gives the author one heading, one guidance comment (what / why /
one anti-pattern), and one placeholder. All three approaches below add the four devices
that best-in-class fill-in templates lean on hardest. They differ only in **where the
guidance sits** and **what survives render**.

1. **Strong-vs-weak contrast** (the single most instructive device)
2. **Guiding questions** to answer while writing
3. **A deep-link to the exact companion section** (not a generic "see the companion")
4. **Per-field hints** inside tables (what a good row looks like, priority legend)

---

## Approach A: enriched comments (clean shape)

All guidance lives in the HTML comment. The rendered page stays exactly as clean as it
is today. The author sees everything while editing raw Markdown; downstream readers of
the finished doc see none of it.

**Raw source (what the author edits):**

```markdown
## Summary

<!-- WHAT  One short paragraph: what this is and the single outcome it should produce.
           The whole idea, graspable before any detail.
     WHY   The summary is the triage surface; reviewers decide from it whether to read on.
           Deep dive: prd_companion.md, section 1 (Orientation) and section 3 (Anatomy > Summary).
     ASK   What is it? Who is it for? What single outcome does it produce?
     GOOD  "Saved Views lets an analyst capture a dashboard's filters as a named, reopenable
           view, so they spend time reading data, not rebuilding the lens to see it."
     WEAK  "We will add a Views menu with a dropdown and a save button." (mechanics, not outcome)
     TRAP  Describing the solution's mechanics instead of the outcome for the user. -->

{{summary}}
```

**Renders as (comment vanishes):**

```
Summary

{{summary}}
```

**Trade-offs.**
- Honors both locked conventions: "guidance vanishes on render" and "smallest useful
  default" (rendered shape is unchanged).
- Maximum guidance density with zero cost to the finished document.
- The companion deep-link is **not clickable** while it sits in a comment (it is a path
  the author reads, then navigates to by hand).
- An author who never opens the raw source (for example, pastes the rendered blank) sees
  no help. In practice you fill a template in an editor, where the comment is visible.

---

## Approach B: visible on-page scaffolding

The prompts and examples are visible blockquotes. Most obviously "robust" when rendered,
and the companion pointer is a real clickable link. The cost: the author must delete the
scaffolding before shipping, and it departs from the "guidance vanishes on render" rule.

**Raw source and render are the same (blockquote is visible until deleted):**

```markdown
## Summary

> **Fill in:** what is it, who is it for, and the single outcome it produces? One paragraph.
> **Strong:** "Saved Views lets an analyst capture a dashboard's filters as a named,
>   reopenable view, so they spend time reading data, not rebuilding the lens to see it."
> **Weak:** "We will add a Views menu with a dropdown and a save button." (mechanics, not outcome)
> **Why / deep dive:** [companion section 1 (Orientation)](prd_companion.md#1-orientation).
> _Delete this block before shipping._

{{summary}}
```

**Trade-offs.**
- Most visibly robust; help is impossible to miss; the deep-link is clickable.
- Departs from the locked "guidance vanishes on render" convention.
- The author must remember to delete every block, or the shipped doc carries scaffolding.
- The rendered blank is heavier, which pushes against "smallest useful default."

---

## Approach C: hybrid (one visible prompt line + rich comment)

One always-visible italic prompt line survives render as a nudge and carries the clickable
companion link. The heavier material (strong/weak, traps) stays in a hidden comment.

**Raw source (what the author edits):**

```markdown
## Summary

_What is it, who is it for, and the single outcome it produces? One short paragraph._
_Deep dive: [companion section 1 (Orientation)](prd_companion.md#1-orientation)._

<!-- GOOD "Saved Views lets an analyst capture a dashboard's filters as a named, reopenable
          view, so they spend time reading data, not rebuilding the lens to see it."
     WEAK "We will add a Views menu with a dropdown and a save button." (mechanics, not outcome)
     TRAP describing solution mechanics instead of the user outcome. -->

{{summary}}
```

**Renders as (italic prompt stays, comment vanishes):**

```
Summary

What is it, who is it for, and the single outcome it produces? One short paragraph.
Deep dive: companion section 1 (Orientation).

{{summary}}
```

**Trade-offs.**
- A middle ground: a light on-page nudge plus a clickable companion link, with the bulky
  guidance hidden.
- Partially departs from "guidance vanishes on render" (one line stays), but stays close
  to "smallest useful default."
- The author still deletes one line per section, but far less than approach B.

---

## The reference-linking fix (applies in every option)

Separate from the style choice above, all four companions get the same treatment. Today
there are 37 reference entries across the four companions and zero of them are clickable,
and every inline `[n]` is plain text.

**Before:**

```markdown
A PRD is a forcing function for shared understanding [7].

...

[7] Lenny Rachitsky. "Examples and templates of 1-Pagers and PRDs." Lenny's Newsletter.
https://www.lennysnewsletter.com/p/prds-1-pagers-examples (accessed 2026-06-30). [practitioner]
```

**After:**

```markdown
A PRD is a forcing function for shared understanding [[7]](#ref-7).

...

<a id="ref-7"></a>[7] Lenny Rachitsky. "[Examples and templates of 1-Pagers and PRDs](https://www.lennysnewsletter.com/p/prds-1-pagers-examples)."
Lenny's Newsletter (accessed 2026-06-30). [practitioner]
```

- Inline `[[7]](#ref-7)` renders as a clickable `[7]` that jumps to the entry.
- The reference title becomes the hyperlink; the bare URL is removed from the visible text.
- Each entry gets an `<a id="ref-n"></a>` anchor so the inline jump lands on it.
- Internal sources (the catalog `[internal]` entries) get an anchor and a relative path
  link where one exists, or stay plain if there is no linkable target.

---

## My recommendation

**Approach A**, for three reasons specific to this library:

1. It is the only option that keeps both locked methodology principles intact
   (guidance vanishes on render; smallest useful default). The other two require amending
   those principles, which then has to propagate through `methodology.md`.
2. A template is filled in an editor, where the comment is fully visible. The guidance is
   present at exactly the moment of writing and absent from the finished artifact, which
   is what you want.
3. It carries the most guidance per section with no render cost, so "much more robust"
   lands without making the blank shape heavier.

If your worry is that authors will not open the raw source, **Approach C** is the safe
compromise: it keeps the clean-ish shape but guarantees one visible nudge and a clickable
companion link per section. **Approach B** only wins if you specifically want the guidance
to be unmissable on the rendered page and accept editing the scaffolding out each time.

Pick one and I will apply it to all eight template files, fix the linking in all four
companions, and codify both the chosen style and the linking rule in `methodology.md`.
