---
title: stop_reason
domain: 1
tasks: ["1.1"]
verified: "2026-08-12"
---

# `stop_reason`

The field that drives agentic loop control flow. **Read it; never infer it.**

| Value | Meaning | In the guide |
|---|---|---|
| `"tool_use"` | The model wants a tool executed — continue the loop | ✅ |
| `"end_turn"` | The model is finished — terminate | ✅ |
| `"max_tokens"` | Hit the output cap | — |
| `"stop_sequence"` | Hit a custom stop sequence | — |
| `"pause_turn"` | A server-side tool loop paused and can be resumed | — |
| `"refusal"` | The model declined on safety grounds | — |

The exam tests the first two. A production loop should branch on all of them — a `pause_turn` treated as termination silently truncates the answer.

## Why it matters

Every wrong answer on [1.1](../tasks/1-1.md) substitutes something else for this field: parsing the assistant's prose for "I'm done", capping iterations, or checking whether text content appeared. All three are probabilistic readings of a signal that is already explicit and typed.

See [agentic loop](agentic-loop.md) · [drift log](../exam/drift-log.md#stop_reason-values--extended)
