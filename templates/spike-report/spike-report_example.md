---
title: "Over-the-air updates fit the overnight window, and today's bootloader cannot survive one that fails"
spike_id: "SPK-2026-014"
status: "complete"
conducted_by: ["Hana Okafor, Firmware (hana.okafor@riverlandsensing.example)"]
date: "2026-09-04"
work_item: "OPS-1187, Can deployed catchment nodes be updated over the air?"
doc_type: spike-report
size: lean
source_template: spike-report
source_template_version: 0.1.0
---

> **Worked example.** A filled `spike-report` for a four-day technical investigation at Riverland Sensing,
> a fictional operator of water-quality monitoring nodes deployed in remote catchments. The bundle ships
> one variant, so there is no size choice to demonstrate here. Every figure, version, serial number,
> commit hash, identifier and date below is illustrative.
>
> It is deliberately independent of the [`adr`](../adr/adr_example.md), [`rfc`](../rfc/rfc_example.md) and
> [`sdd`](../sdd/sdd_example.md) examples rather than chained to them. The `decision-docs` family teaches
> the difference between investigating a question, proposing an answer, recording a decision and
> describing a design, so each member's example is a different piece of work.
>
> Read it alongside [`spike-report_guide.md`](spike-report_guide.md), the rubric it was graded against.
> Three things it does are the ones this template's own TRAP notes warn against skipping: it names the
> branch the investigation abandoned and the signal that stopped it, it corrects an early finding in
> place instead of deleting it, and it
> spends its closing section on what its own answer fails to cover. Whether a spike should produce a
> written document at all is contested;
> [`spike-report_companion.md`](spike-report_companion.md) section 6.1 carries both sides of that, and
> this example demonstrates the shape rather than a settled practice.

# Over-the-air updates fit the overnight window, and today's bootloader cannot survive one that fails

## The Question

Can a complete application firmware image be delivered to a deployed RS-4 catchment node over its existing
low-power radio link, inside one overnight maintenance window, without drawing the node's battery below the
reserve it needs to survive until its next scheduled calibration visit?

One question, one node, one window. Field operations owns the site-visit budget for the 2027 season and
holds a line in it for unscheduled trips, of which firmware faults are the largest single cause. They are
deciding in October whether the firmware share of that line can come out. Two results would have closed
this as a no: a node that cannot finish a transfer before the window ends, or a node that finishes and
lands under reserve. Both were live possibilities on day one, and one of them happened.

## Scope and Time Box

* Allotted: four working days, agreed with the field operations lead and the firmware lead at the August
  planning session, under one standing condition: nothing gets transmitted to a node that is actually
  deployed. Bench only.
* Allotted time is **calendar** time, not desk time, and that distinction is what makes the run count
  possible. The bench ran unattended around the clock: the sixteen scored runs, one node at a time, at four
  to eight hours each are roughly ninety hours of radio time, which fits three and a half calendar days
  only because nobody had to watch it. Attended work was the setup, the two stalls, and the analysis.
* Spent: three and a half days. The last half-day was planned for a fourth link profile and was not used.
  Once the bootloader constraint in What Was Found turned up, a fourth set of transfer times could not have
  changed what this report recommends, so the box was closed early rather than spent on a number nobody
  would act on.
* Deliberately not attempted:
  * **Gen-1 nodes**, the 60 units carrying the smaller flash part. Excluded by agreement at the start:
    they are already on the retirement schedule and will be off the network before any rollout could
    begin. Nothing here applies to them.
  * **Differential updates.** Planned for day three, abandoned at the end of day two. We had intended to
    measure a binary delta against the full image, and stopped after reading the bootloader source and
    linker map, which show a single application slot with nowhere to stage and verify a patched image
    before it overwrites the running one. The signal that ended this branch was the memory map, not a
    measurement, and it is the reason the recommendation below reads the way it does.
  * **More than one node updating behind a gateway at a time.** Never inside a four-day box. It is the
    largest item in What This Does Not Settle, and it is the one that decides how long a fleet rollout
    takes.
  * **The calibration firmware**, which is a separately signed image on its own update path and was out of
    scope by agreement.

## What Was Tried

Everything below ran on a bench rig, never on the deployed fleet.

