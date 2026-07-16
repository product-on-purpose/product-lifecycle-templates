# Guide: Release Notes (operator card)

Fast reference for the Release Notes bundle. For the full reasoning, history, and sources, read
[`release-notes_companion.md`](release-notes_companion.md).

## When to use

- To tell users and stakeholders what changed in a release and what to do about it.
- At every release; even a small one gets an entry.
- When a release includes anything users must act on (new capability, breaking change, known issue).

## When NOT to use

- You need the permanent, complete, structured record of every change. Keep a changelog (Keep a
  Changelog format); derive the notes from it.
- You need a full launch plan and comms. Use a launch checklist and announcement; release notes are one
  input.

## Pick a variant

- **Lean** (default): the customer-facing announcement (Summary, New, Improved, Fixed) in plain,
  benefit-led language. For routine releases.
- **Full**: adds Highlights, Changed, Deprecated, Removed, Security, Breaking changes and upgrade notes,
  and Known issues. For major or breaking releases, or notes that double as the changelog entry. Grow
  lean into full by adding sections; never reorder the shared ones.

## Quality rubric (self-grade before publishing)

- [ ] Each entry leads with user benefit, in plain language, not implementation detail.
- [ ] Changes are grouped so a reader can scan to what matters.
- [ ] The summary says something specific, not "various improvements and bug fixes."
- [ ] Breaking changes are surfaced with a concrete upgrade path.
- [ ] Security-relevant fixes are called out separately, with severity.
- [ ] Known issues are listed honestly, with workarounds where they exist.
- [ ] The date is ISO 8601 (YYYY-MM-DD); the version follows a stated scheme (e.g. SemVer).
- [ ] All guidance comments deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **Git-log dump.** Pasting raw commit messages as notes.
2. **Written for the shipper.** Implementation language instead of user benefit.
3. **"Various improvements and bug fixes."** A summary that communicates nothing.
4. **Hidden breaking changes.** A breaking change with no flag and no upgrade path.
5. **Security buried in "Fixed."** A security fix with no separate visibility or severity.
6. **No known issues.** Omitting known problems so users hit them unprepared.
