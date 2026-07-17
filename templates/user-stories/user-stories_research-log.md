# Research log: User Stories bundle

Evidence trail for the companion, per the methodology's research protocol (§A6). Researched 2026-06-30.
**Citation integrity pass 2026-07-16 (WP-10): every reachable source fetched and verified against the
claims that cite it.** Corrections below.

## Sources consulted

| # | Source | Tier | Retrieval | Claims it supports |
|---|---|---|---|---|
| 1 | Kent Beck, *Extreme Programming Explained*, 1999 | primary | **Print book, no URL. Not retrieved**; cited from the book | User stories in XP's planning game. The *dated* history (C3 1997, book 1999) is sourced to [7], which was verified |
| 2 | Mike Cohn, "User Stories and User Story Examples," Mountain Goat Software | practitioner | **Fetched and verified 2026-07-16** | Verbatim: "As a < WHO >, I want < WHAT > so that < WHY >."; "every user story is a placeholder for a future conversation"; "Ron Jeffries named in 2001 with the wonderful alliteration of card, conversation, and confirmation". **Does NOT mention Connextra, Rachel Davies, XP, or the C3 project** |
| 3 | Ron Jeffries, "Essential XP: Card, Conversation, Confirmation," 2001 | practitioner | **Fetched and verified 2026-07-16** (same source verified for the acceptance-criteria bundle) | The three C's, verbatim: "User stories have three critical aspects. We can call these Card, Conversation, and Confirmation."; Confirmation as the acceptance test |
| 4 | Bill Wake, "INVEST in Good Stories, and SMART Tasks," XP123, 2003 | practitioner | **Fetched and verified 2026-07-16** | The INVEST letters; Testable, verbatim: "I understand what I want well enough that I *could* write a test for it." **Says stories are "at most a few person-weeks worth of work", NOT "one iteration". Defines Negotiable as "not an explicit contract for features; rather, details will be co-created", NOT "the path not the need"** |
| 5 | The XP team at Connextra, London, 2001 | practitioner | **No primary source online.** Origin and attribution cited from [7] | Origin of the "As a..." template |
| 6 | Alan Klement, "Replacing the User Story with the Job Story," jtbd.info, 2013 | practitioner | **NOT RETRIEVABLE from this environment: the jtbd.info domain times out (connection timeout, 2026-07-16), as does its root.** The article is live and indexed elsewhere, so this is an access failure, not a dead link. Never verified against source text | Job story format; the critique of user-story assumptions. **Corroborated from search excerpts and [11] only** |
| 7 | Wikipedia, "User story" | reference | **Fetched and verified 2026-07-16** | Verbatim dated history: "1997: Kent Beck introduces user stories at the Chrysler C3 project in Detroit."; "1999: Kent Beck published the first edition..."; "2001: The XP team at Connextra in London devised the user story format"; "Cohn names Rachel Davies as the inventor... she credits the team as a whole"; epic/theme/initiative hierarchy; Patton 2014 |
| 8 | Scrum Guide 2020 | primary | Verified (prior bundle); URL confirmed live 2026-07-16 | Stories as common Product Backlog items; format not mandated |
| 9 | Master catalog entry 30 (User Story) | internal | On disk | Canonical sections, aliases, relationships, S-only sizing note |
| 10 | Mike Cohn, *User Stories Applied*, 2004 | practitioner | **Print book, no URL. Not retrieved**; cited from the book | The book's role as standard reference; Cohn naming Rachel Davies (as recorded by [7]) |
| 11 | Intercom, "How we accidentally invented Job Stories" | practitioner | **Fetched, URL live 2026-07-16** | Job stories originating at Intercom |
| 12 | Jeff Patton, *User Story Mapping*, O'Reilly, 2014 | practitioner | **Print book, no URL. Not retrieved**; cited from the book | Story mapping as a narrative arrangement of stories |

## Corrections applied 2026-07-16 (WP-10 citation integrity pass)

This bundle had never had an adversarial citation pass; it predates the discipline. Seven defects, in
a bundle the gate had always passed green.

**A quote from a source that cannot be retrieved.** The companion presented the user story as
*"contains too many assumptions and doesn't acknowledge causality"* as Klement's exact words [6]. The
jtbd.info domain times out from this environment, so the quote could not be checked, and the wording
in search excerpts differs ("they contain... don't acknowledge"). **De-quoted to a paraphrase**, with
the retrieval failure stated in the reference itself. This is the ADR bundle's defect exactly:
verbatim quotation from a source never read at source.

**Four combined entries split.** Each bundled a retrievable source with an unretrievable one under a
single number, which is how the misattributions below survived:

| Old entry | Bundled | Now |
|---|---|---|
| [1] | Beck's 1999 book **and** the C3/1997 origin claim | [1] the book (print, labeled); dated history cited to [7] |
| [2] | Cohn's 2004 book **and** the Mountain Goat page | [2] the page (verified); [10] the book (print, labeled) |
| [6] | Klement's jtbd.info post **and** the Intercom blog | [6] Klement (unretrievable, labeled); [11] Intercom (live) |
| [7] | Wikipedia **and** Patton's 2014 book | [7] Wikipedia (verified); [12] Patton (print, labeled) |

**Misattributions the splits exposed:**

- **"Cohn credits Rachel Davies, who in turn credits the whole team"** was cited to the Mountain Goat
  page [2]. **That page never mentions Davies, Connextra, XP, or C3.** The claim is real but belongs to
  Cohn's book [10] and is recorded verbatim by Wikipedia [7]. Re-pointed.
- **"User Stories Applied (2004) generalized the practice"** cited [2], the *page*, for a claim about
  the *book*. Re-pointed to [10].
- **"Deliberately small: sized to fit inside one iteration"** cited Wake [4]. **Wake says no such
  thing**; his wording is "at most a few person-weeks worth of work. (Some teams restrict them to a
  few person-days of work.)" Rewritten to Wake's actual guidance, with the iteration framing labeled
  as the common working gloss.
- **"Negotiable does not mean the need is up for debate, only the path"** cited Wake [4]. Wake's
  actual definition is that a story "is not an explicit contract for features; rather, details will be
  co-created by the customer and programmer during development." The need/path reading is a
  reasonable gloss but is **this bundle's**, and now says so.

**This log was wrong too.** It claimed Jeffries' three C's and Wake's INVEST were corroborated but
that "primary URLs are cited but were not individually fetched." Both have now been fetched and
verified, and Wake's contradicted two claims made in his name.

## Notes and limitations

- **[6] Klement is the load-bearing source for the job-story debate and has never been read at
  source.** jtbd.info times out from this environment (the domain root too), so this is an access
  failure rather than a dead link; the article is live and indexed. Its claims rest on search excerpts
  and on [11] Intercom, which was reachable. A human on a different network should verify, or the
  claims should lean on [11].
- **Three print books ([1] Beck, [10] Cohn, [12] Patton) have no URL** and are cited from the books
  rather than retrieved. This is the book/pre-web format case WP-10e will codify in the methodology.
- **[5] Connextra has no primary source online at all**; its origin and attribution are cited from
  [7], which records both explicitly.
- One nuance not acted on: [7] records the original Connextra wording as "As a &lt;role&gt; I **can**
  &lt;capability&gt;, so that &lt;receive benefit&gt;", whereas the near-universal modern form (and
  this bundle's) uses "I **want**". The bundle teaches the modern form deliberately; the divergence is
  noted here rather than silently smoothed.
- No time-bound regulatory claims appear in this bundle.