**Hardware and versions.** Six RS-4 nodes, serials RS4-0031 through RS4-0036, all on application firmware
3.8.2 and bootloader 1.4.0. One production-configuration gateway, GW-C, on build 2.11.4-rs. A programmable
RF attenuator sat between the nodes and the gateway so that link conditions could be set on purpose instead
of waited for. Transfer used the fragmented-downlink mechanism already shipping in 3.8.2; no new transport
was written for this.

**Link profiles, taken from logs rather than invented.** Three profiles were built from twelve months of
gateway logs: a **strong** profile derived from the 40 deployed nodes with the best median link margin, a
**fleet-median** profile, and a **weak** profile matched to the 20 worst-performing nodes on the network.
Each profile is a fixed attenuation plus a scripted fade replayed from a recorded month.

**What was measured.** Wall-clock time to transfer the full 214 KB image and acknowledge every fragment,
the fragment-acknowledgement percentage at the point a run was stopped, and charge drawn. Charge was taken
with a coulomb counter in series on three of the six nodes, RS4-0031, RS4-0033 and RS4-0035, sampled once
per second.

**Where the evidence lives.** Harness, attenuation profiles and raw per-run logs are in `spikes/ota-window/`
at commit `9d41c2e`. Runs are numbered in `runs/manifest.csv`, and every figure in the next section names
the runs it comes from. Nineteen runs are recorded: runs 1 and 19 are rig setup and teardown checks, run 2
is excluded (see the correction below), and runs 3 to 18 are the sixteen scored runs.

**Reused rather than re-measured, and flagged as such.** The idle-current baseline each charge figure is
subtracted from is the one captured during 3.8.2 release qualification in June, not re-taken this week. The
firmware did not change between then and now, so the reuse is sound, but the baseline is three months old
and a reader should know that before treating the charge numbers as fresh.

## What Was Found

* Observed:
  * **Strong profile, runs 3 to 8.** Five of six transfers completed, in 4 h 10 m to 4 h 35 m, against a
    seven-hour overnight window. The sixth, run 7, ended in the downlink stall described two bullets
    below rather than in anything to do with the link.
  * **Fleet-median profile, runs 9 to 14.** Four of six completed, in 6 h 05 m to 6 h 50 m. Run 13 stood
    at 84 percent of fragments acknowledged when the window closed. Run 12 ended in the stall.
  * **Weak profile, runs 15 to 18.** No run completed. Three were deliberately allowed to run an hour
    past the seven-hour window, to see how close the weakest link came, and were stopped at the
    eight-hour mark with between 61 and 74 percent of fragments acknowledged; run 17 ended in the stall
    at 52 percent.
  * **Charge.** 41 to 46 mAh per completed strong-profile transfer; 58 mAh for the slowest median-profile
    run that finished. The illustrative annual energy budget for an RS-4 is 1,100 mAh per node.
  * **A repeated failure with no cause attached.** On runs 7, 12 and 17, the gateway stopped serving
    downlink to a node that was awake and still requesting fragments. The node kept asking; the queue
    never moved again. Service resumed only after the gateway process was restarted. Same symptom, three
    of sixteen scored runs, and once on each of the three link profiles.
  * **The bootloader has one application slot.** Read directly from bootloader 1.4.0 source and the linker
    map. There is no second region to write into and no known-good image to return to, so a write
    interrupted partway leaves a node holding an incomplete image. No node was deliberately interrupted to
    demonstrate this.
* Which implies:
  * **The window binds where the link is worst, and only there.** For well-linked nodes the overnight
    window is comfortably long enough. Airtime grows with retries, retries are what the weak-profile nodes
    spend their time doing, and the nodes that are hardest to reach by radio are the same ones that are
    most expensive to reach by road. So the saving this work was chasing is concentrated in exactly the
    part of the fleet where it is worth least.
  * **Energy is not the reason to stop.** At 58 mAh, the worst completed transfer is roughly five percent
    of a node's annual budget, for an update we would run at most twice a year. Nothing measured here
    threatens the calibration-visit reserve.
  * **The downlink stall is an open defect, not a known limit.** It is not a link-quality effect, because
    it happened once on each of the three profiles, which rules out the explanation we would otherwise
    have reached for first. We can describe the symptom precisely and cannot say what causes it: gateway
    configuration, a node-side request pattern, and a resource ceiling on GW-C are all still live. Any
    schedule built on the transfer times above is built on a path that stopped working three times this
    week.
  * **The single slot is the finding that changes the answer.** With no fallback image, a transfer that
    fails at the wrong moment does not cost a retry. It costs a technician standing in a catchment with a
    programmer, which is the cost this whole idea exists to remove. This is an inference from code rather
    than from an observed failure, and the confidence is high for that reason rather than in spite of it:
    the recovery path is absent from the source, not merely unreliable.
  * **Confidence, stated where it is uneven.** High on the transfer times, which come from sixteen scored
    runs with one variable moved at a time. Lower on the charge figures, which rest on three nodes from a
    single cell batch against a three-month-old baseline. Lowest on anything to do with the stall, where
    we have a symptom and nothing else.

