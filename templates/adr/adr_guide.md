# Guide: ADR (operator card)

Fast reference for using the ADR bundle. For the full reasoning, history, and sources, read
[`adr_companion.md`](adr_companion.md).

## When to use

- A decision is **expensive or slow to reverse**: a persistence engine, a data model, a public API
  shape, an auth scheme, a language or framework, a hard dependency.
- Reasonable engineers **disagreed**, and the disagreement is worth preserving.
- A future reader will predictably ask **"why is it like this, and did they consider X?"**
- The decision **looks wrong from outside** but was deliberate. This is the highest-value record
  you will ever write.
- You are **backfilling** a decision made months ago that the team keeps re-litigating. Legitimate,
  and explicitly endorsed practice. Date it when the decision was *made*, and say it was
  reconstructed.

## When NOT to use

- **The decision is cheap to reverse.** Use the reversibility test, not a significance test: if
  undoing it next quarter costs an afternoon, it does not need a record. This is the single most
  useful filter, and skipping it is how a decisions directory fills with noise.
- **The decision has not been made yet.** You want an RFC or a design proposal. An RFC *requests
  input*; an ADR *records an outcome*. Run the RFC, then write the ADR when the call is made.
- **It is an implementation detail.** A variable name, a minor refactor, a library version bump.
- **It is already stated in a rulebook.** If your methodology or contributing guide already mandates
  it, an ADR restating it adds a second source of truth, which is worse than none.
- **You are writing it so nobody can be blamed later.** That is not a record, and everyone can tell.

## Pick a variant

- **Lean** (default, and it is not a compromise): the three sections MADR marks mandatory. Most
  decisions are recorded honestly in half a page. A short record that gets written beats a thorough
  one that does not.
- **Full**: when the decision is contested, crosses teams, carries regulatory or safety weight, or
  you expect to defend it to an auditor. Adds Decision Drivers, Confirmation, Pros and Cons of the
  Options, and More Information.

Grow lean into full by adding sections; never reorder the shared ones. The full variant is a strict
superset.

The scaling signal is the **contestedness of the decision**, not the importance of the system.

## Quality rubric (self-grade before you commit)

- [ ] The **title names the decision**, not the topic. A stranger scanning the folder knows what was
      chosen.
- [ ] The **context describes the situation, not the argument you won.** It was not written
      backwards from the conclusion.
- [ ] The context records **conditions that could stop being true**, so a future reader can tell
      whether the decision has expired.
- [ ] **"Do nothing" appears** in Considered Options, or its absence is deliberate.
- [ ] **No straw men.** Every option listed was genuinely on the table.
- [ ] The outcome is in **active voice** ("We will ..."), and a human being is named in
      `decision-makers`.
- [ ] There is at least one **real negative consequence**, and it is one someone would actually act
      on. "Small learning curve" does not count.
- [ ] The **chosen** option has honest cons listed, not just the rejected ones.
- [ ] (Full) **Decision Drivers exist and are falsifiable**: at least one option fails at least one
      driver. If every option passes every driver, the real reason is still unwritten.
- [ ] (Full) **Confirmation names a real check**, or honestly states that nothing enforces this.
- [ ] `status` is correct, and if this supersedes an earlier record, that record has been updated to
      point here.
- [ ] Filed at `docs/internal/decisions/NNNN-kebab-title.md` with a **fresh, never-reused number**.
- [ ] Every guidance comment deleted; no placeholders remain.

## Named anti-patterns (the usual wrecks)

1. **Approval theater.** Records written after the fact for decisions nobody contested, so the folder
   looks disciplined. They bury the records that matter.
2. **The CYA record.** Written to spread accountability rather than inform. The tells are passive
   voice and a `decision-makers` field that is either empty or lists the entire org chart.
3. **Decision without alternatives.** The most common substantive failure. The record cannot answer
   the only question it will ever be asked.
4. **Stale status.** A record still marked `accepted` for something ripped out two years ago is not
   merely useless; it actively misleads whoever finds it.
5. **Scope bloat.** Everything becomes an ADR, and the architecture gets *harder* to see. The
   artifact inverts its own purpose.
6. **All-upside consequences.** If the decision cost nothing, it was not a decision.
7. **The wiki.** Records stored anywhere but the repo are reliably records nobody reads.

## Coming from Nygard's format?

Every Nygard section maps into MADR without loss. You are not rewriting anything, you are renaming.

| Nygard (2011) | MADR (this template) |
|---|---|
| Title | Title (H1) |
| Status | `status` in YAML frontmatter |
| Context | Context and Problem Statement |
| Decision | Decision Outcome |
| Consequences | Consequences (under Decision Outcome) |
| *(not in Nygard)* | Considered Options, and the rest of the full variant |

The one substantive addition is that MADR makes **Considered Options** a mandatory section, where
Nygard's five sections have no dedicated home for the alternatives at all. Promoting them to a
required list of their own is the most useful thing MADR changed, because the alternatives are the
section teams silently drop, and a record without them cannot answer the only question it will ever
be asked. (That is this bundle's reading of the difference between the two formats, not a claim about
what Nygard intended.)

## Compatibility note: the `develop-adr` skill

This bundle's `pairs_with` is [`develop-adr`](https://github.com/product-on-purpose/pm-skills) in
pm-skills, which drafts an ADR interactively.

**Be aware that the two currently differ.** The skill's bundled template follows **Nygard's** format
(Status / Context / Decision / Consequences / Alternatives Considered / References). This bundle
follows **MADR v4**, which is the format the wider product-on-purpose organization has standardized
on for its own decision records, and which its project scaffolding expects at
`docs/internal/decisions/`.

Until they converge, use the mapping table above: content drafted by the skill transfers into this
template section for section. If you are recording a decision **inside a product-on-purpose
repository**, use this template, because it is the format the org's tooling and conventions expect.

*(This divergence was found while building this bundle, and it is logged as a finding for pm-skills
rather than silently patched. It is exactly the kind of drift a template library exists to surface.)*
