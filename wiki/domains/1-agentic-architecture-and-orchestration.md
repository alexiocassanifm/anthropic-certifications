---
title: "Domain 1: Agentic Architecture & Orchestration"
domain: 1
weight: 27
items_at_60: 16
task_statements: 7
---

# Domain 1: Agentic Architecture & Orchestration

**27% of the exam — 16 items at 60. The largest domain, and the one with the most task statements.**

## What this domain is about

How you assemble agents that act. The loop that drives a single agent; the coordinator-subagent topology that drives several; how context crosses the boundary between them; where you enforce order; and how a session survives across time.

The unifying concern is **control**. Every task statement here asks a version of the same question: what decides what happens next — the model, your code, or an accident?

## Task statements

| ID | Title | Core idea |
|---|---|---|
| [1.1](../tasks/1-1.md) | Design and implement agentic loops for autonomous task execution | Loop on `stop_reason`, not on heuristics |
| [1.2](../tasks/1-2.md) | Orchestrate multi-agent systems with coordinator-subagent patterns | Hub-and-spoke; the coordinator owns routing, aggregation, and recovery |
| [1.3](../tasks/1-3.md) | Configure subagent invocation, context passing, and spawning | Subagents inherit nothing; pass context explicitly |
| [1.4](../tasks/1-4.md) | Implement multi-step workflows with enforcement and handoff patterns | Programmatic gates where compliance must be guaranteed |
| [1.5](../tasks/1-5.md) | Apply Agent SDK hooks for tool call interception and data normalization | Intercept results to normalise, intercept calls to enforce |
| [1.6](../tasks/1-6.md) | Design task decomposition strategies for complex workflows | Fixed chaining for predictable work, adaptive decomposition for open-ended work |
| [1.7](../tasks/1-7.md) | Manage session state, resumption, and forking | `--resume`, `fork_session`, and when to start fresh instead |

## The through-lines

**Control flow belongs to `stop_reason`.** The single most testable fact in the domain. Continue while `stop_reason` is `"tool_use"`; finish when it is `"end_turn"`. Everything else — parsing the assistant's prose for a completion signal, capping iterations, checking whether text content appeared — is an anti-pattern the guide names explicitly. See [1.1](../tasks/1-1.md).

**Subagents are isolated by default.** They do not inherit the coordinator's conversation history and they do not share memory between invocations. Every design question about multi-agent context reduces to this: if the subagent needs to know it, you must put it in the prompt. See [1.3](../tasks/1-3.md).

**The coordinator is the hub, deliberately.** All inter-subagent communication routes through it. This looks like overhead until you need observability, consistent error handling, or controlled information flow — which is exactly when the exam asks. Subagents talking directly to each other is always the wrong answer. See [1.2](../tasks/1-2.md).

**Prompts guide; code guarantees.** When identity must be verified before money moves, an instruction is not enough. Prerequisite gates and interception hooks are how you make a sequence non-optional. See [1.4](../tasks/1-4.md), [1.5](../tasks/1-5.md), and [deterministic vs probabilistic](../heuristics/deterministic-vs-probabilistic.md).

**Decomposition quality caps system quality.** A coordinator that partitions "creative industries" into three visual-arts subtasks will produce a coherent, well-cited report that is silently missing music, writing, and film — with every subagent working perfectly. When an item describes good component behaviour and a bad overall result, look upstream at the decomposition. See [1.6](../tasks/1-6.md).

## Where the failures live

The domain's items are largely built from these failure shapes:

- The loop that never terminates, or terminates early, because termination was inferred rather than read
- The subagent that received the task but not the findings, and so invented or omitted
- The synthesis that lost source attribution because the handoff format did not carry it
- The refund processed against an unverified customer because the instruction said "mandatory" and the model, 12% of the time, disagreed
- The report with perfect coverage of the wrong third of the topic
- The resumed session confidently reasoning about files that changed yesterday

## Preparation

The guide's own advice: **build one.** Implement a complete agentic loop with tool calling, error handling, session management, subagent spawning, and explicit context passing. This domain rewards having watched these failures happen more than it rewards reading about them.

The single highest-value exercise is spawning two subagents in **parallel** — multiple `Task` calls emitted in one coordinator response, not across separate turns — and then deliberately breaking one of them to see what the coordinator receives.

## Related

- Scenarios that lean on this domain: [1](../scenarios/1-customer-support-resolution-agent.md), [3](../scenarios/3-multi-agent-research-system.md), [4](../scenarios/4-developer-productivity-with-claude.md)
- [Domain 5](5-context-management-and-reliability.md) is this domain's other half: what happens when the orchestration you designed hits reality
