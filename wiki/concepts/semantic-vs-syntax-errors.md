---
title: Semantic vs syntax errors
domain: 4
tasks: ["4.3", "4.4"]
verified: "2026-08-12"
---

# Semantic vs syntax errors

**The guarantee boundary.** Know exactly where a strict schema stops helping.

| Eliminated by the schema | **Not** eliminated |
|---|---|
| Malformed JSON | Line items that do not sum to the stated total |
| Missing required fields | A value placed in the wrong field |
| Wrong types | A plausible but fabricated value |
| Invalid enum values | An inconsistent source faithfully transcribed |

Everything in [4.4](../tasks/4-4.md) exists because of the right-hand column.

## The named technique for catching semantic errors

**Extract `calculated_total` alongside `stated_total` and flag the discrepancy.** Add a `conflict_detected` boolean for inconsistent source data. You do not trust either value; you compare them.

## The exam shape

*"Line items don't sum to the total, yet schema validation passed."* → schemas eliminate syntax errors, not semantic ones. The fix is a semantic validation flow, not a stricter schema.

See [validation and retry](validation-retry.md) · [4.3](../tasks/4-3.md)
