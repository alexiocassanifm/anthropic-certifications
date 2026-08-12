---
title: Task decomposition
domain: 1
tasks: ["1.2", "1.6"]
verified: "2026-08-12"
---

# Task decomposition

## Two patterns

| Pattern | Use when | Example |
|---|---|---|
| **Prompt chaining** (fixed sequential) | The steps are known before you start | Per-file review passes, then a cross-file integration pass |
| **Dynamic adaptive** | Findings at each step determine the next subtasks | "Add comprehensive tests to a legacy codebase" |

The choice is decided by one question: **do you know the shape of the work in advance?**

## Partitioning across agents

Assign **distinct subtopics or source types** to each subagent, to minimise duplication. And keep partitions wide enough to cover the actual topic — narrow decomposition produces polished, incomplete output with every component working correctly.

## Iterative refinement

The coordinator evaluates synthesis output for gaps, re-delegates to search and analysis with **targeted** queries, and re-invokes synthesis until coverage is sufficient. Accepting the first pass is a recognisable wrong answer.

## Attention dilution

Analysing many files in one pass produces inconsistent depth and contradictory findings. This is a **quality** problem, not a **capacity** problem — a larger context window does not fix it. Splitting into focused passes does.

See [attention dilution in review](multi-pass-review.md) · [1.6](../tasks/1-6.md)
