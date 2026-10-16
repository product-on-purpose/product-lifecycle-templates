---
title: "GPS telemetry ingestion for the truck fleet: recommend Amazon MSK over RabbitMQ Streams"
status: "final"
date: "2026-10-09"
decision_makers: ["Marta Lindqvist, Platform Engineering Lead"]
doc_type: trade-study
size: full
source_template: trade-study
source_template_version: 0.1.0
---

> **Worked example.** A filled `trade-study` for a fictional freight company, working name Thornwell
> Freight, choosing a message-ingestion technology for GPS telemetry from its truck fleet. The full
> variant is shown because the choice is hard to reverse once a customer contract depends on it and
> the two engineers who would run it disagree about one of the weights. Every company name, person
> name, figure, weight, score and date below is illustrative; where a technical claim about Kafka,
> Amazon MSK or RabbitMQ Streams appears, it is a fact about that product as documented, not an
> invented one.
>
> It is deliberately independent of the [`adr`](../adr/adr_example.md), [`rfc`](../rfc/rfc_example.md)
> and [`sdd`](../sdd/sdd_example.md) examples rather than chained to them, and of
> [`spike-report_example.md`](../spike-report/spike-report_example.md): the `decision-docs` family
> teaches the difference between investigating a question, proposing an answer, evaluating named
> options, recording a decision and describing a design, so each member's example is a different piece
> of work. Read it alongside [`trade-study_guide.md`](trade-study_guide.md), the rubric it was graded
> against.

# GPS telemetry ingestion for the truck fleet: recommend Amazon MSK over RabbitMQ Streams

## Problem and Decision Framing

* Question this study answers: the fleet-management platform at Thornwell Freight currently uploads
  each truck's full day of GPS positions once, overnight, when the truck docks at a depot and
  connects to depot Wi-Fi. A new customer contract requires geofence-exit alerts to reach dispatch
  within the hour of the event, not the next morning. The question is which message-ingestion
  technology should sit between the truck-side device and the dispatch dashboard to carry that
  continuous stream.
* Decision this feeds, and who decides: whether to introduce a continuous ingestion layer at all, and
  if so, which technology to run it on, for the next two to three years. Decided by Marta Lindqvist,
  Platform Engineering Lead, with Sofia Reyes, Operations Lead, consulted because she owns the
  on-call rotation that will carry whichever system is chosen.
* Constraints and assumptions every alternative must respect: the truck-side GPS device and its
  firmware are out of scope: a fleet-wide hardware change is not budgeted this cycle, and every
  alternative below assumes the device keeps sending the same message format it already sends. The
  new ingestion path must be able to run alongside the nightly batch during cutover rather than
  requiring a single flag day. The platform team is two engineers who also carry other production
  responsibilities, so whatever is chosen has to fit inside their existing on-call capacity. Whatever
  is chosen must be running before the new contract's go-live date, three months from this study.

## Criteria and Weights

Scoring method and scale in use: each alternative is scored 0 to 10 on each criterion below. A
weighted total is score times weight divided by 10, summed across the five criteria, so the maximum
possible weighted total is 100.
What a weight means here: importance. None of the weights below are set to the swing between the best
and worst alternative on that criterion; the team discussed swing weighting and chose importance
because two of the five criteria (cost and latency) do not yet have a wide enough spread between
alternatives to weight by swing honestly.

