---
title: CCAR-F Wiki
---

# CCAR-F Wiki

The knowledge base for **Claude Certified Architect – Foundations**. Everything is plain Markdown with relative links, so it renders on GitHub and navigates in Obsidian.

Written against *Exam Guide v1.0, July 2026*. This kit is unofficial — see [DISCLAIMER.md](../DISCLAIMER.md).

## Start here

1. [Exam blueprint](exam/blueprint.md) — domains, weights, the 30 task statements
2. [Out of scope](exam/out-of-scope.md) — what you can stop studying
3. [Heuristics](#heuristics) — the reasoning patterns that decide most items
4. [Preparation plan](exam/preparation-plan.md) — a 3-week schedule

## Exam

| Note | What it covers |
|---|---|
| [Blueprint](exam/blueprint.md) | Format, domain weights, task statement index, scenario index |
| [Format and scoring](exam/format-and-scoring.md) | Item types, timing, criterion-referenced scoring, retakes, recertification |
| [Out of scope](exam/out-of-scope.md) | The explicit not-tested list, and the distinctions that catch people |
| [Drift log](exam/drift-log.md) | Where current documentation differs from the exam guide — **read before exam day** |
| [Logistics](exam/logistics.md) | Registration, ID, accommodations, exam-day rules, NDA, appeals |
| [Preparation plan](exam/preparation-plan.md) | Week-by-week schedule and readiness signals |

## Heuristics

Cross-domain reasoning patterns. Read these before the domains — they generalise, and they predict more answers than any single fact.

| Note | The rule |
|---|---|
| [Cheapest fix at root cause](heuristics/cheapest-fix-at-root-cause.md) | Prefer the least elaborate intervention that addresses the *stated* root cause |
| [Deterministic vs probabilistic](heuristics/deterministic-vs-probabilistic.md) | When compliance must be guaranteed, enforce it in code, not in a prompt |
| [Least-privilege tooling](heuristics/least-privilege-tooling.md) | Give each agent the tools its role needs, and no more |

## Domains

| # | Domain | Weight | Items at 60 |
|---|---|---|---|
| 1 | [Agentic Architecture & Orchestration](domains/1-agentic-architecture-and-orchestration.md) | 27% | 16 |
| 2 | [Tool Design & MCP Integration](domains/2-tool-design-and-mcp-integration.md) | 18% | 11 |
| 3 | [Claude Code Configuration & Workflows](domains/3-claude-code-configuration-and-workflows.md) | 20% | 12 |
| 4 | [Prompt Engineering & Structured Output](domains/4-prompt-engineering-and-structured-output.md) | 20% | 12 |
| 5 | [Context Management & Reliability](domains/5-context-management-and-reliability.md) | 15% | 9 |

## Task statements

The core study unit. One note each, all 30.

**Domain 1** · [1.1](tasks/1-1.md) agentic loops · [1.2](tasks/1-2.md) coordinator-subagent · [1.3](tasks/1-3.md) subagent invocation & context · [1.4](tasks/1-4.md) enforcement & handoff · [1.5](tasks/1-5.md) hooks · [1.6](tasks/1-6.md) task decomposition · [1.7](tasks/1-7.md) sessions

**Domain 2** · [2.1](tasks/2-1.md) tool interfaces · [2.2](tasks/2-2.md) structured errors · [2.3](tasks/2-3.md) tool distribution & choice · [2.4](tasks/2-4.md) MCP integration · [2.5](tasks/2-5.md) built-in tools

**Domain 3** · [3.1](tasks/3-1.md) CLAUDE.md hierarchy · [3.2](tasks/3-2.md) commands & skills · [3.3](tasks/3-3.md) path-specific rules · [3.4](tasks/3-4.md) plan mode · [3.5](tasks/3-5.md) iterative refinement · [3.6](tasks/3-6.md) CI/CD

**Domain 4** · [4.1](tasks/4-1.md) explicit criteria · [4.2](tasks/4-2.md) few-shot · [4.3](tasks/4-3.md) tool use & JSON Schema · [4.4](tasks/4-4.md) validation & retry · [4.5](tasks/4-5.md) batch processing · [4.6](tasks/4-6.md) multi-pass review

**Domain 5** · [5.1](tasks/5-1.md) context preservation · [5.2](tasks/5-2.md) escalation · [5.3](tasks/5-3.md) error propagation · [5.4](tasks/5-4.md) codebase exploration · [5.5](tasks/5-5.md) human review & confidence · [5.6](tasks/5-6.md) provenance & uncertainty

## Scenarios

Four of these six frame your exam.

1. [Customer Support Resolution Agent](scenarios/1-customer-support-resolution-agent.md) — domains 1, 2, 5
2. [Code Generation with Claude Code](scenarios/2-code-generation-with-claude-code.md) — domains 3, 5
3. [Multi-Agent Research System](scenarios/3-multi-agent-research-system.md) — domains 1, 2, 5
4. [Developer Productivity with Claude](scenarios/4-developer-productivity-with-claude.md) — domains 2, 3, 1
5. [Claude Code for Continuous Integration](scenarios/5-claude-code-for-continuous-integration.md) — domains 3, 4
6. [Structured Data Extraction](scenarios/6-structured-data-extraction.md) — domains 4, 5

## Concepts

Atomic notes on the tested technology surface — `stop_reason`, `tool_choice`, `.claude/rules/`, MCP `isError`, the Message Batches API, and the rest. Browse [`concepts/`](concepts/), or reach them from the task statement that needs them.

## Practising

The wiki teaches; the [question bank](../questions/) tests. In Claude Code:

```
/study 1.4          learn one task statement
/quiz --domain 2    short targeted quiz
/mock-exam          full 60-item timed simulation
/progress           readiness dashboard
/drill              spaced repetition on weak areas
/refresh-kb         re-verify this wiki against current official docs
```

## Keeping this accurate

Every note carries a `verified` date. The technical claims were checked against
official documentation on the date shown, and divergence from the exam guide is
recorded in the [drift log](exam/drift-log.md) rather than silently corrected —
because the guide, not current documentation, is what the exam was written
against.

Run `/refresh-kb` to re-check. It is worth doing once before exam day, and
whenever Claude Code or the Agent SDK ships something that touches Domain 3.
