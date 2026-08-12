---
title: Confidence calibration and accuracy segmentation
domain: 5
tasks: ["5.5"]
verified: "2026-08-12"
---

# Confidence calibration and accuracy segmentation

## Aggregate accuracy masks segment failure

**A 97% overall figure can conceal a document type or a field performing terribly.** Before reducing human review, **validate accuracy by document type and by field**. Automating on an aggregate automates the broken segment along with the good ones.

## Calibration is what makes confidence legitimate

**Field-level confidence scores calibrated using labelled validation sets** route review attention. The labelled set is the whole difference between this and the [unreliable proxy](unreliable-proxies.md) that [5.2](../tasks/5-2.md) rejects.

Route to human review: low model confidence, and ambiguous or contradictory source documents.

## Stratified random sampling

Sample **high-confidence** extractions on an ongoing basis, to measure error rates and **detect novel error patterns** — the ones nobody wrote a rule for.

Reviewing only low-confidence items feels efficient and guarantees that unknown failure modes in the high-confidence pool are never found. That is the trap.

See [unreliable proxies](unreliable-proxies.md) · [validation and retry](validation-retry.md) · [5.5](../tasks/5-5.md)
