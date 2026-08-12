---
title: Subagent context isolation
domain: 1
tasks: ["1.2", "1.3"]
verified: "2026-08-12"
---

# Subagent context isolation

**Subagents do not inherit the coordinator's conversation history, and do not share memory between invocations.**

This single fact drives a large share of Domain 1 items. There is no ambient state: if a subagent needs to know something, it must be in its prompt.

## Consequences

- The synthesis agent knows nothing about what the search agent found unless you pass the findings.
- Context must be **explicitly provided** in the subagent's prompt — complete findings, not pointers.
- Metadata (source URLs, document names, dates) must travel in a **structured format**, or it dissolves at the boundary and [5.6](../tasks/5-6.md)'s provenance problem begins.

## The diagnostic

| Failure | Cause |
|---|---|
| An agent does not *know* something an earlier agent found | Context was not passed |
| An agent covers the wrong *scope* | Decomposition was too narrow |

Two different fixes. Read the stem carefully to tell them apart.

See [coordinator-subagent](coordinator-subagent.md) · [structured handoff](structured-handoff.md) · [1.3](../tasks/1-3.md)
