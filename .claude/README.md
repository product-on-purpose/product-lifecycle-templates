# `.claude/` is maintainer-internal and does not ship

Nothing in this directory is part of the template library. It is the harness that **builds** the library,
and it is here for the maintainer and for agents working on this repository.

| Path | What it is |
|---|---|
| [`commands/build-bundle.md`](commands/build-bundle.md) | The slash command that drives one bundle end to end, per [`bundle-pipeline.md`](../docs/internal/bundle-pipeline.md) |
| [`workflows/build-bundle.js`](workflows/build-bundle.js) | The research and review fan-outs that command runs |

## Why it is a command and not a skill

**It used to be a skill, and that was a defect that shipped.** The first ever run of
`npx skills add product-on-purpose/product-lifecycle-templates` installed **two** skills, and the second was
this build harness, whose own description says it is not for library users. The `skills` CLI scans
`.claude/skills` deliberately, its skip list is hardcoded, and it reads no ignore file, so a skill cannot be
excluded in place.

Moving the harness to `commands/` makes it invisible to both the CLI and the Advanced Skill Library
Standard's component discovery. That is recorded in
[ADR 0037](../docs/internal/decisions/0037-keep-the-build-harness-off-the-published-skill-surface.md).

**The move is the small half.** [`tools/check-export-surface.py`](../tools/check-export-surface.py) is the
half that lasts: it fails CI whenever the set of skills an installer would export stops matching what
`library.json` declares, across all 31 prefixes the CLI scans. **If you add anything to this directory, that
check is what tells you whether you just leaked it to every installer.**

## The one rule for this directory

**Do not create `.claude/skills/`.** Anything placed there ships to users who ran `npx skills add`, whether
or not it was meant for them.
