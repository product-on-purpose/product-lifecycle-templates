---
id: incident-postmortem-002
difficulty: sparse
domain: "video streaming service, partial regional outage of unclear cause"
title: "Regional playback outage postmortem, cause unconfirmed"
created: 2026-08-08
authored_blind: true
---

# Scenario: Regional playback outage postmortem, cause unconfirmed

> **Input brief for a blind efficacy eval.** Every arm receives the ask and the facts below and
> nothing else. Judges never see this file. Authored from the document type description alone by an
> agent instructed not to open this library's templates, per
> [the eval protocol](../../docs/internal/eval-protocol.md) section 6.

## The ask

We had a bad afternoon. Starting around 2:14pm ET on a Tuesday, a chunk of our EU-West subscribers started getting playback failures and endless spinners instead of video. Support ticket volume for 'video won't load' spiked to about 40x normal within the first hour, and we saw roughly 18 percent of EU-West session starts failing at the peak, versus a normal baseline under 1 percent. It took us 51 minutes to confirm we even had a regional problem rather than a client-side bug, and about 2 hours 40 minutes total before playback success rates were back to normal. We still do not have a confirmed root cause. The on-call engineer's working theory is a CDN edge node cache poisoning event tied to a manifest file change, but the CDN vendor's own status page never showed a regional incident and their support case is still open with no answer. Around the same time we also pushed a minor client app update to a small percentage of Android users, and although the timing is suspicious, nobody has been able to reproduce the failure using that build. I need someone to write up what we know, what we don't know, and what we're doing about it, and I need it to go to the exec staff meeting Thursday morning without overpromising a root cause we can't back up. One more wrinkle: this is the third regional playback incident in five months, and the VP of Engineering wants to know whether this one is related to the February incident, which was eventually traced to a DNS TTL misconfiguration. Separately, our billing system had an unrelated payment processor timeout that same week, entirely disconnected from this, that support kept getting confused with the video issue in tickets. Customer sentiment on social media was notably negative, with several posts mentioning cancellation threats, but our subscriber churn data for the week won't be available for another 10 days. We paged the CDN vendor's enterprise support line but SLA response time was 35 minutes against a contracted 15 minute target.

## What you know

- Incident began around 2:14pm ET on a Tuesday, affecting EU-West region
- Peak failure rate reached about 18 percent of EU-West session starts versus a normal baseline under 1 percent
- Support ticket volume for 'video won't load' spiked to roughly 40x normal within the first hour
- 51 minutes elapsed before the team confirmed a regional server-side problem rather than a client bug
- Total time to restore normal playback success rates was about 2 hours 40 minutes
- Root cause is unconfirmed: leading theory is CDN edge cache poisoning tied to a manifest file change, but the CDN vendor's status page showed no incident and their support case remains open
- A minor Android client update shipped to a small percentage of users around the same time; timing is suspicious but no one has reproduced the failure on that build
- This is the third regional playback incident in five months; the VP of Engineering wants to know if it relates to February's incident, which was traced to a DNS TTL misconfiguration
- CDN vendor's enterprise support SLA is a 15 minute response target; actual response took 35 minutes
- The document needs to go to the exec staff meeting Thursday morning without overstating a root cause the team cannot support

## Retrieval probes

> Not shown to any writing arm. A judge answers these from the produced document alone.

| Question | Expected |
|---|---|
| What is the confirmed root cause of this incident? | None confirmed; the document should state the CDN edge cache poisoning theory is unconfirmed (vendor status page showed nothing, support case still open) rather than asserting it as fact |
| How long did it take to confirm this was a regional issue rather than a client-side bug, and how long until playback was fully restored? | 51 minutes to confirm regional scope; about 2 hours 40 minutes total to restore normal playback success rates |
| Is this incident confirmed to be related to the February incident traced to a DNS TTL misconfiguration? | Not confirmed / explicitly called out as an open question the team could not resolve, not asserted as related or unrelated |
| Did the CDN vendor meet its support SLA during this incident? | No, response took 35 minutes against a contracted 15 minute target |
| Was the concurrent Android client update ruled in or ruled out as a contributing cause? | Neither ruled in nor out; timing was suspicious but the team could not reproduce the failure on that build, so it remains an open/unresolved lead |

## Distractors

> Not shown to any writing arm. Facts that are true of the situation and do not belong in a good
> document of this type. A document that includes them is not more complete, it is less disciplined.

- Customer sentiment on social media was notably negative, with several posts mentioning cancellation threats
- An unrelated billing system payment processor timeout occurred the same week and got confused with the video issue in support tickets
- Subscriber churn data for the affected week will not be available for another 10 days
