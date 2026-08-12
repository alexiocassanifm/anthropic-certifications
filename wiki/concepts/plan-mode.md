---
title: Plan mode vs direct execution
domain: 3
tasks: ["3.4"]
verified: "2026-08-12"
---

# Plan mode vs direct execution

**Plan when the *approach* is uncertain. Execute directly when only the *work* remains.**

| | Use for |
|---|---|
| **Plan mode** | Large-scale changes, multiple valid approaches, architectural decisions, multi-file modifications |
| **Direct execution** | Simple, well-scoped changes — a single validation check, a one-file bug fix with a clear stack trace |

Plan mode enables safe codebase exploration and design **before committing to changes**, preventing costly rework when dependencies surface late.

## Both signals must be present

Scale *and* genuine uncertainty. A 45-file migration with one obvious mechanical transformation is large but not uncertain. An architectural choice touching three files is small but uncertain. The guide's examples pair them — microservice restructuring, library migrations, choosing between integration approaches with different infrastructure requirements.

## The named wrong answers

- **"Start direct, switch to plan mode if it gets complicated"** — wrong when the complexity is **already stated in the requirements**. You are not discovering it; you were told.
- **"Make changes incrementally and let the implementation reveal the structure"** — risks costly rework.
- **"Direct execution with comprehensive upfront instructions"** — assumes you already know the right structure without exploring.

## Combining them

Plan mode for investigation, direct execution for implementation, is explicitly endorsed.

See [Explore subagent](explore-subagent.md) · [task decomposition](task-decomposition.md) · [3.4](../tasks/3-4.md)
