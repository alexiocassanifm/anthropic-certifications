---
title: Provenance and uncertainty in synthesis
domain: 5
tasks: ["5.6"]
verified: "2026-08-12"
---

# Provenance and uncertainty in synthesis

## Attribution is lost at the summarisation step

When findings are compressed **without** their claim-source mappings, the attachment is gone and cannot be recovered downstream. The fix is therefore upstream: require subagents to emit **structured claim-source mappings** — source URL or document name, relevant excerpt, publication date — that synthesis preserves and merges.

## Conflicting sources

**Annotate the conflict with attribution; do not arbitrarily select one value.** Picking one silently destroys information the reader needs to judge the claim.

Document analysis should **complete with conflicting values included and explicitly annotated**, letting the coordinator decide how to reconcile before synthesis.

Structure reports with explicit sections distinguishing **well-established** findings from **contested** ones, preserving original source characterisations and methodological context.

## Temporal data

Require **publication or data-collection dates** in structured outputs. A 2023 figure and a 2025 figure are not a contradiction; they are a trend. Without dates, the difference gets flagged as a conflict.

## Render content types appropriately

Financial data as tables, news as prose, technical findings as structured lists — **rather than converting everything to a uniform format**. Flattening loses meaning that the format was carrying.

See [structured handoff](structured-handoff.md) · [progressive summarization](progressive-summarization.md) · [5.6](../tasks/5-6.md)