| ID | Criterion | Weight | Mandatory? | Justification |
|---|---|---|---|---|
| C1 | Replicates every message to more than one node before acknowledging receipt | 15 | Yes | Marked mandatory because a truck's telemetry that exists on only one node is one disk failure away from vanishing outright, which Operations will not accept from anything meant to replace the nightly batch. Scored rather than left unweighted, so that the degree of exposure among the alternatives that do pass it still counts. |
| C2 | Operational burden on the two-person on-call rotation | 35 | No | Set to the highest weight here because neither platform engineer has run a distributed message broker in production, and whichever option is chosen has to be carried by two people without a dedicated hire. |
| C3 | Integration effort with the existing fleet-management pipeline | 25 | No | Weighted this high because the dispatch dashboard, the device-side agent and the existing data-warehouse job all read today's nightly-batch format, and every alternative below changes some part of that chain. |
| C4 | Cost at the fleet's current and projected message volume | 15 | No | Weighted lower than operational burden because the contract that forces this decision is worth more than any plausible difference in ingestion cost; every score on this row is this team's own illustrative estimate, not a vendor quote. |
| C5 | Latency from a truck leaving a geofence to the alert reaching the dispatch dashboard | 10 | No | Weighted lowest of the four non-mandatory rows because the new contract's own service level is "within the hour," which every live alternative clears comfortably; finer differences between them matter less than the other four rows. |

## Alternatives, Including a Do-Nothing Baseline

How the field was narrowed to the alternatives below: six named technologies were on the table before
narrowing: self-managed Apache Kafka, Amazon MSK, Amazon Kinesis Data Streams, RabbitMQ Streams, NATS
JetStream and Google Cloud Pub/Sub. Kinesis Data Streams was set aside first, on a procurement
constraint rather than a technical one: Thornwell's existing data-warehouse contract already includes
committed Kafka-compatible throughput that Kinesis would duplicate rather than use. Google Cloud
Pub/Sub was set aside because standing up a second cloud provider's identity and networking stack for
one service is not something a two-person platform team is resourced to maintain. NATS JetStream was
set aside on familiarity: Thornwell already runs RabbitMQ for two other internal queues and has never
run NATS, so RabbitMQ carries the "message broker the team already knows" argument and NATS does not.
That left four alternatives, including the baseline.

| ID | Alternative | Description | Do-nothing or do-minimum baseline? |
|---|---|---|---|
| A0 | Keep the current nightly batch upload | No new ingestion system. Each truck's onboard GPS log is extracted once it docks overnight and the batch file is uploaded into the existing data-warehouse job, as today. | Yes |
| A1 | Self-managed Apache Kafka | A Kafka cluster the platform team builds, configures and operates itself on the company's own compute, with replication factor and acknowledgment settings set per topic by the team. | No |
| A2 | Amazon MSK (provisioned) | A managed Kafka control plane: AWS creates, updates and deletes the cluster's brokers and replaces a failed broker automatically; the team still owns topic-level configuration. | No |
| A3 | RabbitMQ Streams, self-hosted | A RabbitMQ stream, run by the platform team on the same infrastructure that already hosts Thornwell's two other internal RabbitMQ queues. | No |

## Scoring Matrix

The do-nothing baseline is scored on every criterion below for comparison, but its weighted total is
not computed: it fails mandatory criterion C1, and a failed mandatory criterion drops an alternative
from the ranking rather than merely cost it points.

