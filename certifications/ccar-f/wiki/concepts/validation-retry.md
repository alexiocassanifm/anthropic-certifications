---
title: Validation, retry, and feedback loops
domain: 4
tasks: ["4.4"]
verified: "2026-08-12"
---

# Validation, retry, and feedback loops

## Retry with error feedback

Send back **the original document, the failed extraction, and the specific validation error**. A bare "try again" retries the same reasoning and produces the same failure.

## The limit of retry — the key fact

**Retries are ineffective when the required information is simply absent from the source document.**

| Retry works for | Retry cannot fix |
|---|---|
| Format mismatches | Information that is not in the document |
| Structural output errors | Data that exists only in an external source you did not provide |

Distinguishing "the model got it wrong" from "the data is not there" is the whole objective. The second case needs detection and routing, not more retries.

## Self-correction validation flows

- Extract `calculated_total` alongside `stated_total` to flag discrepancies
- Add `conflict_detected` booleans for inconsistent source data
- Add a `detected_pattern` field to findings, enabling analysis of false-positive patterns when developers dismiss them

See [semantic vs syntax errors](semantic-vs-syntax-errors.md) · [confidence calibration](confidence-calibration.md) · [4.4](../tasks/4-4.md)
