---
title: "Scenario 6: Structured Data Extraction"
scenario: 6
primary_domains: [4, 5]
---

# Scenario 6: Structured Data Extraction

**Primary domains:** [4 — Prompt Engineering & Structured Output](../domains/4-prompt-engineering-and-structured-output.md) · [5 — Context Management & Reliability](../domains/5-context-management-and-reliability.md)

## The situation

A structured data extraction system built on Claude. It extracts information from **unstructured documents**, validates output against **JSON schemas**, and maintains **high accuracy**. It must handle edge cases gracefully and integrate with downstream systems.

## What makes this scenario generative

Four constraints, each carrying a cluster of items:

1. **Unstructured documents** — inputs vary in format, and some genuinely lack the information you are asking for.
2. **JSON schema validation** — the guarantee boundary is testable: schemas stop syntax errors, not semantic ones.
3. **"High accuracy"** — a measurable claim, which invites the question *accuracy measured how, and on which segment?*
4. **"Downstream systems"** — the output is consumed by machines, so a fabricated value is worse than a null.

This is the scenario where Domain 4 and Domain 5 genuinely merge: the extraction is a prompting problem, the trust in the extraction is a reliability problem.

## Failure modes to expect

| Symptom | Where it points |
|---|---|
| Occasional malformed JSON breaks the parser | Define the schema as a tool's input schema; read from `tool_use` — [4.3](../tasks/4-3.md) |
| Line items do not sum to the stated total, but the schema validated | Schemas eliminate syntax errors, not semantic ones — [4.3](../tasks/4-3.md) |
| The model invents plausible values for fields the document lacks | Make those fields optional / nullable — [4.3](../tasks/4-3.md) |
| Several extraction schemas exist and the document type is unknown | `tool_choice: "any"` — forces a tool call, model picks which — [4.3](../tasks/4-3.md) |
| Metadata extraction must run before enrichment | Forced `tool_choice: {"type": "tool", "name": "extract_metadata"}` — [4.3](../tasks/4-3.md) |
| A category needs to grow over time without schema changes | Enum with `"other"` plus a detail string; `"unclear"` for ambiguous cases — [4.3](../tasks/4-3.md) |
| Validation fails; the retry is blind | Send back the original document, the failed extraction, and the specific validation error — [4.4](../tasks/4-4.md) |
| Retries burn tokens and never succeed | The information is absent from the source — retry cannot conjure it — [4.4](../tasks/4-4.md) |
| Source data is internally inconsistent | Extract `calculated_total` alongside `stated_total`; add a `conflict_detected` boolean — [4.4](../tasks/4-4.md) |
| Required fields come back empty on structurally varied documents | Few-shot examples covering the varied formats — [4.2](../tasks/4-2.md) |
| Informal measurements and odd phrasings get hallucinated | Few-shot examples reduce hallucination in extraction — [4.2](../tasks/4-2.md) |
| Source formatting is inconsistent (dates, units, currency) | Format normalisation rules in the prompt alongside the strict schema — [4.3](../tasks/4-3.md) |
| 100 documents to process overnight | Message Batches API: 50% cheaper, 24h window — [4.5](../tasks/4-5.md) |
| Some batch documents fail | Resubmit only the failures, identified by `custom_id`, with modifications (e.g. chunking oversized documents) — [4.5](../tasks/4-5.md) |
| An SLA must be met with 24h batch processing | Calculate submission frequency from the constraint — e.g. 4-hour windows to guarantee 30 hours — [4.5](../tasks/4-5.md) |
| Aggregate accuracy is 97% but scanned invoices are terrible | Segment accuracy by document type and field before automating — [5.5](../tasks/5-5.md) |
| Reviewer capacity is limited and misallocated | Field-level confidence calibrated against a labelled validation set — [5.5](../tasks/5-5.md) |
| Novel error patterns go unnoticed in high-confidence output | Stratified random sampling of high-confidence extractions — [5.5](../tasks/5-5.md) |

## The guarantee boundary — the single most testable idea

**A strict JSON schema via tool use eliminates syntax errors entirely. It does not prevent semantic errors.**

| Prevented by the schema | Not prevented |
|---|---|
| Malformed JSON | Line items that do not sum to the total |
| Missing required fields | A value placed in the wrong field |
| Wrong types | A plausible but fabricated value |
| Invalid enum values | An internally inconsistent document faithfully transcribed |

Everything in [4.4](../tasks/4-4.md) exists because of the right-hand column. Semantic validation is your job — and the guide's named technique is to extract both the calculated and the stated value and flag the discrepancy, rather than trusting either.

## The nullable-field principle

**A required field is an instruction to produce something.** If the source document may not contain the information, mark the field optional; the model will return null instead of inventing a value. This is the cheapest single defence against extraction hallucination, and it appears in both the objectives and the preparation exercises.

Pair it with:
- `"unclear"` as an enum value for genuinely ambiguous cases
- `"other"` plus a free-text detail field for extensible categories

## The confidence trap

[5.5](../tasks/5-5.md) contains a distinction that is easy to get backwards:

- **Self-reported confidence, uncalibrated** → unreliable. The model is confident and wrong on exactly the hard cases. This is the same anti-pattern as sentiment-based escalation in [5.2](../tasks/5-2.md).
- **Field-level confidence calibrated against a labelled validation set** → legitimate, and the guide's recommended routing mechanism.

The difference is the labelled validation set. Without it you are routing on a number that means nothing.

And before reducing human review at all: **verify accuracy by document type and by field.** A 97% aggregate can hide a segment at 60%.

## Task statements most likely to be tested here

[4.3](../tasks/4-3.md) · [4.4](../tasks/4-4.md) · [4.2](../tasks/4-2.md) · [4.5](../tasks/4-5.md) · [5.5](../tasks/5-5.md) · [5.1](../tasks/5-1.md)

## How to prepare for it

Build the pipeline. A tool with a JSON schema containing required, optional, and nullable fields plus an `"other"` + detail enum. Feed it documents where fields are genuinely absent, and verify you get nulls rather than inventions. Add a validation-retry loop that feeds back the specific error, and track which failures retry can fix and which it cannot. Then submit 100 documents through the Batches API, handle failures by `custom_id`, and compute whether your total processing time fits a stated SLA.
