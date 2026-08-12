---
title: Explore subagent and context isolation
domain: 3
tasks: ["3.4", "5.4"]
verified: "2026-08-12"
---

# Explore subagent and context isolation

The **Explore subagent** isolates verbose discovery output and returns **summaries**, preserving the main conversation's context.

## One principle, four expressions

Keeping verbose work out of the thread that must stay coherent appears across the blueprint:

| Mechanism | Where |
|---|---|
| Explore subagent | [3.4](../tasks/3-4.md) |
| `context: fork` on a skill | [3.2](../tasks/3-2.md) |
| Subagent delegation for exploration | [5.4](../tasks/5-4.md) |
| Grep-then-Read incremental discovery | [2.5](../tasks/2-5.md) |

Recognising them as the same idea makes four objectives cheaper to hold.

## When it applies

Verbose discovery phases during multi-phase tasks, where the alternative is context window exhaustion partway through the real work.

See [context degradation](context-degradation.md) · [SKILL.md frontmatter](skill-md-frontmatter.md) · [3.4](../tasks/3-4.md)
