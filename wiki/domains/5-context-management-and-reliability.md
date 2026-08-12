---
title: "Domain 5: Context Management & Reliability"
domain: 5
weight: 15
items_at_60: 9
task_statements: 6
---

# Domain 5: Context Management & Reliability

**15% of the exam — 9 items at 60. The lightest domain by weight, and the easiest to underestimate.**

## What this domain is about

What happens to your architecture over time and under failure. Facts decaying as a conversation is summarised; deciding when a human must take over; failures moving between agents without losing their meaning; exploring a codebase larger than the context window; routing the right work to limited reviewer capacity; and keeping claims attached to their sources through synthesis.

## Why not to skip it

Nine items is the smallest allocation on the exam, but Domain 5 concerns appear *inside* Domain 1 and Domain 2 items as well — because escalation, error propagation, and context passing are how multi-agent systems actually fail in production, and the scenarios are drawn from production. Three of the six exam scenarios list this domain as primary. Its effective footprint is larger than 15%.

## Task statements

| ID | Title | Core idea |
|---|---|---|
| [5.1](../tasks/5-1.md) | Manage conversation context to preserve critical information across long interactions | Persist facts structurally; summaries lose numbers |
| [5.2](../tasks/5-2.md) | Design effective escalation and ambiguity resolution patterns | Explicit criteria; honour stated preferences; policy gaps escalate |
| [5.3](../tasks/5-3.md) | Implement error propagation strategies across multi-agent systems | Structured error context, not generic statuses |
| [5.4](../tasks/5-4.md) | Manage context effectively in large codebase exploration | Subagent delegation, scratchpads, state manifests |
| [5.5](../tasks/5-5.md) | Design human review workflows and confidence calibration | Calibrate against labelled data; segment accuracy by type |
| [5.6](../tasks/5-6.md) | Preserve information provenance and handle uncertainty in multi-source synthesis | Claim-source mappings survive summarisation |

## The through-lines

**Summarisation is lossy in a specific direction: it eats precision.** Amounts, percentages, dates, order numbers, and customer-stated expectations condense into vague prose exactly when they matter most. The fix is structural, not stylistic: extract transactional facts into a persistent "case facts" block included in every prompt, *outside* the summarised history. See [5.1](../tasks/5-1.md).

**Position matters within a long input.** Models process the beginning and end of long inputs reliably and may omit findings from the middle. So put the key findings summary at the top of an aggregated input and organise the detail under explicit section headers. This is a design constraint, not a curiosity. See [5.1](../tasks/5-1.md).

**Tool results consume context out of proportion to their value.** A 40-field order lookup where five fields matter is thirty-five fields of noise repeated every turn. Trim before accumulation. Upstream agents should return structured key facts, citations, and relevance scores — not verbose content and reasoning chains — when downstream agents have limited budgets. See [5.1](../tasks/5-1.md).

**Escalate on the right triggers.** Explicit customer request for a human; a policy gap or exception — not merely a *complex* case; and inability to make meaningful progress. If the customer explicitly asks for a person, honour it immediately without first attempting investigation. If they are frustrated but the issue is within your capability, acknowledge and offer resolution — escalate only if they reiterate. And sentiment and self-reported confidence are both unreliable proxies for complexity. See [5.2](../tasks/5-2.md).

**Ask, do not guess, on ambiguity.** Multiple customer matches means requesting an additional identifier, not picking with a heuristic. See [5.2](../tasks/5-2.md).

**An error is a decision input for the coordinator.** Failure type, the attempted query, any partial results, and possible alternatives let a coordinator retry differently, route around, or proceed and annotate the gap. `"search unavailable"` hides all of that. Two anti-patterns bracket the correct answer: silently returning empty results as success, and terminating the whole workflow on one subagent's failure. Subagents recover locally from transient failures and propagate only what they could not resolve. See [5.3](../tasks/5-3.md).

**Access failure ≠ empty result.** A timed-out search and a successful search with no matches look identical if you flatten them, and they demand opposite responses. Keeping them distinct appears in both [2.2](../tasks/2-2.md) and [5.3](../tasks/5-3.md).

**Context degrades before it runs out.** In long sessions a model starts giving inconsistent answers and referring to "typical patterns" instead of the specific classes it found earlier. Scratchpad files persist key findings across that boundary; subagents keep verbose exploration out of the main thread; a summary injected into a fresh phase beats carrying stale history; state manifests let a coordinator recover after a crash. See [5.4](../tasks/5-4.md).

**Aggregate accuracy hides segment failure.** 97% overall can conceal a document type or a field that performs terribly. Before reducing human review, verify accuracy **by document type and by field**. Calibrate confidence thresholds against a labelled validation set, and keep stratified random sampling of high-confidence extractions running to catch novel error patterns. See [5.5](../tasks/5-5.md).

**Provenance is lost at the summarisation step.** Findings compressed without their claim-source mappings cannot be re-attributed later. Require subagents to emit structured claim-source pairs — URL or document name, relevant excerpt, publication date — and require synthesis to preserve and merge them. Conflicting statistics from credible sources are annotated with attribution, not silently resolved; and publication dates prevent a temporal difference from being read as a contradiction. See [5.6](../tasks/5-6.md).

## Where the failures live

- A refund conversation where the amount became "the discussed amount" three summaries ago
- An agent that investigated for six turns after the customer said "let me talk to a person"
- A coordinator that received "search unavailable" and had no basis for any decision
- A research report that silently dropped a subtopic because a source was unreachable
- A 97%-accurate extraction pipeline that is 61% accurate on scanned invoices
- A synthesis that picked one of two conflicting statistics, with no record that the other existed

## Preparation

Practise extracting structured facts from verbose tool output, keeping scratchpad files across a long session, and delegating exploration to subagents. Then take an escalation policy and write explicit criteria with few-shot examples for the boundary cases — the ones where the customer is frustrated but the issue is simple, and where policy is silent rather than restrictive.

## Related

- Scenarios: [1](../scenarios/1-customer-support-resolution-agent.md), [2](../scenarios/2-code-generation-with-claude-code.md), [3](../scenarios/3-multi-agent-research-system.md), [6](../scenarios/6-structured-data-extraction.md)
- [Domain 1](1-agentic-architecture-and-orchestration.md) — this domain is what its orchestration hits when it meets reality
