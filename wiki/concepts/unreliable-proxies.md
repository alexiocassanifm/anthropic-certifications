---
title: Unreliable proxies
domain: 5
tasks: ["5.2", "5.5"]
verified: "2026-08-12"
---

# Unreliable proxies

A family of wrong answers that **measure something adjacent to what you care about**.

## Sentiment

Sentiment analysis measures **how annoyed the customer is**. Case complexity is a different quantity. Escalating on sentiment routes upset-but-simple cases to humans and leaves genuinely hard ones with the agent. The guide states plainly that sentiment does not correlate with complexity.

## Self-reported confidence

An LLM's own confidence is **poorly calibrated**. On hard cases the agent is typically wrong *and confident*. Routing on self-reported confidence therefore routes exactly the wrong cases.

## The legitimate exception

**Field-level confidence calibrated against a labelled validation set** is endorsed in [5.5](../tasks/5-5.md), and finding-level confidence for review routing in [4.6](../tasks/4-6.md).

The reconciliation:

| Illegitimate | Legitimate |
|---|---|
| The model's self-assessment of whether a whole case is too hard | Field-level scores **calibrated against labelled data** |
| An uncalibrated 1–10 score with a threshold | Thresholds derived from a validation set |

**If an item gives you a confidence score with no labelled validation set behind it, treat it as the unreliable proxy.**

## The wider family

Keyword/pattern-matching routing layers, iteration caps as loop control, consensus voting across runs. All measure a proxy rather than the thing.

See [escalation triggers](escalation-triggers.md) · [confidence calibration](confidence-calibration.md) · [deterministic vs probabilistic](../heuristics/deterministic-vs-probabilistic.md)
