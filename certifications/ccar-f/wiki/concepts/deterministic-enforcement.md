---
title: Deterministic enforcement and prerequisite gates
domain: 1
tasks: ["1.4", "1.5"]
verified: "2026-08-12"
---

# Deterministic enforcement and prerequisite gates

**A prompt instruction has a non-zero failure rate.** When a requirement must hold every time, encode it in code.

## Prerequisite gate

Block a downstream tool call until an earlier step has completed successfully. The canonical example: `process_refund` is unavailable until `get_customer` has returned a **verified** customer ID. The model cannot skip the step because the step is not skippable.

## When a gate is required

Ask what happens the 1% of the time the model does not comply:

- *A slightly worse answer* → a prompt is fine, and cheaper.
- *Money moves incorrectly, an unverified identity gets access, a policy is violated* → a prompt is **not** fine, however well written.

"12% of refunds go to the wrong account" is not a prompting problem. Rewriting the instruction to say *mandatory* moves 12% to maybe 3%, and 3% is still an incident.

## The recognisable wrong answers

- "Enhance the system prompt to state that verification is mandatory"
- "Add few-shot examples showing the agent always calling `get_customer` first"
- "Implement a routing classifier that enables only the relevant tools" — addresses tool *availability*, not tool *ordering*

See [hooks](hooks.md) · [deterministic vs probabilistic](../heuristics/deterministic-vs-probabilistic.md) · [1.4](../tasks/1-4.md)
