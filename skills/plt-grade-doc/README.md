---
title: "plt-grade-doc"
---

# `plt-grade-doc`

The library's second skill, and the first one that is worth something to a person who has not adopted the
library. It takes a product document that already exists and grades it against that document type's own
researched rubric, returning an itemized report card with the document's own text quoted as evidence.

[`plt-fill-template`](../plt-fill-template/) runs template to document. This runs document to rubric. The
knowledge lives in the bundles under [`templates/`](../../templates/); this skill is the reading of them.

The name matches this directory, which the
[Agent Skills specification](https://agentskills.io/specification) requires, and carries the library's
`plt-` prefix, which the Advanced Skill Library Standard requires at convergent tier. Both are recorded in
[ADR 0036 (the library prefix and the skill's path)](../../docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md).
The build spec this skill implements calls it `grade-doc`; the spec predates that ADR, and the deviation is
stated in `SKILL.md` rather than left for a reader to notice.

## Inventory

- [`SKILL.md`](SKILL.md) - the skill definition an agent framework loads
- [`references/`](references/) - the report card format, the detailed grading procedure, the EV-3 feedback
  form, and a real report card from the first run. Loaded on demand, not up front
