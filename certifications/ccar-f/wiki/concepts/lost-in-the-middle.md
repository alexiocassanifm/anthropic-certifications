---
title: Lost in the middle
domain: 5
tasks: ["5.1"]
verified: "2026-08-12"
---

# Lost in the middle

**Models process the beginning and end of long inputs reliably, but may omit findings from middle sections.**

This is a design constraint on how you order aggregated input, not a curiosity.

## The mitigations

- **Place the key findings summary at the beginning** of an aggregated input
- **Organise detailed results with explicit section headers**, so the structure is navigable rather than a wall

## Where it bites

Anywhere you concatenate many results into one prompt: multi-agent synthesis, multi-file review, long document analysis. If a finding sits in the middle of a long aggregation, assume it may not land.

See [progressive summarization](progressive-summarization.md) · [5.1](../tasks/5-1.md)
