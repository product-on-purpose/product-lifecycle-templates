---
title: "{{product_name}} Product Vision"
product: "{{product_name}}"
owner: "{{who_owns_this_vision}}"
horizon: "{{target_year_or_range}}"
status: "{{draft_or_agreed}}"
last_updated: "{{date}}"
doc_type: product-vision
size: full
format: narrative
source_template: product-vision
source_template_version: 0.1.0
---

<!--
PRODUCT VISION, NARRATIVE FORMAT. Prose, two to four pages, written to be read start to finish rather than
scanned. This is a DIFFERENT DOCUMENT from product-vision_template-full.md, not a longer one: it shares none
of the canvas headings, and the gate deliberately asserts no nesting relationship between the two formats.

WHY THIS FORMAT EXISTS. The practitioner who has written most directly about the product vision, Marty
Cagan, argues explicitly against filling in a canvas for this job, on the grounds that a strong vision is a
work of persuasion closer to storytelling than to form-filling. The library ships the canvas anyway, because
a canvas is teachable and a canvas can be cited in an argument. It ships this too, because his objection is
a real one and the reader deserves the option he is actually advocating. See product-vision_companion.md
section 4 for the disagreement, stated in both parties' own words.

WHEN TO REACH FOR IT. When the vision has to make someone WANT the future rather than merely understand it:
a hiring conversation, a founding team, a board that has to fund years of work, a team that has lost the
thread. A canvas states a future. Prose can make someone believe it is worth their next three years.

RULES THAT MAKE THIS FORMAT WORK, AND THAT THE CANVAS DOES NOT NEED
1. WRITE IT IN THE PRESENT TENSE, FROM INSIDE THE FUTURE. Not "users will be able to", but "Priya opens the
   dashboard and sees". The tense is the technique; it forces concrete detail and exposes vagueness fast.
2. NAME A PERSON AND FOLLOW THEM. One named user living one specific hour is worth more than a paragraph
   about "customers". The single piece of evidence-backed advice in this subject is that vision language rich
   in concrete imagery is associated with better performance than language rich in abstract values, and that
   leaders tend to do the opposite. That finding studied leader RHETORIC rather than written documents and
   only its experimental half is causal, so treat it as a strong steer rather than a law; companion section 6.
3. NO BULLET LISTS, NO TABLES, NO HEADINGS BEYOND THE FIVE BELOW. The moment it becomes scannable it becomes
   a canvas with worse formatting. If you find yourself wanting a list, you are writing the other format.
4. NO FEATURE NAMES. A feature dates the document in two quarters and invites the reader to argue about the
   feature instead of the future.
5. IT MUST STILL BE ABLE TO REFUSE SOMETHING. Persuasion is not a licence for vagueness; the fourth section
   is not optional and is the test the canvas is also judged by.

HOW TO FILL THIS IN
1. Draft the first section in one sitting without stopping to edit. This form rewards a voice.
2. Read it aloud. Every sentence that is hard to say aloud is a sentence a reader will skim.
3. Replace each {{placeholder}} with your prose.
4. Before you share it: self-grade against product-vision_guide.md, then DELETE every HTML comment.
-->

# {{product_name}}: {{short_evocative_line}}

## Open in the Future

<!-- WHAT  Two or three paragraphs describing an ordinary hour in the world once this has worked, in the
           present tense, following one named person. Start in the middle of their day, not with context.
     WHY   This is the whole reason to choose this format. A reader who can picture the future argues about
           whether it is worth reaching; a reader given abstractions argues about the abstractions. The
           imagery-over-values finding applies most sharply here. Deep dive: product-vision_companion.md
           section 3 (The Vision) and section 4 (narrative format).
     ASK   What hour of whose day am I describing? What are they doing in the first sentence? What is
           present in this scene that does not exist today, and what is absent that exists today? Would a
           reader who knows nothing about us still picture it?
     GOOD  "It is a Tuesday and Priya, who runs fulfilment, wants to know why the north-east region slipped
           last week. She asks, in the same window where she noticed the problem, and has an answer before
           the thought has gone. She does not file a request. Nobody is waiting on Dev, who used to be the
           only person who could have told her, and who is now doing something harder and more interesting."
     WEAK  "In the future, our platform will empower business users to access insights seamlessly and drive
           data-informed decisions across the enterprise." (no person, no hour, nothing to picture, and it
           could describe any analytics product written in the last fifteen years)
     TRAP  Opening with the problem statement or the market. Those belong later. The scene has to land
           first, or the reader reads the rest as a pitch rather than a place. -->

{{open_in_the_future}}

## The People There

