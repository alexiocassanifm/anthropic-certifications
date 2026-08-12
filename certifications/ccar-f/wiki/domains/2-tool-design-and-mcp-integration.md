---
title: "Domain 2: Tool Design & MCP Integration"
domain: 2
weight: 18
items_at_60: 11
task_statements: 5
---

# Domain 2: Tool Design & MCP Integration

**18% of the exam — 11 items at 60. The smallest domain by item count, but the one whose failures cascade furthest.**

## What this domain is about

The interface between the model and everything outside it. How a tool describes itself, how it reports failure, who gets access to it, how MCP servers are wired into Claude Code and agent workflows, and when to reach for a built-in tool rather than building something.

The unifying idea: **the tool description is not documentation, it is the routing table.** It is the primary mechanism the model uses to choose. Treat it as an implementation detail and selection becomes unreliable — not occasionally, but structurally.

## Task statements

| ID | Title | Core idea |
|---|---|---|
| [2.1](../tasks/2-1.md) | Design effective tool interfaces with clear descriptions and boundaries | Descriptions drive selection; ambiguity causes misrouting |
| [2.2](../tasks/2-2.md) | Implement structured error responses for MCP tools | `isError` plus category, retryability, and a human-readable reason |
| [2.3](../tasks/2-3.md) | Distribute tools appropriately across agents and configure tool choice | Scope by role; `tool_choice` for guarantees |
| [2.4](../tasks/2-4.md) | Integrate MCP servers into Claude Code and agent workflows | Project vs user scope, env var expansion, resources vs tools |
| [2.5](../tasks/2-5.md) | Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively | Grep for content, Glob for paths, Read+Write when Edit cannot anchor |

## The through-lines

**A weak description is a root cause, not a symptom.** When an agent calls `get_customer` for an order lookup because both tools say one vague line, the fix is the description — input formats, example queries, edge cases, and an explicit boundary against the similar tool. Few-shot examples would help but add token overhead without addressing the cause; a routing layer is over-engineering that discards the model's language understanding. See [2.1](../tasks/2-1.md) and [cheapest fix at the root cause](../heuristics/cheapest-fix-at-root-cause.md).

**Errors are information for a decision-maker.** A generic `"Operation failed"` tells the agent nothing about whether to retry, try another approach, or explain to the user. Structured metadata — `errorCategory` (transient / validation / business / permission), an `isRetryable` boolean, a human-readable description — is what makes recovery possible. And a business rule violation should carry `retryable: false` plus a customer-friendly explanation, because the agent's next move is to *communicate*, not to retry. See [2.2](../tasks/2-2.md).

**Breadth degrades selection.** Eighteen tools instead of four or five does not make an agent more capable; it makes tool choice less reliable. Scope each agent to its role, and add narrow cross-role tools only for proven high-frequency needs. See [2.3](../tasks/2-3.md) and [least-privilege tooling](../heuristics/least-privilege-tooling.md).

**Scope is the MCP configuration question.** Project-level `.mcp.json` for shared team tooling, committed to version control with `${ENV_VAR}` expansion so no secret is committed. User-level `~/.claude.json` for personal and experimental servers. Both are active at once, and tools from all configured servers are discovered at connection time. See [2.4](../tasks/2-4.md).

**Resources are for catalogues; tools are for actions.** Exposing issue summaries, documentation hierarchies, or database schemas as MCP **resources** gives an agent visibility into what exists without burning exploratory tool calls to find out. This distinction is easy to miss and easy to test. See [2.4](../tasks/2-4.md).

**Built-in tool selection follows the shape of the question.** Searching *contents* → Grep. Finding files by *name pattern* → Glob. Targeted edit with a unique anchor → Edit; when no unique anchor exists → Read then Write. Building understanding of an unfamiliar codebase → Grep for entry points, then Read to follow imports — not reading everything upfront. See [2.5](../tasks/2-5.md).

## Where the failures live

- Two tools with near-identical descriptions, and 12% misrouting nobody notices until an incident
- A system prompt whose keyword-sensitive wording quietly overrides a well-written tool description
- An agent retrying a permission error forever because every failure looks the same
- A subagent that "successfully" returned empty results, when in fact its search timed out
- A synthesis agent doing its own web searches because it was given the tools to
- A secret committed in `.mcp.json` because someone inlined a token instead of expanding an env var
- Claude preferring `Grep` over a far more capable MCP tool, because the MCP tool's description did not explain what it could do

## Preparation

Write three or four MCP tools where at least two are deliberately similar, then test selection reliability with realistic ambiguous requests. Add structured errors with categories and retryable flags, and verify the agent behaves differently for each category — retrying transient failures, explaining business errors, and not retrying permission errors.

## Related

- Scenarios: [1](../scenarios/1-customer-support-resolution-agent.md), [3](../scenarios/3-multi-agent-research-system.md), [4](../scenarios/4-developer-productivity-with-claude.md)
- [Domain 1](1-agentic-architecture-and-orchestration.md) — tool distribution across subagents overlaps heavily
- [Domain 5](5-context-management-and-reliability.md) — error propagation continues where structured errors leave off
