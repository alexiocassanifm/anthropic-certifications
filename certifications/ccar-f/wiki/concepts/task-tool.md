---
title: Task tool, AgentDefinition, parallel spawning
domain: 1
tasks: ["1.3"]
verified: "2026-08-12"
---

# Task tool, AgentDefinition, parallel spawning

## `Task` — the spawning mechanism

A coordinator spawns subagents by calling the `Task` tool. **`"Task"` must be in its `allowedTools`** or it cannot spawn at all. A concrete, checkable fact and an easy exam item.

## `AgentDefinition`

Configures each subagent type:

- **description** — what it is for
- **system prompt** — how it behaves
- **tool restrictions** — which tools it may use

Tool restrictions here are where [least-privilege tooling](../heuristics/least-privilege-tooling.md) meets subagent design.

## Parallel spawning

**Emit multiple `Task` calls in a single coordinator response.** Spawning across separate turns serialises work that is independent, and is the latency bug this skill exists to prevent.

If an item reports "subagents run one after another and latency is 4× what it should be", this is the answer.

See [subagent context isolation](subagent-context-isolation.md) · [tool distribution](tool-distribution.md) · [1.3](../tasks/1-3.md)
