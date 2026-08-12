---
title: Nullable fields
domain: 4
tasks: ["4.3"]
verified: "2026-08-12"
---

# Nullable fields

**A required field is an instruction to produce something. The model complies.**

If a source document may not contain the information, mark the field **optional / nullable**. The model returns null instead of inventing a plausible value.

This is the cheapest single defence against extraction hallucination on the whole exam, and it appears in both the objectives and the preparation exercises.

## The companions

- **`"unclear"`** as an enum value, for cases that are present but ambiguous
- **`"other"` + a detail string**, for categories you could not enumerate in advance

Together they give the model somewhere honest to put every kind of uncertainty — which is what stops it from resolving uncertainty by guessing.

## The exam shape

*"Extractions succeed but contain values not present in the source document."* → the fields are required; make them nullable.

Distractors will propose stricter prompts or stricter schemas. Neither helps: a stricter schema makes the fabrication *more* required, not less.

See [tool use structured output](tool-use-structured-output.md) · [4.3](../tasks/4-3.md)
