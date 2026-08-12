---
title: Access failure vs valid empty result
domain: 2
tasks: ["2.2", "5.3"]
verified: "2026-08-12"
---

# Access failure vs valid empty result

Two situations that look identical if you flatten them, and demand opposite responses:

| | Meaning | Right response |
|---|---|---|
| **Access failure** | The query could not run — timeout, unavailable | Retry, try an alternative, or report the gap |
| **Valid empty result** | The query ran and found nothing | Accept it as information |

## Why it matters twice

This distinction appears in **two domains** — [2.2](../tasks/2-2.md) (tool error design) and [5.3](../tasks/5-3.md) (error propagation across agents). That doubles its exam probability.

## The anti-pattern

Catching a timeout and **returning an empty result set marked successful**. This silently converts a failure into "there is nothing there". The coordinator has no way to know, cannot recover, and produces a confidently incomplete answer.

It is the worst option in the [5.3](../tasks/5-3.md) sample question precisely because it fails silently — the other wrong answers at least fail loudly.

See [MCP structured errors](mcp-errors.md) · [structured error context](structured-error-context.md)
