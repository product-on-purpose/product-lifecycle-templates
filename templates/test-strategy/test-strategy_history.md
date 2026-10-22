# test-strategy: history

Change log for the `test-strategy` bundle. Each entry records what changed and why, so a reader can tell a
correction from a preference.

## 0.1.0 - 2026-10-20

**Initial release.** Admitted on the 2026-10-12 admission sweep against the catalog entry `test-strategy`
(catalog 103 in `docs/internal/catalog.md`, atlas index 102 in `atlas/catalog-data.json`; issue #260);
specced 2026-10-19 in `tier2-specs.md`. `test-strategy_research-log.md` records 44 sources marked
fetched-and-verified and one marked not-retrieved and quarantined (ISO's own Online Browsing Platform
preview of ISO/IEC/IEEE 29119-3), with 291 lines in the log's Quotable lists, each checked against the
source's own raw text across three research passes: the 2026-10-12 admission sweep, a 2026-10-14
follow-up that recovered a lost research dimension, and a 2026-10-15 scope follow-up.

**The seventh `standing-standards` member, and the third this family's own forecast never named.**
[ADR 0075](../../docs/internal/decisions/0075-test-strategy-joins-standing-standards-as-a-foundation.md)
assigns `classification: foundation`, on the same marker-by-marker reasoning ADR 0053, ADR 0058, ADR 0062
and ADR 0071 used for the family's earlier members: this strategy is a standard a project's own test plan
is judged against or states a reasoned deviation from, not an instrument executed under time pressure.

### Single size, by the research rather than by default

`sizes_available: [lean]`. No source in either research dimension describes a short form and a long form
of a test strategy: Process Street's own steps, ISO/IEC/IEEE 29119-1's own content list, Ofgem's own
testing-scope structure and the catalog's own content note each describe one comprehensive shape. The
catalog's own `size_variant: "M"` marker is corrected in the same landing, independent of this build's own
meta.

### Scoped to an organization or program, the maintainer's ruling of 2026-10-15, never a portfolio

The 2026-10-14 family-fit follow-up found the scope question undecidable from admission evidence alone:
strong, direct, mostly primary evidence for a program-scoped strategy (Ofgem's two Switching Programme
documents, a UK smart-metering program strategy, the HNG-X Testing Strategy) against thinner,
mostly secondary evidence for a whole-organization reading. The maintainer ruled the type scoped to "an
organization or program... used across more than one project," after a further check found no source
anywhere in the research scopes the artefact itself to a portfolio; the one source using both words ties
the Test Strategy artefact to program scope and reserves "portfolio" for a separate, higher level. This
bundle builds only the organization-or-program sense, standing and consulted by more than one project; the
per-project sense is already shipped inside `test-plan`'s own Test Levels and Types and Risk-Ranked
Approach sections, and in its `test_strategy_ref` field, which this bundle is the forward reference for.

### ISO/IEC/IEEE 29119-3's own clause text was never read, and nothing here cites it directly

Every automated fetch of the standard's own current text (iso.org, IEEE Xplore, an iTeh mirror, an ANSI
preview page) returned a 403, a paywall, or a JS-rendered empty page across both research dimensions. Every
reference to the standard in this bundle is to a secondary account (Wikipedia's description of its Part 3
structure, ISTQB's current syllabus describing it) and is labelled as secondary. The syllabus also raises,
and this bundle does not resolve, a possible rename of the organization-level artefact inside the standard
itself; it is recorded as an open question in the companion rather than settled here.

### `pairs_with: []`, checked and confirmed empty rather than left empty by default

Checked against `product-on-purpose/pm-skills` `origin/main` on 2026-10-16: no pm-skills skill ID in
[`tools/known-skills.txt`](../../tools/known-skills.txt) produces or consumes this type.

### `related_templates: [test-plan]`

`test-plan` is the one sibling carrying an existing, unresolved forward reference to this type: its own
guide's "Plan, strategy, case, or report?" routing row points here before any bundle existed to receive it,
and its full-variant frontmatter already ships a `test_strategy_ref` field whose only job is to name a
standing strategy like this one, or to state that none exists.

### Alias corrections, checked rather than carried forward

**Added:** `organizational test strategy`, ISTQB's own term for this bundle's own sense, on a passing
quotation from both the official glossary's backing API and an unofficial mirror. **Dropped:**
`test approach`, which inside this library already names the per-project sense; `test-plan_guide.md`
states plainly that a project's own Risk-Ranked Approach section "is your strategy for this release," so a
reader typing "test approach" is more likely searching for that section than for this standing document.
**Not added:** `QA strategy`, which carries no passing or filed quotation in any of the three research
passes; nothing in the log supports it, so it is left off rather than added on the strength of a
plausible-sounding phrase. **Not added:** `master test plan` or `test policy`, each a distinct artefact in
ISTQB's own glossary, read and verified directly against the backing API in this bundle's own research.
