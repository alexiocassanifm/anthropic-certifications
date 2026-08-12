---
title: "Scenario 3: Multi-Agent Research System"
scenario: 3
primary_domains: [1, 2, 5]
---

# Scenario 3: Multi-Agent Research System

**Primary domains:** [1 — Agentic Architecture & Orchestration](../domains/1-agentic-architecture-and-orchestration.md) · [2 — Tool Design & MCP Integration](../domains/2-tool-design-and-mcp-integration.md) · [5 — Context Management & Reliability](../domains/5-context-management-and-reliability.md)

## The situation

A multi-agent research system on the Claude Agent SDK. A **coordinator** delegates to specialised subagents: one searches the web, one analyses documents, one synthesises findings, one generates reports. The system researches topics and produces comprehensive, **cited** reports.

## What makes this scenario generative

This is the richest scenario on the exam. Four agents in a pipeline gives you three handoff boundaries, and every boundary is a place where information can be lost, duplicated, or misattributed.

Four details carry the weight:

1. **A coordinator with four specialists** — every question about delegation, partitioning, parallelism, and routing lives here.
2. **"Comprehensive"** — coverage is a stated requirement, so incomplete coverage is a defect the items can point at.
3. **"Cited"** — provenance must survive three handoffs, including a summarisation step that naturally destroys it.
4. **Web search** — an unreliable dependency. Timeouts and empty results are guaranteed, so error propagation is in scope by construction.

## Failure modes to expect

| Symptom | Where it points |
|---|---|
| Every subagent works correctly, but the report misses a third of the topic | Coordinator decomposition too narrow — [1.6](../tasks/1-6.md), [1.2](../tasks/1-2.md) |
| Two subagents research the same ground | Partition scope by subtopic or source type — [1.2](../tasks/1-2.md) |
| The synthesis subagent has no idea what the search agent found | Subagents inherit nothing; pass findings in the prompt — [1.3](../tasks/1-3.md) |
| The coordinator cannot spawn subagents at all | `allowedTools` must include `Task` — [1.3](../tasks/1-3.md) |
| Subagents run one after another; latency is 4× what it needs to be | Emit multiple `Task` calls in a **single** coordinator response — [1.3](../tasks/1-3.md) |
| Web search times out and the coordinator gets `"search unavailable"` | Structured error context: failure type, attempted query, partial results, alternatives — [5.3](../tasks/5-3.md) |
| A subagent returns empty results marked successful after a timeout | Access failure ≠ valid empty result — [5.3](../tasks/5-3.md), [2.2](../tasks/2-2.md) |
| One subagent failure kills the whole workflow | Local recovery for transient failures; propagate only the unresolvable — [5.3](../tasks/5-3.md) |
| Citations are gone by the time the report is written | Structured claim-source mappings preserved through synthesis — [5.6](../tasks/5-6.md) |
| Two credible sources give different statistics; the report shows one | Annotate the conflict with attribution; do not silently pick — [5.6](../tasks/5-6.md) |
| A 2023 figure and a 2025 figure are reported as a contradiction | Require publication dates in structured output — [5.6](../tasks/5-6.md) |
| The synthesis agent starts doing its own web searches | It was given tools outside its specialisation — [2.3](../tasks/2-3.md) |
| Verification round-trips through the coordinator add 40% latency | A scoped `verify_fact` tool for the simple 85%; complex cases still delegate — [2.3](../tasks/2-3.md), [least-privilege tooling](../heuristics/least-privilege-tooling.md) |
| Synthesis findings are coherent but shallow, with gaps unacknowledged | Iterative refinement: coordinator evaluates for gaps, re-delegates, re-synthesises — [1.2](../tasks/1-2.md) |
| The synthesis agent's context fills with verbose upstream reasoning | Upstream returns structured key facts and citations, not prose — [5.1](../tasks/5-1.md) |

## The diagnostic move this scenario rewards

When an item says *"each subagent completes successfully"* and then describes a bad overall result, **look upstream at the coordinator**, not at the agent nearest the symptom. Every downstream agent doing exactly what it was told, on a badly partitioned task, produces a polished and incomplete answer. Blaming the search agent's queries or the synthesis agent's gap detection is the designed trap — see the `blames-wrong-component` family in [`question-style-guide.md`](../../questions/question-style-guide.md).

## The design principles to have ready

- **Coordinator prompts specify goals and quality criteria**, not step-by-step procedure — that is what lets subagents adapt.
- **Dynamic subagent selection** beats always routing through the full pipeline. A simple query does not need all four.
- **Structured formats separate content from metadata** (source URLs, document names, page numbers) so attribution survives the handoff.
- **All communication routes through the coordinator** — for observability, consistent error handling, controlled information flow. Subagent-to-subagent links are always wrong here.
- **Coverage annotations** in synthesis output: which findings are well-supported, and which areas have gaps because a source was unreachable.

## Task statements most likely to be tested here

[1.2](../tasks/1-2.md) · [1.3](../tasks/1-3.md) · [1.6](../tasks/1-6.md) · [2.2](../tasks/2-2.md) · [2.3](../tasks/2-3.md) · [5.1](../tasks/5-1.md) · [5.3](../tasks/5-3.md) · [5.6](../tasks/5-6.md)

## How to prepare for it

Build a coordinator with two subagents, ensure `allowedTools` includes `Task`, and pass findings explicitly. Then break things deliberately: simulate a subagent timeout and check what the coordinator actually receives; feed it two sources with conflicting statistics and see whether both survive into the output with attribution.
