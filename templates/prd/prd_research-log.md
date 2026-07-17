# Research log: PRD bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Kept with the
reference implementation to show the process; later bundles may fold this directly into the
companion's reference section. Researched 2026-06-30.
**Citation integrity pass 2026-07-16 (WP-10): sources re-fetched and claims checked against the actual
text.** Corrections below, including a wrong date and a quote that could never have been verified.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Scrum Guide 2020 (scrumguides.org) | primary | Fetched, verified; URL live 2026-07-16 | Three Scrum artifacts + three commitments; PRD is not a Scrum artifact; Product Backlog captures requirements |
| 2 | Cagan, "Revisiting the Product Spec," SVPG, **2006-10-12** | practitioner | **Fetched and verified 2026-07-16.** The prior 403 no longer reproduces | Prototype as the spec, verbatim: "But the majority of the product spec should be the high-fidelity prototype, representing the functional requirements, the information architecture, the interaction design, and the visual design of the user experience." **Dated 2006, not 2007** |
| 3 | Cagan, "How To Write a Good PRD," SVPG 2024 | practitioner | **URL confirmed live 2026-07-16** (prior 403 gone); **PDF body not read in this pass** | Cagan's evolved, current PRD position. Corroboration only; no claim rests on it alone |
| 4 | Cagan, "Discovery vs. Documentation," SVPG | practitioner | **URL confirmed live 2026-07-16**; **body not read claim by claim** | Spec-as-substitute-for-discovery caution. Corroboration only |
| 5 | Bryar & Carr, Amazon Working Backwards PR/FAQ (workingbackwards.com) | practitioner | Fetched, verified (2026-06-30) | PR/FAQ precedes the PRD; ~2004 origin; Kindle/Prime/AWS; press release as customer-value forcing function |
| 6 | Pragmatic Institute, "Writing the MRD" | practitioner | Search excerpt; **body not verified** | MRD-then-PRD waterfall lineage; why vs how vs what split; dozens-of-pages history |
| 7 | Lenny Rachitsky, "PRDs, 1-pagers, examples," Lenny's Newsletter | practitioner | **PAYWALLED. "This post is for paid subscribers"; body unreadable on 2026-06-30 and again 2026-07-16.** Never verified | Problem-first discipline; one-pager as default. **Nothing is quoted from it**, and its load-bearing claims were moved to [8] |
| 8 | "Lenny's Product Requirements template," Atlassian Confluence | vendor | **Fetched and verified 2026-07-16** | The freely readable rendering of the template whose source post [7] is paywalled. Sections: Description, Problem, Why, Success, Audience, then "What does this look like in the product?"; step one is "Crystallize the problem you are solving" |
| 9 | ProductPlan glossary, PRD | vendor | Fetched, verified | PRD definition and canonical components; waterfall-vs-agile usage note |
| 10 | Atlassian, "What is a PRD?" | vendor | Search excerpt (marketing shell on fetch); **body not verified** | Living-document, lightweight-agile framing |
| 11 | Figma, "How To Create a PRD" | vendor | Search excerpt; **body not verified** | Modern sections: goals/non-goals, success metrics, open questions; living document |
| 12 | Master catalog entry 29 (PRD) | internal | On disk | Canonical sections, aliases, relationships, Cagan caution, one-pager as S variant |

## Corrections applied 2026-07-16 (WP-10 citation integrity pass)

WP-10 named four defects in this bundle. **All four were real.** Re-checking found a fifth.

**A wrong date, and it was load-bearing.** The companion said "Cagan has argued since **2007**" and [2] was
dated 2007. The article is dated **October 12, 2006**. Corrected in both the prose and the reference.
This matters because the sentence is about the *longevity* of Cagan's position.

**The Cagan quote was never verified, and was verified only by luck.** This log previously said:
*"Quotes attributed to Cagan use wording confirmed across both the search excerpt and the catalog."*
A quote confirmed against a search excerpt and **this repository's own internal catalog** is not
confirmed at all: it is the ADR bundle's defect exactly. The page was re-fetched (the 403 no longer
reproduces) and the quote **is** verbatim. That is a lucky outcome, not a rigorous process, and the
process is what changed here.

**The Lenny quote could never have been verified.** The companion presented *"the single most
important step in solving any problem"* as Lenny Rachitsky's words [7]. **The post is paywalled**: the
page returns "This post is for paid subscribers" and the body is unreadable. Per WP-10's instruction
("de-quoted to paraphrase or verified via subscription"), it is **de-quoted**. Better: the claims it
carried were moved to **[8]**, Atlassian's freely readable rendering of the same template, which
states the problem-first structure plainly and can be checked by anyone.

**Refs 8 and 12 were uncited padding.** Both had zero inline citations, which the gate cannot catch:
check E fails an inline citation with no anchor, never an anchor with no citation (the reverse
direction is WP-11's job).

- **[8] is now cited**, and is the fix for the paywalled [7] rather than a decorative extra.
- **[12] Hustle Badger is removed.** It was uncited, and it 403s to fetch. WP-10 offered "cited or
  removed, ref 12 retagged"; inventing a citation to justify a reference is padding by another name,
  so it is removed and the catalog reference renumbered 13 -> 12 to leave no gap.

**SVPG entries gained retrieval qualifiers**, as WP-10 required. [2] is now fully verified. [3] (a PDF)
and [4] are confirmed live but **were not read in this pass**, and both now say so; they are cited as
corroboration only, and no claim rests on either alone.

## Notes and limitations

- **[7] Lenny is paywalled and stays cited but unverified.** Nothing is quoted from it and nothing
  rests on it alone; [8] carries the same claims accessibly. A subscriber could verify it; this pass
  could not.
- **Three sources are cited from search excerpts with unread bodies: [6] Pragmatic Institute, [10]
  Atlassian, [11] Figma.** They support convention and consensus framing rather than contested claims
  of fact, so the risk is low, but the labels now say so instead of implying verification.
- **[3] and [4] were not read**, only confirmed live. The position they corroborate is stated verbatim
  in [2], which was verified.
- Vendor sources ([8], [9], [10], [11]) are used for convention and modern-section consensus, not for
  contested claims of fact, per the citation standard.
- Recency: the Cagan position is stable (2006 to 2024). No time-bound regulatory claims appear in this
  bundle.