| Criterion | Weight | A0: Nightly batch | A1: Self-managed Kafka | A2: Amazon MSK | A3: RabbitMQ Streams |
|---|---|---|---|---|---|
| C1: Replicates before ack | 15 | 0 (fails: a truck's positions sit only on that truck's own device until the nightly job runs, so nothing is replicated before the batch exists at all) | 8 (Kafka's replication factor is set per topic, and a committed message survives as long as one in-sync replica stays up, once the team sets `acks` and `min.insync.replicas` to require that) | 6 (AWS replaces a failed broker automatically, but this research found no Amazon MSK-specific statement of a per-topic replication or commit guarantee independent of Kafka's own documentation, so the score rests on broker-level failure handling rather than a message-level guarantee the team has independently confirmed for MSK) | 7 (RabbitMQ streams are persistent and replicated by default, and a publisher confirms are issued once the write has reached a quorum of stream replicas; the gap is that a replica does not explicitly flush to disk, so an uncontrolled shutdown can still lose data on that one node) |
| C2: Operational burden | 35 | 10 (nothing new to run) | 3 (the team owns cluster operations end to end with no prior production experience running one) | 7 (AWS owns the control-plane operations; the team still owns topic configuration and client-side settings) | 4 (self-hosted, but the team already operates two other RabbitMQ queues, so the operational pattern, if not the stream feature specifically, is familiar) |
| C3: Integration effort | 25 | 10 (nothing changes) | 5 (new client libraries, new topic schema, and a new consumer to feed the dashboard) | 6 (same client-side work as self-managed Kafka, with cluster provisioning handled by AWS instead of the team) | 8 (the team's existing RabbitMQ client code and monitoring carry over; only the stream-specific consumer logic is new) |
| C4: Cost (illustrative team estimate) | 15 | 10 (already paid for; no new spend) | 6 (compute cost for a cluster the team must size itself) | 5 (managed-service premium on top of the same compute) | 7 (runs on infrastructure already provisioned for the existing queues) |
| C5: Latency | 10 | 1 (next business day, by design) | 8 (sub-minute, estimated from the team's own prototype) | 8 (sub-minute, estimated from the team's own prototype) | 7 (sub-minute, estimated from the team's own prototype, slightly behind the other two because of the quorum-confirm round trip) |
| **Weighted total** | | Dropped (fails mandatory C1) | 52.0 | 64.0 | 62.0 |

## Sensitivity Analysis

* Weight or score tested: the weight on operational burden (C2), the number Marta and Dev argued over
  most, because neither of them has operated a message broker in production and they disagreed about
  how much that inexperience should count against both live broker options equally.
* How far it would have to move before the recommendation changes: shifted from 35 down toward 30 of
  the 100 total points, moving the difference onto integration effort (C3). At a weight of 31,
  Amazon MSK and RabbitMQ Streams are tied at 63.6. At 30, RabbitMQ Streams leads, 64.0 to 63.5.
* Does the recommendation survive this test: yes, but only just. Amazon MSK leads at any weight on
  operational burden above 31; at 31 the two tie, and at 30 RabbitMQ Streams takes the lead. A
  four-point move in a single weight erases the lead, and five points reverse it.

## Risk and Benefit

| Alternative | Risk | Benefit | Mitigation (if this becomes the recommendation) |
|---|---|---|---|
| Self-managed Kafka | If the team sets `acks` or `min.insync.replicas` wrong while learning the system, the committed-message guarantee is weaker than the score above assumes, and neither engineer has configured these settings before. | Finer control: replication factor and the acknowledgment setting are both set per topic, rather than inherited from a managed service's defaults. | Bring in a contractor with production Kafka experience for the first topic configuration, or send one engineer to training before go-live. |
| Amazon MSK | The broker-level auto-replacement this score credits is AWS's; this research did not independently confirm a per-topic replication or commit guarantee for MSK beyond what self-managed Kafka's own documentation states, so part of what the team is relying on for durability is inherited rather than separately verified for the managed service. | AWS owns cluster creation, update and deletion, and automatically mitigates or replaces an unhealthy broker, which is exactly the operational work the two-person rotation is least equipped to absorb. | Before committing operationally, have the team confirm the actual per-topic replication factor and acknowledgment settings it will run on MSK, rather than assuming they match self-managed Kafka's documentation by default. |
| RabbitMQ Streams | Without an explicit retention policy, a stream's log grows until the disk runs out, and a replica does not flush to disk automatically, so an uncontrolled shutdown can lose data for replicas on that one node. A stream also needs a quorum of its declared nodes available to function, so losing too many nodes makes it unavailable rather than merely degraded. | The team already runs two other RabbitMQ queues on the same infrastructure, so monitoring, alerting and the on-call runbook pattern already exist and do not need to be built from nothing. | Set an explicit retention policy before this carries fleet telemetry, and document the quorum-loss failure mode in the on-call runbook before go-live. |

## Recommendation

* Recommended alternative, or alternatives if genuinely close: Amazon MSK, narrowly ahead of RabbitMQ
  Streams, 64.0 to 62.0 of 100. Call this a near-tie rather than a clear win: the Sensitivity Analysis
  above shows a four-point move in one weight erases the lead. Self-managed Kafka is not
  competitive at any weight tested in that analysis. The nightly-batch baseline is excluded from the
  ranking entirely because it fails mandatory criterion C1.
* Rows this depends on: C2 (operational burden), where MSK scores well because AWS owns the
  control-plane work the two-person rotation is least equipped to absorb, and C1, where the evidence
  for MSK's own durability guarantee is thinner than the evidence for self-managed Kafka's, a gap the
  Risk and Benefit section names directly.
* Conditions under which this holds: stands only as long as operational burden's weight stays above 31
  of the 100 points. This should be revisited if the two-person rotation gains a third
  engineer, if the team's RabbitMQ experience ends up outweighing its Kafka experience, or if the
  per-topic replication settings confirmed for MSK (see Risk and Benefit) turn out weaker than
  self-managed Kafka's.
* Decision taken, and where it is recorded for good: adopt Amazon MSK for GPS telemetry ingestion,
  conditional on confirming the per-topic replication and acknowledgment settings before go-live.
  Recorded in Thornwell Freight's internal decision log as entry TF-DEC-2026-07.

## Dissent or Independent Review

* Who disagreed, and how it was addressed: Dev Marsh, the platform engineer who would carry most of
  the day-to-day operation of whichever broker is chosen, preferred RabbitMQ Streams, on the strength
  of the team's existing RabbitMQ experience, and argued the operational-burden weight of 35 overstated
  how much that experience gap actually matters once either system is running in steady state. Marta
  reworked Sensitivity Analysis using Dev's preferred weight of 28; at that number RabbitMQ Streams leads,
  64.8 to 63.3. Dev accepted the result once the Sensitivity Analysis made the threshold explicit,
  rather than continuing to argue the number in the abstract, but flagged that the decision should be
  revisited after the first quarter of running MSK if the operational burden turns out closer to his
  estimate than to the team's.
* Who checked the scoring, and how independent of the outcome they are: Sofia Reyes reviewed the
  completed matrix before this document was finalized and found no arithmetic error. She is not
  independent of the outcome: she owns the on-call rotation that will run whichever system is chosen,
  so she has a stake in the answer. No reviewer outside the platform and operations teams checked the
  scoring.

## References

* Apache Kafka documentation, replication and acknowledgment sections, read 2026-09-29, source for the
  replication-factor, `acks` and `min.insync.replicas` facts under self-managed Kafka in Criteria and
  Weights and the Scoring Matrix.
* Amazon MSK documentation, cluster operations and broker-failure handling pages, read 2026-09-29,
  source for the control-plane and broker-replacement facts under Amazon MSK in the Scoring Matrix and
  Risk and Benefit.
* RabbitMQ Streams documentation, persistence and replication pages, consulted 2026-09-30, source for
  the quorum-confirm, retention and disk-flush facts under RabbitMQ Streams in the Scoring Matrix and
  Risk and Benefit.
* Thornwell Freight platform team, ingestion prototype notes, dated 2026-10-05, source for the
  sub-minute latency estimates in the Scoring Matrix's C5 row.
* Thornwell Freight on-call rotation roster, current as of 2026-10-01, source for the two-person
  staffing fact behind the weight on operational burden in Criteria and Weights.
* The new customer contract's service-level addendum, signed 2026-09-18, source for the "within the
  hour" alert requirement behind the weight on latency in Criteria and Weights.
* Thornwell Freight platform team, internal cost estimate worksheet, dated 2026-10-02, source for the
  illustrative cost scores in the Scoring Matrix; no vendor price appears anywhere in this document.
