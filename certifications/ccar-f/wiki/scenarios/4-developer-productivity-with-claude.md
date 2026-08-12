---
title: "Scenario 4: Developer Productivity with Claude"
scenario: 4
primary_domains: [2, 3, 1]
---

# Scenario 4: Developer Productivity with Claude

**Primary domains:** [2 — Tool Design & MCP Integration](../domains/2-tool-design-and-mcp-integration.md) · [3 — Claude Code Configuration & Workflows](../domains/3-claude-code-configuration-and-workflows.md) · [1 — Agentic Architecture & Orchestration](../domains/1-agentic-architecture-and-orchestration.md)

## The situation

Developer productivity tooling built on the Claude Agent SDK. The agent helps engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate, and automate repetitive tasks. It uses the **built-in tools** — Read, Write, Bash, Grep, Glob — and integrates with **MCP servers**.

## What makes this scenario generative

This is the only scenario that names the built-in tools explicitly, which makes it the natural home for [2.5](../tasks/2-5.md). Three details drive the items:

1. **"Explore unfamiliar codebases"** — an unbounded discovery task against a codebase larger than the context window. Tool *selection* and context *management* are both in play.
2. **"Legacy systems"** — code with no documentation and non-obvious structure, where the naive approach (read everything) fails on cost and the smart approach (grep for entry points, follow imports) succeeds.
3. **Built-in tools *and* MCP servers together** — so items can ask which to reach for, and why a well-described MCP tool should beat a generic built-in one.

## Failure modes to expect

| Symptom | Where it points |
|---|---|
| Searching for every caller of a function across the codebase | Grep — content search — [2.5](../tasks/2-5.md) |
| Finding all files matching `**/*.test.tsx` | Glob — path pattern matching — [2.5](../tasks/2-5.md) |
| Edit fails because the anchor text is not unique | Read the full file, then Write — [2.5](../tasks/2-5.md) |
| The agent reads 200 files upfront and exhausts context | Grep for entry points, then Read to follow imports — [2.5](../tasks/2-5.md) |
| Tracing usage across wrapper modules | Identify all exported names first, then search each across the codebase — [2.5](../tasks/2-5.md) |
| Claude uses `Grep` when a far more capable MCP tool exists | The MCP tool's description does not explain its capabilities in enough detail — [2.4](../tasks/2-4.md) |
| Team wants shared MCP tooling without committing a token | `.mcp.json` with `${ENV_VAR}` expansion — [2.4](../tasks/2-4.md) |
| One developer wants an experimental server nobody else gets | User-scoped `~/.claude.json` — [2.4](../tasks/2-4.md) |
| The agent burns tool calls discovering what data even exists | Expose a content catalogue as an MCP **resource** — [2.4](../tasks/2-4.md) |
| Someone proposes building a custom Jira MCP server | Prefer an existing community server for standard integrations — [2.4](../tasks/2-4.md) |
| Verbose exploration output floods the main conversation | Explore subagent, or a skill with `context: fork` — [3.4](../tasks/3-4.md), [3.2](../tasks/3-2.md) |
| A long exploration session starts giving inconsistent answers | Context degradation — scratchpads, `/compact` — [5.4](../tasks/5-4.md) |
| Boilerplate generation keeps missing project conventions | CLAUDE.md and path-scoped rules — [3.1](../tasks/3-1.md), [3.3](../tasks/3-3.md) |
| A repetitive task should be one command for the whole team | Project-scoped slash command in `.claude/commands/` — [3.2](../tasks/3-2.md) |
| An agent given 18 tools picks the wrong one | Scope tools to the role — [2.3](../tasks/2-3.md) |

## The tool-selection table to have memorised

| You need to… | Reach for |
|---|---|
| Find text *inside* files — function names, error strings, imports | **Grep** |
| Find files by *name or extension* pattern | **Glob** |
| Load a whole file | **Read** |
| Replace a unique, identifiable snippet | **Edit** |
| Modify a file where no unique anchor exists | **Read**, then **Write** |
| Run a command | **Bash** |

The exam's framing is *content versus path*. Grep searches contents; Glob matches paths. Everything else follows.

## The incremental-understanding principle

The single most testable idea in this scenario: **build understanding incrementally rather than reading everything upfront.** Start with Grep to find entry points, then Read to follow imports and trace flows. Reading the whole codebase is not thoroughness — it is context exhaustion, and it is a wrong answer every time it appears.

The same principle drives the Explore subagent ([3.4](../tasks/3-4.md)) and subagent delegation for exploration ([5.4](../tasks/5-4.md)): keep the verbose discovery out of the main thread and bring back a summary.

## Task statements most likely to be tested here

[2.4](../tasks/2-4.md) · [2.5](../tasks/2-5.md) · [2.3](../tasks/2-3.md) · [3.1](../tasks/3-1.md) · [3.2](../tasks/3-2.md) · [3.4](../tasks/3-4.md) · [1.3](../tasks/1-3.md) · [5.4](../tasks/5-4.md)

## How to prepare for it

Point Claude Code at a codebase you have never seen and ask it to explain how one feature works end to end. Watch which tools it reaches for and in what order. Then configure an MCP server whose tools overlap with Grep, and see whether a thin description or a detailed one changes which it picks.
