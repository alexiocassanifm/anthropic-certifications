---
title: Agentic loop
domain: 1
tasks: ["1.1"]
verified: "2026-08-12"
---

# Agentic loop

The cycle that lets an agent act autonomously.

1. Send the request to Claude
2. Inspect `stop_reason`
3. If the model requested tools, execute them
4. Append the results to conversation history
5. Send again

Repeat while `stop_reason` is `"tool_use"`; stop when it is `"end_turn"`.

## Tool results go back into context

Results are appended as a message, so the next request carries them and the model can reason over what it just learned. Dropping or summarising them away leaves the model reasoning about a world that no longer exists — and starts the context problems in [5.1](../tasks/5-1.md).

## Model-driven, not pre-configured

In an agentic loop **Claude decides which tool to call next** based on current context. That is the difference from a decision tree or a fixed tool sequence written in advance, and it is the reason the loop is worth building: it adapts to what the tools actually returned.

See [stop_reason](stop-reason.md) · [1.1](../tasks/1-1.md)
