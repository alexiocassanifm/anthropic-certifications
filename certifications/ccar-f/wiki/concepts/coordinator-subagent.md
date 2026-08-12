---
title: Coordinator-subagent (hub-and-spoke)
domain: 1
tasks: ["1.2"]
verified: "2026-08-12"
---

# Coordinator-subagent (hub-and-spoke)

One coordinator agent manages **all** inter-subagent communication. Subagents never talk to each other.

## What centralisation buys

- **Observability** — one place to see what happened
- **Consistent error handling** — one place that decides what a failure means
- **Controlled information flow** — one place that decides who learns what

These three are why the apparent overhead is worth it, and they are what an item is testing when it offers direct subagent-to-subagent communication as an "efficiency" improvement. That option is always wrong.

## The coordinator's four jobs

1. Task decomposition
2. Delegation
3. Result aggregation
4. Deciding **which** subagents to invoke, based on query complexity — not always the full pipeline

## The dominant failure

Decomposition quality caps system quality. A coordinator that partitions a topic too narrowly produces a coherent, well-cited, incomplete answer — with every subagent working perfectly. When components all succeed and the whole fails, look upstream.

See [subagent context isolation](subagent-context-isolation.md) · [task decomposition](task-decomposition.md) · [1.2](../tasks/1-2.md)