<!-- WHAT  Who this future is for, widened out from the one person in the opening scene, and what they need
           badly enough that they would change their habits for it. One or two paragraphs. Say plainly who
           it is not for.
     WHY   The scene establishes that the future is desirable; this establishes that it is desirable to a
           specific, findable group rather than to everyone in principle. A vision for everyone constrains
           nothing. Deep dive: product-vision_companion.md section 3 (Who It Is For, and What They Need).
     ASK   How many Priyas are there, and where do they work? What do they do today instead, and what does
           it cost them in time or in decisions not made? Who would read the opening scene and correctly
           conclude this is not for them?
     GOOD  "There are a few dozen Priyas in a company like hers and a few hundred thousand across the
           mid-market: people who own an operational number, are measured on it weekly, and cannot get at
           it without asking someone. This is not for professional analysts. They already have better tools
           than we will ever build, and they are not waiting on anyone."
     WEAK  "Our target users are business decision-makers who value data." (excludes nobody)
     TRAP  Sliding into persona documentation. This is a paragraph about people, not a spec sheet about
           segments; the persona document is a different artifact and lives elsewhere. -->

{{the_people_there}}

## Why This Falls to Us

<!-- WHAT  Why this team reaches that future when others have not, and why now rather than five years ago.
           One or two paragraphs of argument, not of credentials.
     WHY   Without this the narrative is a nice story about a future anyone could build, which gives the
           reader nothing to believe in beyond the writing. This is the section that turns a story into a
           bet. Deep dive: product-vision_companion.md section 3 (Why Us).
     ASK   What do we know or have that others do not? What changed recently that opens this? What could a
           well-funded competitor not simply copy next quarter? Why has nobody done it already, and is that
           reason going away?
     GOOD  "The reason nobody has done this is that answering a question in context requires already being
           in the context, and analytics tools have always started by copying the data somewhere else. We
           start from inside the operational systems, which is an accident of where we came from and the one
           thing a general-purpose competitor cannot adopt without becoming a different company."
     WEAK  "We have a world-class team, deep domain expertise, and a track record of execution." (a sentence
           available to anyone, and therefore evidence of nothing)
     TRAP  Reciting credentials instead of making an argument. Nobody has ever been persuaded of a future by
           a team's CVs; they are persuaded by a reason the future is reachable from here. -->

{{why_this_falls_to_us}}

## What We Are Not Doing

<!-- WHAT  The futures this one excludes, in prose. Two to four concrete refusals, at least one of which a
           reasonable colleague would argue for.
     WHY   THE NARRATIVE FORMAT IS JUDGED BY THE SAME TEST AS THE CANVAS: can this be used to refuse
           something? Prose makes it easier to be moving and easier to be vague, and this section is the
           guard against the second. A vision nobody has ever cited to say no is decoration in any format.
           Deep dive: product-vision_companion.md section 3 (What This Rules Out) and section 7.
     ASK   What has been proposed in the last year that this future says no to? What would we decline even
           if a large customer paid for it? If the answer is nothing, is the future above specific enough to
           be a destination at all?
     GOOD  "We are not building a query builder. Every conversation about this eventually produces someone
           asking for one, and every time we build one we are building for the analysts we just said this is
           not for. We are also not going after compliance reporting, which needs guarantees this future
           does not, and which would quietly turn us into an audit vendor over about two years."
     WEAK  "We will remain focused on our core mission and resist the temptation to do everything." (refuses
           nothing in particular and will never be quoted in a real argument)
     TRAP  Refusing only things nobody wanted. If every exclusion is comfortable, this section has made the
           document look disciplined without costing anything. -->

{{what_we_are_not_doing}}

## What Has to Be True

<!-- WHAT  The assumptions this future rests on that cannot yet be proven, and the horizon you are working
           to. One or two paragraphs, plainly stated, including the one that worries you most.
     WHY   Buying into an ambitious vision is unavoidably an act of faith: if it could be validated in
           advance it would not be ambitious. Saying so, and naming what would disprove it, is what makes
           this a considered bet rather than optimism, and it is what lets the vision be revisited honestly
           instead of defended. Deep dive: product-vision_companion.md section 3 (Leaps of Faith).
     ASK   What must be true about these people for this to matter to them? About the technology? About the
           market? Which of those is most likely to be wrong, and what would be the earliest cheap signal?
           By when do we expect this to be real?
     GOOD  "The bet that keeps me up is whether someone who did not derive an answer will act on it. Every
           part of this depends on that, and we will know early: if pilot users take the answer to Dev to
           check it, we have built a faster way to generate work for the analytics team. We are working to
           about three years, and reviewing this each October or sooner if that signal turns."
     WEAK  "There are of course risks and uncertainties, which we will manage as they arise." (names no
           assumption, so nothing can ever be shown to be wrong)
     TRAP  Listing only assumptions you are confident about. The section exists to expose the fragile one;
           a comfortable list makes the vision look examined without examining it. -->

{{what_has_to_be_true}}
