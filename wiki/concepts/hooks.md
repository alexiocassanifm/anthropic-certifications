---
title: Agent SDK hooks
domain: 1
tasks: ["1.5"]
verified: "2026-08-12"
---

# Agent SDK hooks

Interception points that run deterministically around tool use. Two directions, two jobs.

| Direction | Hook | Job |
|---|---|---|
| Results coming back | **`PostToolUse`** | Transform tool results before the model processes them |
| Calls going out | **Tool call interception** | Inspect an outgoing call and block or redirect it |

## `PostToolUse` — data normalisation

Different MCP tools return the same concept in different shapes: Unix timestamps, ISO 8601 strings, numeric status codes. Asking the model to reconcile them on every turn is asking for a deterministic transformation to be done probabilistically — and paying tokens for it forever. Write the transformation.

## Interception — compliance

A refund above $500 never reaches the payment system; the hook blocks it and redirects to an alternative workflow such as human escalation.

## The rule

**Hooks give deterministic guarantees; prompt instructions give probabilistic compliance.** Choose hooks when business rules require guaranteed compliance — and *not* when the thing you need is judgment, which a hook cannot supply and will instead block.

See [deterministic enforcement](deterministic-enforcement.md) · [1.5](../tasks/1-5.md)
