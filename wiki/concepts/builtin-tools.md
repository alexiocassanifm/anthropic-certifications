---
title: Built-in tools
domain: 2
tasks: ["2.5"]
verified: "2026-08-12"
---

# Built-in tools

## The selection table

| You need to… | Reach for |
|---|---|
| Find text **inside** files — function names, error strings, imports | **Grep** |
| Find files by **name or extension** pattern | **Glob** |
| Load a whole file | **Read** |
| Replace a unique, identifiable snippet | **Edit** |
| Modify a file with no unique anchor | **Read**, then **Write** |
| Run a command | **Bash** |

The exam's framing is **content versus path**. Grep searches contents; Glob matches paths.

## Edit anchor failure

Edit needs an unambiguous anchor. When the snippet appears more than once, Edit fails — and the documented fallback is **Read the full file, then Write it back**. Retrying Edit with a slightly different snippet is not the answer.

## Incremental understanding

**Start with Grep to find entry points, then Read to follow imports and trace flows.** Reading all files upfront is not thoroughness — it is context exhaustion, and it is a wrong answer wherever it appears.

## Tracing across wrapper modules

Two steps: **enumerate all exported names first, then search each name** across the codebase. A single grep for the original function name misses every call routed through a re-export.

See [context degradation](context-degradation.md) · [2.5](../tasks/2-5.md)
