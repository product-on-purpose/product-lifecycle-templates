# Research log: ADR bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Researched
2026-07-14. **Corrected the same day after an adversarial review; see [Corrections](#corrections).**

Reference numbers match the companion's [References](adr_companion.md#references) for rows 1-19.
Rows 20-22 are internal sources that inform the bundle but are not cited in the companion.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Nygard, "Documenting Architecture Decisions," Cognitect, 2011 | primary | **Fetched RAW 2026-07-14** (a first pass went through a summarizing pipeline and produced a bad quote; see Corrections) | Origin of the format; the five sections (Title, Context, Decision, Status, Consequences); the four status values (`proposed`, `accepted`, `deprecated`, `superseded`); "ADRs will be numbered sequentially and monotonically. Numbers will not be reused."; "The whole document should be one or two pages long. We will write each ADR as if it is a conversation with a future developer."; "All consequences should be listed here, not just the 'positive' ones."; the accept-blindly-or-change-blindly motivation |
| 2 | MADR v4.0.0: docs home, both template files, CHANGELOG (adr.github.io/madr, github.com/adr/madr) | practitioner | **Both templates fetched RAW and verbatim.** Docs home and CHANGELOG fetched | Exact section headings and heading levels for both templates; **that Considered Options is MANDATORY and that Decision Drivers, Consequences, Confirmation, Pros and Cons, and More Information are all optional**; that the minimal template carries **no frontmatter at all**, and that the full template's five frontmatter fields are marked collectively optional; the status enum incl. `rejected` and the `superseded by ADR-NNNN` form; the note that Confirmation "is included in many ADRs"; v1.0.0 2017-09-09, v3.0.0 2022-10-09, v4.0.0 2024-09-17; the "Architectural" to "Any" to "Architectural" rename; the "to strengthen the importance for decisions in software architecture work" phrasing, **which is from the docs home page, not the CHANGELOG**; maintainer Oliver Kopp |
| 3 | Fowler, "Architecture Decision Record," martinfowler.com | practitioner | Fetched, confirmed | Credits Nygard as origin; restates immutability (supersede, never reopen) |
| 4 | Tyree and Akerman, "Architecture Decisions: Demystifying Architecture," IEEE Software 22(2), 2005 | practitioner | **Paywalled. Primary text NOT read.** Bibliographic record via dblp; the 14-field count via a community reconstruction | The field *count* only, and only to make the qualitative point that the pre-Nygard template was heavy. **The companion does not enumerate the fields and quotes nothing from this paper** |
| 5 | Zdun, Capilla, Tran and Zimmermann, "Sustainable Architectural Design Decisions," IEEE Software 30(6), 2013 | practitioner | **Paywalled. Primary text NOT read.** Bibliographic record only | The Y-statement's publication venue and date, and nothing else. **The verbatim template wording is cited to [6], not to this** |
| 6 | Zimmermann, "Y-Statements," Medium / ozimmer.ch, 2020 | primary | **Re-fetched and re-verified 2026-07-14** after a review found the quoted wording was wrong (see Corrections) | The six clause connectives, verified literally: *in the context of / facing / we decided for / and neglected / to achieve / accepting that*. The only source the companion quotes the template from; "Y" is for "why"; SATURN 2012 first presentation |
| 7 | Zimmermann, "Architectural Decision Records: Any Decision Records?" ozimmer.ch, 2021 | primary | Fetched, confirmed | The "expand the scope" camp in the significance debate |
| 8 | Pureur and Bittner, "What Is the Purpose of Architectural Decision Records?" InfoQ | practitioner | Fetched, confirmed | The "restrict the scope" camp; scope bloat makes architecture harder to perceive; the responsibility-deflection / safety-in-numbers failure mode |
| 9 | Thoughtworks Technology Radar, Lightweight ADRs | practitioner | Fetched, confirmed | Entered Trial November 2016; now in Adopt; the store-in-source-control-not-a-wiki recommendation; that the *lightweight* form is what the industry adopted |
| 10 | Spotify Engineering, "When Should I Write an ADR?" 2020 | practitioner | Fetched, confirmed | Backfilling is legitimate; "up to each team to align on what defines" significance (the deflection position) |
| 11 | Dagdeviren, "ADRs and RFCs," candost.blog | practitioner | Fetched, confirmed | RFC requests input before deciding; ADR records a decision already made; RFC-then-ADR sequencing |
| 12 | ISO/IEC/IEEE 42010:2022 | primary | **Paywalled; iso.org returned 403. NOT read.** Scope established via the Wikipedia article (fetched) and search corroboration | That the standard requires architecture *rationale* including rejected alternatives, and that **no secondary source reports it mandating ADRs or using the term.** This is a claim about the secondary literature, not about the text, and the companion says so at the point of use |
| 13 | Dillon and Varanasi, "Context-Augmented Code Generation: How Product Context Improves AI Coding Agent Decision Compliance by 49%," arXiv 2605.08112 | **vendor** | **Abstract fetched raw 2026-07-14 and re-verified after review** | 8 tasks, 41 weighted decision points; augmented 95% vs baseline 46% decision compliance, a **49 percentage-point** delta; and the finding that actually matters: the baseline scored **100% on decisions visible in the codebase and 0-33% on decisions requiring context the code did not hold.** **The intervention is the authors' own commercial product-context retrieval system, NOT ADRs.** Supports no ADR-specific efficacy claim |
| 14 | Valmis, "How AI Coding Agents Use ADRs," Mneme HQ, 2026 | vendor | Fetched, confirmed | The machine-checkability framing ("an ADR nobody checks is a comment"). Conceptual only, no measured outcomes |
| 15 | Catio, "Architecture Decision Records" | vendor | **Search-corroborated only. NOT fetched** | The stale-status failure mode and the living-document deviation from immutability, **as corroboration only.** The companion states both in its own voice and quotes nothing from this source |
| 16 | Stride, "Should Engineers Write ADRs?" | practitioner | Fetched, confirmed | Whole-team authorship with a designated owner |
| 17 | AWS Architecture Blog, ADR best practices | vendor | **Search-corroborated only. NOT fetched** | Cross-repo discoverability tooling at organizational scale |
| 18 | adr organization, "ADR Tooling" (adr.github.io/adr-tooling) | practitioner | Fetched 2026-07-14; **re-read on review, which reversed what it supports** | Which tools support which format. **`adr-tools` (npryce) is Nygard-only.** Log4brains and adr-manager are MADR, but both target **MADR 2.1.2**, and nothing listed on the page tracks v4. This source is evidence that MADR's tooling ecosystem **lags the spec by two major versions**, i.e. it argues *against* the tooling case for v4, and the companion now says so |
| 19 | adr/madr issue 97, "Can ADRs replace design docs and RFCs?" | primary | Fetched, confirmed | An open, unresolved thread on the ADR-vs-RFC-vs-design-doc boundary, in the standard's own tracker |
| 20 | Master catalog entry 64 (Architecture Decision Record) | internal | On disk | Canonical sections, aliases, doc-type spine. **Its "S only" size call is overturned by this bundle; see below** |
| 21 | `develop-adr` skill, pm-skills (SKILL.md + references/TEMPLATE.md) | internal | On disk, read directly | The `pairs_with` target; its Nygard-format template, which is the divergence recorded below |
| 22 | Org decision-record convention: `jp-init-project`, and ADR 0011 in this repo | internal | On disk | `docs/internal/decisions/` + MADR v4 is the standard this template must produce records for |

## Findings that changed the bundle

**1. The catalog's "S only" size call for the ADR is wrong, and the evidence overturns it.**

Master catalog entry 64 classifies the ADR as single-size. MADR itself ships a *minimal* template and
a *full* template as separate files [2], which is the clearest available signal from the standard's
own maintainers that this type genuinely earns two weights. The bundle declares
`sizes_available: [lean, full]`.

Worth recording as a small independent validation of this library's own rules: MADR's minimal section
list turns out to be a **strict ordered subset** of its full one, with no adjustment. Two independent
projects arrived at the same nesting property, which is modest evidence that the nesting rule
describes something real about how documents grow rather than a convention this library invented.

**2. The paired skill and this template disagree on format. Reported, not patched.**

`pairs_with: [develop-adr]` resolves to a real skill in pm-skills, but its bundled template follows
**Nygard's** format [21], while this organization has standardized on **MADR v4** at
`docs/internal/decisions/` for its own decision records [22]. This template follows MADR, because a
template producing records that violate the adopting organization's own convention would manufacture
exactly the drift the library exists to prevent. The guide carries a one-to-one mapping table so the
two remain interoperable, and the divergence is left as a finding for the pm-skills maintainer rather
than silently patched from here. Both this and finding 1 are recorded as decision
[0012](../../docs/internal/decisions/0012-evidence-outranks-catalog-and-paired-skill.md).

**3. A widely repeated claim about ISO/IEC/IEEE 42010 is false, and the companion says so.**

The standard is frequently cited as mandating ADRs. It requires that architecture *rationale*
(including alternatives not chosen) be captured; no secondary source reports it prescribing a format
or using the term "ADR" [12]. The companion states this **and states that the text itself was not
read**, because citing a paywalled standard as authority for this template would be exactly the
appeal a careful reader would check and catch.

**4. MADR is no longer "Any Decision Records."** It renamed to "Any" in v3.0.0 (2022) and reverted to
"Markdown **Architectural** Decision Records" in the v4 line (2024) [2]. Much live blog content still
repeats the v3 name. The rename round-trip is itself the clearest artifact of the scope debate in
section 6 of the companion, so it is told as history rather than suppressed.

## Corrections

**2026-07-14, after an adversarial review of the first draft.** The review found errors of fact, not
merely thin sourcing, and they are named here rather than quietly patched. This log is part of the
product; a log that hides its own corrections is worth less than one that shows them.

| What was wrong | What is true |
|---|---|
| Ref 13 described as a **2025** study showing that supplying **ADRs** improved AI decision compliance **by roughly 49%**, tagged `[primary]`, logged as "fetched, confirmed" | The paper is **2026** (the arXiv ID `2605` encodes it). The intervention is the authors' **own commercial product-context system, not ADRs**. The 49 is a **percentage-point delta** (46% to 95%), not a relative gain. It is **vendor** evidence. Every clause of the original row was wrong |
| The MADR "strengthen the importance" quote attributed to the **v4.0.0 release note** | It is from the MADR **documentation home page**. (The rename itself *is* in the CHANGELOG, under 4.0.0-beta, 2024-09-02; it is only the quoted phrasing that is not) |
| **`adr-tools` cited as MADR tooling**, as one of three stated reasons for choosing MADR over Nygard | `adr-tools` is **Nygard-only** [18]. The claim argued against its own conclusion |
| **The first fix for that error introduced the same defect again.** `adr-tools` was swapped for "Log4brains and adr-manager," still cited to [18] as evidence that MADR has tooling | Those tools target **MADR 2.1.2**; nothing on [18] tracks v4. The citation still undercut the claim it was offered for. Tooling is **no longer given as a reason** to choose MADR; the companion now states the two-major-version lag as a real cost, and rests the choice on the maintained spec, the superset section set, and the org convention |
| Nygard quoted verbatim ("has a chance") from a source this log said was read only in summarized form | The page fetches raw perfectly well. **The hedge was the bug.** Nygard is now quoted exactly, from the raw text |
| The Y-statement quoted as *"facing the need to [X] ... and against [Y]"*, certified in this log as "the exact six-clause wording" | Neither clause is right. The template connectives are **"facing"** and **"and neglected"**; "the need to" was prose lifted out of the worked Web-shop example. Corrected against the raw source |
| **Considered Options described as one of MADR's *optional* additions** | It is **mandatory**, one of MADR's three required sections. The bundle contradicted itself: three other places (companion sections 4 and 5, and the guide) said so correctly |
| The lean/full frontmatter split attributed to MADR | MADR's minimal template has **no frontmatter at all**, and its full template marks all five fields optional. The split, and the requirement of `status`, are **this library's design**, and are now credited as such |
| Tyree and Akerman's fourteen fields **enumerated by name** from a paper the log says was never read | Cut to the field count, which is all the secondary reconstruction supports |
| The Y-statement's verbatim wording co-cited to paywalled, unread ref 5 | Cited to [6] alone, which is where the wording was actually read. Ref 5 now carries only the venue and date |
| "The acronym ADR does not appear in [ISO 42010]" stated flatly, from a standard never opened | Recast as a claim about what the secondary literature reports, with the non-retrieval stated at the point of use |
| Several universal claims about "the literature" ("nobody is publicly arguing...", "close to unanimous") | Recast as claims about **this bundle's search**, which is what a search can actually support |

Three lessons, and they generalize well past this bundle.

**1. The failure mode was not fabrication from nothing. It was transcription drift under
summarization.** Every bad claim had a real source behind it saying something adjacent to, but weaker
than, what got written down. Retrieval status in the table above is the control, and it only works if
the companion is held to it *clause by clause* rather than source by source. That check is human today
and has no automation, which makes it the strongest argument on the roadmap for citation-tracing in
the gate (WP-11).

**2. A hedge is not a substitute for a retrieval.** The log confessed that Nygard had been read only
in summary, and then the companion quoted him verbatim anyway. The right response to "I could not read
the source properly" is to go and read it, not to disclose the weakness and then rely on the source as
if the disclosure had fixed something. Honesty about a gap is not a licence to write across it. The raw
page fetched on the first try when someone finally tried.

**3. Fixing a citation defect is where the next citation defect gets introduced.** The first review
caught `adr-tools` being cited as MADR tooling. The fix swapped in Log4brains and adr-manager, cited to
the same page, and reproduced the identical defect in subtler form: that page shows those tools target
MADR **2.1.2**, so it still undercut the claim it was offered for. A correction written under the
relief of having been caught is not more reliable than the error it replaces, and it deserves the same
adversarial pass. It only got one because a second reviewer was sent to re-check the first reviewer's
fixes, and that is now the practice: **verify the corrections, not just the draft.**

## Notes and limitations

- **Three sources behind the IEEE/ISO paywall were not read**: Tyree and Akerman 2005 [4], Zdun et al.
  2013 [5], and ISO/IEC/IEEE 42010:2022 [12]. The companion quotes nothing from any of them, and states
  the non-retrieval where a reader meets the claim rather than only here.
- **Open lead on [4].** A free full-text copy of the Tyree and Akerman paper appears to be served from
  a university host. It was not retrieved here (the host presents an untrusted TLS certificate), but the
  claim this bundle makes from it (a fourteen-field template, cited only to establish that the
  pre-Nygard form was heavy) has been independently corroborated by counting the fields in the community
  reconstruction. **Reading the actual paper is the single cheapest upgrade available to this bundle**,
  and it should happen before the next `template_version`.
- **Nygard [1] is now raw-fetched**, and the quotations are exact. The earlier "read only in summary"
  limitation was retired rather than managed, which is the correct disposal of a hedge whose underlying
  gap is closeable in one request.
- **The one empirical claim in the bundle is vendor-run and does not test ADRs** [13]. It is reported
  with that caveat stated in-line, and it justifies no structural choice in the template. Confirmation
  is taught because MADR defines it and practitioners skip it, not because of this study.
- **Two sources are search-corroborated only** [15] [17], both vendor-tier, both used only for
  failure modes that other sources independently attest.
- **Sources encountered and deliberately not cited.** A Java Code Geeks piece (403-blocked) and a
  Neil Sherman post (search-corroborated only) both address the write-only-archive debate; the
  companion presents that debate's two camps without attributing them to named individuals, because
  the retrieval was too weak to put words in anyone's mouth. A Medium piece arguing that `AGENTS.md`
  is displacing the ADR was paywall-blocked; the companion notes the framing exists and says plainly
  that it could not retrieve the argument.
- **No empirical evidence was found, in either direction, on whether ADR collections stay usable at
  scale.** The searchability problem past a few hundred records is widely asserted and thinly
  evidenced. The companion says so rather than repeating the assertion as fact.
