---
title: tool_choice
domain: 2
tasks: ["2.3", "4.3"]
verified: "2026-08-12"
---

# `tool_choice`

The knob that turns tool use from a suggestion into a guarantee.

| Value | Guarantee |
|---|---|
| `"auto"` | **None** — the model may return text instead of calling a tool |
| `"any"` | Must call a tool; the model chooses which |
| `{"type": "tool", "name": "..."}` | Must call **this specific** tool |

## When to use which

- **`"any"`** — several extraction schemas exist and the document type is unknown. You need structured output; you do not care which schema.
- **Forced selection** — a specific extraction must run before enrichment steps. `{"type": "tool", "name": "extract_metadata"}` pins it, and subsequent steps happen in follow-up turns.
- **`"auto"`** — fine when a prose answer is an acceptable outcome. Wrong when you need guaranteed structure.

A fourth value, `{"type": "none"}`, also exists (the model cannot use tools). Not mentioned in the guide.

See [tool use structured output](tool-use-structured-output.md) · [tool distribution](tool-distribution.md) · [4.3](../tasks/4-3.md)
