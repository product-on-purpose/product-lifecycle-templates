# Premortem: It Is July 2027 and the Library Failed. What Happened?

- **Date:** 2026-07-11
- **Method:** prospective hindsight. Assume failure one year out (abandoned, irrelevant, or credibility-damaged) and narrate the most probable causes, each with the early signal that would have been visible, a tripwire to install now, and the cheapest pre-commitment that prevents it. This complements the audit's risk register (likelihood x impact) with the thing registers miss: how failures actually unfold as stories.
- **Base rates worth respecting:** solo-maintainer content libraries fail overwhelmingly through abandonment, not through being wrong. The failure modes below are ordered by honest probability, not by drama.

---

## F1: The floor never got poured (probability: highest)

**The story.** The audit landed, the roadmap was admired, and then the interesting work called: a fifth bundle, a better atlas, a new brief. M0's one day of LICENSE, CI, tags, and ADR transcription kept losing to work that felt like progress. Six months later the repo still says Apache-2.0 without a grant, the plan still says Not started, and a would-be adopter's five-minute sniff test still fails. The library did not die; it just never opened.

**The pattern is already in evidence:** D2 sat 11 days at a 30-minute cost; the plan's progress table went stale within a week of the plan being written; the raising-the-ceiling brief itself was written *instead of* executing P1-P3. The project's revealed preference is thinking over flooring, and the thinking is genuinely good, which makes the trap comfortable.

**Early signal:** M0 not merged within 7 days of ratifying the roadmap.
**Tripwire:** put a literal calendar block ("M0: one day") in the next 5 working days; if it slips twice, the STATE.md gets a visible line: "credibility floor: NOT DONE, slipped twice."
**Pre-commitment:** the adoption kit in this package reduces M0's judgment work to review-only; the remaining excuse is one day of hands.

## F2: The wedge found no one (probability: high)

**The story.** LP-2 shipped and was good. Outreach (WP-33, five real PMs) never happened, because building is comfortable and asking people to try your thing is not. Zero external gradings by month three; the EV-3 log stayed empty; motivation decayed the way it always does when nothing external answers back; the repo's last commit aged past six months and the project quietly ended.

**Early signal:** WP-30 (build) done, WP-33 (outreach) log empty two weeks later.
**Tripwire:** WP-33's acceptance criterion is already written as "5 attempts logged," not "5 successes"; hold it.
**Pre-commitment:** name the five people now, before LP-2 exists. Writing five names in the pull-queue doc costs ten minutes and converts outreach from a decision into an errand.

## F3: The maintenance cliff (probability: medium, rises with success)

**The story.** Pulls arrived, bundles grew to 10-12, and the freshness automation (WP-26) was still on the roadmap because content always outranked plumbing. The first quarterly freshness pass was estimated at a weekend and skipped. A user found dead links and a superseded standard in a companion, posted about it, and the "researched, not remembered" claim inverted into the exact story the library existed to prevent. Trust, once the differentiator, became the vulnerability.

**Early signal:** bundle count grows twice without the link-check landing in CI.
**Tripwire:** hard rule from the resources doc: no bundle #6 before WP-26 (link-check) and the VL-3 cadence ADR exist.
**Pre-commitment:** the rule costs nothing to adopt today, everything to adopt after bundle #9.

## F4: The ecosystem moved and the metadata did not (probability: medium)

**The story.** In late 2026 the agent-skills ecosystem standardized a resource/template packaging shape (or MCP resource conventions consolidated). The library's metadata, invented in isolation, mapped awkwardly. D3, the one-hour spec read that would have caught the direction early, was never done (it was open 11 days at audit time and stayed open). Retrofitting 15 bundles cost a month that the solo maintainer did not have; the library stayed installable only by clone while the ecosystem's defaults routed elsewhere.

**Early signal:** D3 still open at the v0.2.0 tag.
**Tripwire:** D3 is in M1 (WP-12); treat its absence at tag time as a release blocker.
**Pre-commitment:** the machine-metadata spec's rule that every field is generated-or-schema'd makes any future remap a script, not a rewrite. Keep it.

## F5: The eval number backfired (probability: low-medium, high damage)

**The story.** The discrimination gap shipped as "+31 percent" with a naive protocol. A capable skeptic reran it with a strong generic control prompt and got +9, wrote it up, and the library's central "measured, not asserted" plank became "measured, misleadingly." The honest response (re-baseline, publish the correction) was executed, but the first impression was the durable one.

**Early signal:** any published gap without the held-out criteria, hollow-arm validation, and interval reporting.
**Tripwire:** [15_measurement-validity.md](15_measurement-validity.md) amendment list adopted into the spec before the first public number; the validation notes publish alongside the first scorecard.
**Pre-commitment:** already written; adoption is one decision.

## F6: The platform shifted under the artifact (probability: low-medium, slow-acting)

**The story.** Through 2027, AI-native prototyping and spec-driven agent workflows kept eroding "blank markdown template" as a category; the one-pager a PM fills by hand started reading as legacy craft. The library had the right raw materials to reposition (machine-readable intent contracts, rubrics as eval criteria, provenance) but the positioning never moved because the flagship companion never engaged the AI-era debate (content review CR-1), and by the time it did, fresher voices owned the conversation.

**Early signal:** the CR-1 section still absent from the PRD companion two quarters after the content review flagged it.
**Tripwire:** CR-1 is scheduled in the content-review revision plan; hold it there.
**Pre-commitment:** the reposition sentence is already latent in the library's own design ("the intent-and-constraints contract both humans and agents fill against"); writing it into the companion and README costs one research session.

## F7: The bus (probability: low, total impact)

**The story.** A life event took the maintainer's hours to zero for a quarter. Nothing was wrong with the project; there was simply nobody else who could run the cadence, and no kit that made it cheap for a future self or a capable agent session to resume cold.

**Early signal:** none; that is the nature of it.
**Pre-commitment:** the AG-3 authoring kit plus the ADR set plus STATE.md are the resume-cold package; they are already scheduled (WP-62, WP-04, WP-05). The premortem's only addition: keep STATE.md honest enough that a cold reader can find the next action in 60 seconds.

---

## What survives even in failure

Worth naming, because it changes the risk calculus: the methodology, the master catalog, the atlas, and the audit corpus are durable reference assets independent of adoption. If every adoption play fails, the project still produced the best-documented template-library *method* in the public domain, and that asset compounds into whatever comes next. The downside is bounded; the upside requires the floor, the wedge, and the cadence.

## The two-day insurance policy

F1, F2, and F4, the three most probable failures, are all prevented by roughly two days of scheduled, already-specified work: M0 (one day), the five outreach names (ten minutes), the D3 read (one hour), plus holding two rules (no bundle #6 before link-check; no public eval number before the validity amendments). Everything else in this package is upside; those two days are survival.
