---
title: Tool descriptions
domain: 2
tasks: ["2.1", "2.4"]
verified: "2026-08-12"
---

# Tool descriptions

**The description is the routing table, not documentation.** It is the primary mechanism the model uses to select a tool.

## What a good description contains

- Input formats it handles
- Example queries
- Edge cases
- An explicit **boundary**: when to use this tool versus the similar one

Minimal descriptions produce unreliable selection among similar tools — structurally and predictably, not occasionally.

## Ambiguity causes misrouting

`analyze_content` versus `analyze_document` with near-identical descriptions is the guide's example. If a human could not tell them apart from the descriptions alone, neither can the model.

## The system prompt can override a good description

Keyword-sensitive instructions in the system prompt create unintended tool associations. When descriptions are already detailed and selection is still wrong, read the system prompt.

## Why this beats the alternatives

Given "two similar tools, thin descriptions, 12% misrouting", expanding the descriptions is the **cheapest fix at the stated cause**. Few-shot examples add token overhead without fixing the cause. A routing layer is over-engineering that discards the language understanding you are paying for.

See [tool splitting](tool-splitting.md) · [cheapest fix at the root cause](../heuristics/cheapest-fix-at-root-cause.md) · [2.1](../tasks/2-1.md)
