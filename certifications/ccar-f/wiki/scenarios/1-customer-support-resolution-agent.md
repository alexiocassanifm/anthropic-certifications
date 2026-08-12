---
title: "Scenario 1: Customer Support Resolution Agent"
scenario: 1
primary_domains: [1, 2, 5]
---

# Scenario 1: Customer Support Resolution Agent

**Primary domains:** [1 — Agentic Architecture & Orchestration](../domains/1-agentic-architecture-and-orchestration.md) · [2 — Tool Design & MCP Integration](../domains/2-tool-design-and-mcp-integration.md) · [5 — Context Management & Reliability](../domains/5-context-management-and-reliability.md)

## The situation

A customer support resolution agent built on the Claude Agent SDK. It handles high-ambiguity requests — returns, billing disputes, account issues — and reaches backend systems through custom MCP tools: `get_customer`, `lookup_order`, `process_refund`, `escalate_to_human`.

The target is **80%+ first-contact resolution**, while knowing when to escalate.

## What makes this scenario generative

Four things in that description do all the work:

1. **Money moves.** `process_refund` means a wrong decision has financial consequences. That single fact decides every enforcement question in the scenario.
2. **Two lookup tools that sound alike.** `get_customer` and `lookup_order` both retrieve records and both accept identifier-shaped inputs. Misrouting is the obvious failure and it is a *description* problem.
3. **An explicit escalation tool.** Having `escalate_to_human` means escalation is a designed decision with criteria — not a fallback.
4. **A stated numeric target.** 80% first-contact resolution gives items a measurable gap to reason about in either direction: escalating too much *or* too little.

## Failure modes to expect

| Symptom | Where it points |
|---|---|
| The agent skips `get_customer` and refunds against a name-matched account | Prerequisite gate, not a stronger instruction — [1.4](../tasks/1-4.md), [deterministic vs probabilistic](../heuristics/deterministic-vs-probabilistic.md) |
| It calls `get_customer` when the user asks about an order | Tool descriptions lack input formats, examples, and boundaries — [2.1](../tasks/2-1.md) |
| A refund exceeds policy limits | Tool call interception hook that blocks and redirects to escalation — [1.5](../tasks/1-5.md) |
| Backend tools return timestamps in three different formats | `PostToolUse` hook to normalise before the model sees them — [1.5](../tasks/1-5.md) |
| Resolution sits at 55%: escalating simple cases, attempting complex ones | Explicit escalation criteria with few-shot examples — [5.2](../tasks/5-2.md) |
| The refund amount discussed eight turns ago is now "the agreed amount" | Persistent case-facts block outside summarised history — [5.1](../tasks/5-1.md) |
| A customer with three concerns gets one answered | Decompose into distinct items, investigate in parallel on shared context, synthesise — [1.4](../tasks/1-4.md) |
| A human agent receives an escalation with no transcript and no context | Structured handoff: customer ID, root cause, refund amount, recommended action — [1.4](../tasks/1-4.md) |
| `lookup_order` returns 40 fields; context fills with noise | Trim tool output to relevant fields before accumulation — [5.1](../tasks/5-1.md) |
| Two customers match the given name | Ask for another identifier; do not choose heuristically — [5.2](../tasks/5-2.md) |
| A tool fails and the agent retries a permission error forever | Structured errors with `errorCategory` and `isRetryable` — [2.2](../tasks/2-2.md) |

## The escalation nuances

This scenario is where the exam tests escalation *judgment*, and the distinctions are fine:

- **Customer explicitly asks for a human** → escalate immediately. Do not investigate first "to be helpful".
- **Customer is frustrated but the issue is straightforward** → acknowledge the frustration, offer to resolve. Escalate only if they reiterate the preference.
- **Policy is silent or ambiguous** on what they are asking (competitor price matching, when policy covers only own-site adjustments) → escalate. A policy *gap* is an escalation trigger; mere complexity is not.
- **Sentiment analysis** and **self-reported confidence** are both wrong answers here. Neither correlates with case complexity.

## Task statements most likely to be tested here

[1.1](../tasks/1-1.md) · [1.4](../tasks/1-4.md) · [1.5](../tasks/1-5.md) · [2.1](../tasks/2-1.md) · [2.2](../tasks/2-2.md) · [2.3](../tasks/2-3.md) · [5.1](../tasks/5-1.md) · [5.2](../tasks/5-2.md)

## How to prepare for it

Build it, at toy scale. Four tools, two deliberately similar. A loop on `stop_reason`. Structured errors with categories. One hook that blocks a refund over a threshold. Then feed it a multi-concern message — "I want to return this, and I was double-charged, and why is my account locked" — and watch what it does.
