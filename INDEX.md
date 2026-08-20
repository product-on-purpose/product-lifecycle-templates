# INDEX - product-lifecycle-templates

> Generated from `library.json` + component frontmatter by `gen-index` and
> drift-checked (G4). Edit the source, not this file. Overview and positioning are
> in [`README.md`](README.md); agent guidance is in [`AGENTS.md`](AGENTS.md).

**Tier:** Gold (advanced). Standard 0.12. Version 0.3.1. Self-validating: `node scripts/check.mjs`.

## Components

### Skills (2)

- [`plt-fill-template`](skills/plt-fill-template/) - Selects and fills a researched product-document template from a 26-bundle library covering the full product lifecycle, then grades the result against that document type's own rubric. Use when writing a PRD, user stories, acceptance criteria, a risk register, a RAID log, a KPI dashboard definition, a test plan, a test case, a bug report, an ADR, an RFC, a software design document, a product vision, strategy, roadmap, OKRs, a business case, a user persona, a definition of done, a runbook, an incident postmortem, sprint retrospective notes, a status report, a product or sprint backlog, or release notes. Each bundle carries a lean and a full variant, a worked example, and the research log every claim traces to.
- [`plt-grade-doc`](skills/plt-grade-doc/) - Grades and reviews a product document that already exists against the researched rubric for its own document type, returning an itemized report card that quotes the document's own text as evidence, names the anti-patterns it hit, and lists the three fixes worth an hour. Use when someone asks for a review, a critique, a quality check, a second opinion, or a score on a PRD, user stories, acceptance criteria, an ADR, an RFC, a software design document, a test plan, a test case, a bug report, a risk register, a RAID log, a KPI dashboard definition, OKRs, a product vision, strategy or roadmap, a business case, a user persona, a definition of done, a runbook, an incident postmortem, retrospective notes, a status report, a backlog, or release notes.

### Subagents (0, Claude-only)

- none

### Commands (0)

- none

## Manifests

- [`library.json`](library.json) - authored canonical cross-agent manifest (the source of truth).
- [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) - Claude Code native manifest (generated; do not hand-edit).

## Documentation and governance

- [`README.md`](README.md) - overview, positioning, quickstart.
- [`CHANGELOG.md`](CHANGELOG.md) - full technical history; [`RELEASE-NOTES.md`](RELEASE-NOTES.md) - curated, user-facing notes.
- [`docs/`](docs/) - Diataxis docs (reference, how-to, explanation).
- [`docs/internal/decisions/`](docs/internal/decisions/) - ADRs.
- [`templates/`](templates/) - scaffolder templates.
