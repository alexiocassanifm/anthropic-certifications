---
title: Structured error context
domain: 5
tasks: ["5.3"]
verified: "2026-08-12"
---

# Structured error context

What a coordinator needs from a failing subagent in order to recover intelligently. **Four things travel with the failure:**

1. **Failure type**
2. **What was attempted** — the query
3. **Partial results**
4. **Potential alternative approaches**

With those, the coordinator can retry with a modified query, route around, or proceed with partial results and annotate the gap. With `"search unavailable"`, it can do none of them.

## Coverage annotations

Synthesis output should carry **coverage annotations** indicating which findings are well-supported and which topic areas have gaps due to unavailable sources. A report with a silent gap reads as complete.

## The two bracketing anti-patterns

| Anti-pattern | Failure |
|---|---|
| Silently returning empty results as success | Suppresses the error entirely; risks confidently incomplete output |
| Terminating the whole workflow on one failure | Kills work that could have succeeded |

The right answer lives between them: **local recovery for transient failures, structured propagation for what cannot be resolved.**

See [access failure vs empty result](access-failure-vs-empty-result.md) · [MCP structured errors](mcp-errors.md) · [5.3](../tasks/5-3.md)
