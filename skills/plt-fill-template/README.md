---
title: "plt-fill-template"
---

# `plt-fill-template`

The library's template-filling skill, and the first of its two. It teaches an agent to pick the right
template bundle for a job, fill it against that bundle's guidance, and grade the result on the bundle's own
rubric. For a document that already exists and was not filled from a template, the other skill is
[`plt-grade-doc`](../plt-grade-doc/). The skill is a thin
wrapper: the knowledge lives in the bundles under [`templates/`](../../templates/), and this file is how an
agent framework finds it.

The name matches this directory, which the
[Agent Skills specification](https://agentskills.io/specification) requires, and carries the library's
`plt-` prefix, which the Advanced Skill Library Standard requires at convergent tier. Both, and why the file
moved here from the repository root, are recorded in
[ADR 0036 (the library prefix and the skill's path)](../../docs/internal/decisions/0036-library-prefix-and-skill-under-skills.md).

## Inventory

- [`SKILL.md`](SKILL.md) - the skill definition an agent framework loads