**Correction, kept in place.** The day-one note in `runs/README.md` recorded that a weak-profile transfer
"completes in about nine hours". That was wrong and it is corrected rather than deleted. It came from run 2,
where the attenuator script had not yet been applied, so the node was effectively running on the strong
profile. Run 2 is excluded from every figure above and is marked excluded in the manifest. The correct
statement is that no weak-profile run completed at all.

## Recommendation

**Proceed to a bounded field pilot, and only after a bootloader that can fall back has shipped.** - Run the
pilot on the 40 strong-profile nodes behind GW-C and GW-F, for one season, before anyone plans anything
wider. The precondition is not a preference and it is not a nice-to-have sequencing note: on bootloader
1.4.0 a failed transfer strands a node until a person reaches it, so piloting first would risk the exact
expense the pilot is meant to prove we can avoid. If a recoverable bootloader is not on the firmware
roadmap for this year, then the honest answer for the 2027 budget is no, and the unscheduled-visit line
should be renewed in October at its current size.

Two things this recommendation deliberately does not ask for. It does not ask for a differential update
scheme: once the window fits, nothing measured suggests the image needs to be smaller. And it does not ask
for a gateway change, because the stall has a symptom and no diagnosis, and buying a fix for an
unexplained fault is how teams end up with two problems.

Who decides what: the firmware lead owns the bootloader call, field operations owns the budget line. Both
need the stall triaged before either can commit, and that triage is the next spike if the bootloader work
gets scheduled. One day, one question, bench rig already standing: what makes the downlink queue stop
serving a node that is still awake and asking?

## What This Does Not Settle

* Still open:
  * **Concurrency, which is the big one.** Every number in this report is one node at a time. There are
    380 nodes behind nine gateways. Whether a gateway can carry several transfers in a single window is
    the difference between a rollout that takes one season and one that takes three, and this spike does
    not even bound it.
  * **The cause of the stall on runs 7, 12 and 17.** Named as a symptom, unexplained as a mechanism. Until
    someone can say what triggers it, nobody can say how often it would happen across a fleet, and the
    pilot's schedule inherits that ignorance.
  * **Cold.** Charge was measured on three nodes from one cell batch at bench temperature, roughly 19 to
    22 C. Several catchment sites sit below freezing for weeks at a time, cell behaviour there is not
    something a bench at room temperature can tell you, and the coldest sites are the ones already running
    the thinnest energy margin.
  * **Whether last year predicts next winter.** The weak profile is a replay of a recorded month from the
    past twelve. It reconstructs conditions that happened; it does not forecast conditions that have not.
  * **Whether a node can abandon a transfer cleanly.** We never tried commanding one to stop partway, so a
    transfer that is visibly not going to finish currently just runs until the window ends. If the stall
    turns out to be node-side, this matters more than it currently sounds.
* Do not conclude from this:
  * **That over-the-air updating removes the site visit.** It removes one reason for one. Annual
    calibration still puts a person next to every node, and the budget line this question came from covers
    both reasons, so what is on offer is a share of that line rather than the line.
  * **That 214 KB is a fixed quantity.** It is the size of today's release. The slowest median-profile run
    that finished had ten minutes of window left, so a larger image does not degrade these results
    gradually; it moves nodes across the line from completing to not completing.
  * **That the strong-profile results describe the fleet.** They describe 40 nodes out of 380. What
    matters for a rollout plan is the distribution of link margin across the whole network, and this spike
    sampled three points on that distribution rather than measuring it.
  * **That the energy result holds for a fleet doing this routinely.** It was measured for one successful
    update. Nothing here covers a node that retries a failing update night after night because no alert
    fires when a transfer never completes.
