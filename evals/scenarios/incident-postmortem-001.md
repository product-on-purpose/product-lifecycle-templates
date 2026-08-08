---
id: incident-postmortem-001
difficulty: standard
domain: "payments processor, overnight settlement batch failure"
title: "Overnight Settlement Batch Failure Postmortem"
created: 2026-08-08
authored_blind: true
---

# Scenario: Overnight Settlement Batch Failure Postmortem

> **Input brief for a blind efficacy eval.** Every arm receives the ask and the facts below and
> nothing else. Judges never see this file. Authored from the document type description alone by an
> agent instructed not to open this library's templates, per
> [the eval protocol](../../docs/internal/eval-protocol.md) section 6.

## The ask

Last night's settlement batch blew its SLA again, third time in five months, and this time it actually hit merchants, not just an internal dashboard turning red. About 2,300 payouts landed after the 9am cutoff, support took 180 tickets, and four of our bigger merchants are making noise about leaving. I need the writeup on my desk that walks through what happened, why our own alerting let it sit for almost three hours before anyone was paged, and why the fix attempt partway through made things worse instead of better. The VP of Payments Ops wants to know inside 48 hours whether this was a one-off vendor problem or something that should move up the reconciliation engine migration. Don't just tell me it's fixed, tell me what actually changes so we're not back here in another five months.

## What you know

- The failed job was the 01:40 UTC nightly settlement batch that reconciles merchant payouts against the acquiring bank file for same-day ACH
- The batch failed at 02:14 UTC when a schema validation step rejected 340,000 of 1.2 million transaction rows after a bank file format change went live without notice
- On-call engineer did not get paged until 04:50 UTC because the alert routing rule for the settlement queue had been pointed at a deprecated Slack channel since a channel rename three weeks earlier
- Merchant payouts were delayed by 6 hours and 40 minutes; about 2,300 merchants had payouts land after their stated 9am cutoff
- Support fielded 180 merchant tickets and four merchants with monthly volume over 500,000 dollars threatened to move to a competitor processor
- The acquiring bank had sent a changelog email about the file format update to a distribution list that no longer included anyone on the current payments engineering team
- A manual failover to the previous day's reconciliation logic was attempted at 05:30 UTC by an engineer who was not the batch's usual owner, and it corrupted the retry counter, which delayed final recovery by another 90 minutes
- The team has a standing SLA that settlement must complete by 06:00 UTC and this is the third time in five months that SLA has been missed
- There is a long-planned migration to a new reconciliation engine scheduled for next quarter that would replace this batch job entirely
- Finance had already closed the previous day's ledger by the time the delayed settlement posted, requiring a manual adjusting entry that the controller flagged as a recurring audit finding risk
- The VP of Payments Ops wants to know within 48 hours whether this is a one-off vendor problem or a pattern that changes the timeline for the reconciliation engine migration
- The engineer who built the original schema validation step left the company four months ago and no one currently owns that code
- Total estimated cost of the incident, including manual reconciliation labor and one merchant credit issued as a goodwill gesture, was approximately 42,000 dollars

## Retrieval probes

> Not shown to any writing arm. A judge answers these from the produced document alone.

| Question | Expected |
|---|---|
| What time did the settlement batch actually fail, and what triggered the failure? | It failed at 02:14 UTC when a schema validation step rejected 340,000 of 1.2 million rows after an unannounced bank file format change |
| Why was the on-call engineer not paged until 04:50 UTC? | The alert routing rule pointed at a deprecated Slack channel, stale since a channel rename three weeks earlier |
| What action taken during the incident made recovery worse, and by how long did it delay things? | A manual failover to the prior day's reconciliation logic, attempted by an engineer who wasn't the usual owner, corrupted the retry counter and added about 90 minutes to recovery |
| Who decides whether this incident changes the timeline for the reconciliation engine migration, and by when? | The VP of Payments Ops, within 48 hours |
| What is explicitly missing in terms of ownership that contributed to the incident or its risk going forward? | The engineer who built the schema validation step left four months ago and no one currently owns that code |

## Distractors

> Not shown to any writing arm. Facts that are true of the situation and do not belong in a good
> document of this type. A document that includes them is not more complete, it is less disciplined.

- Total estimated cost of the incident, including manual reconciliation labor and one merchant credit issued as a goodwill gesture, was approximately 42,000 dollars
- There is a long-planned migration to a new reconciliation engine scheduled for next quarter that would replace this batch job entirely
