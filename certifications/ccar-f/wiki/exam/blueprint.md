---
title: Exam Blueprint
guide_version: "1.0"
guide_date: "July 2026"
exam_code: CCAR-F
---

# Exam Blueprint

Source: *Claude Certified Architect – Foundations Exam Guide v1.0, July 2026, exam code CCAR-F*.

If you are holding a newer guide version, check the weights below before trusting anything else in this repository.

## Format

| | |
|---|---|
| Items | 60 |
| Item types | Multiple-choice and multiple-response. Each item states how many responses to select. |
| Structure | 4 scenarios, drawn at random from a bank of 6 |
| Time | 120 minutes |
| Delivery | Proctored — online or at a test centre |
| Passing score | Scaled 720, on a 100–1,000 range |
| Fee | $125 USD |
| Validity | 12 months |
| Result | Pass/fail with scaled score, plus percent-correct by domain |

120 minutes for 60 items is **two minutes per item**. That is comfortable for a recall question and tight for a five-line scenario stem with four dense options. Practice reading stems quickly, and see [format-and-scoring.md](format-and-scoring.md) for what the score report actually tells you.

## Domain weights

| # | Domain | Weight | Items at 60 | Task statements |
|---|---|---|---|---|
| 1 | [Agentic Architecture & Orchestration](../domains/1-agentic-architecture-and-orchestration.md) | 27% | 16 | 7 |
| 2 | [Tool Design & MCP Integration](../domains/2-tool-design-and-mcp-integration.md) | 18% | 11 | 5 |
| 3 | [Claude Code Configuration & Workflows](../domains/3-claude-code-configuration-and-workflows.md) | 20% | 12 | 6 |
| 4 | [Prompt Engineering & Structured Output](../domains/4-prompt-engineering-and-structured-output.md) | 20% | 12 | 6 |
| 5 | [Context Management & Reliability](../domains/5-context-management-and-reliability.md) | 15% | 9 | 6 |
| | **Total** | **100%** | **60** | **30** |

Item counts are the weights applied to 60 and rounded to sum exactly to 60. They are what `scripts/build_exam.py` targets. The real exam's per-domain counts are not published item-by-item; treat these as a faithful approximation, not a guarantee.

### What the weights mean for your time

Domain 1 alone is more than a quarter of the exam and has the most task statements (7). Domains 1+3+4 together are **67%**. If you have limited time, that is the order.

Domain 5 is the lightest at 15%, but it is deceptive: context management and reliability show up *inside* Domain 1 and Domain 2 items as well, because escalation, error propagation, and context passing are how multi-agent systems actually fail. Do not skip it.

## Task statement index

### Domain 1 — Agentic Architecture & Orchestration (27%)

| ID | Task statement |
|---|---|
| [1.1](../tasks/1-1.md) | Design and implement agentic loops for autonomous task execution |
| [1.2](../tasks/1-2.md) | Orchestrate multi-agent systems with coordinator-subagent patterns |
| [1.3](../tasks/1-3.md) | Configure subagent invocation, context passing, and spawning |
| [1.4](../tasks/1-4.md) | Implement multi-step workflows with enforcement and handoff patterns |
| [1.5](../tasks/1-5.md) | Apply Agent SDK hooks for tool call interception and data normalization |
| [1.6](../tasks/1-6.md) | Design task decomposition strategies for complex workflows |
| [1.7](../tasks/1-7.md) | Manage session state, resumption, and forking |

### Domain 2 — Tool Design & MCP Integration (18%)

| ID | Task statement |
|---|---|
| [2.1](../tasks/2-1.md) | Design effective tool interfaces with clear descriptions and boundaries |
| [2.2](../tasks/2-2.md) | Implement structured error responses for MCP tools |
| [2.3](../tasks/2-3.md) | Distribute tools appropriately across agents and configure tool choice |
| [2.4](../tasks/2-4.md) | Integrate MCP servers into Claude Code and agent workflows |
| [2.5](../tasks/2-5.md) | Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively |

### Domain 3 — Claude Code Configuration & Workflows (20%)

| ID | Task statement |
|---|---|
| [3.1](../tasks/3-1.md) | Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization |
| [3.2](../tasks/3-2.md) | Create and configure custom slash commands and skills |
| [3.3](../tasks/3-3.md) | Apply path-specific rules for conditional convention loading |
| [3.4](../tasks/3-4.md) | Determine when to use plan mode vs direct execution |
| [3.5](../tasks/3-5.md) | Apply iterative refinement techniques for progressive improvement |
| [3.6](../tasks/3-6.md) | Integrate Claude Code into CI/CD pipelines |

### Domain 4 — Prompt Engineering & Structured Output (20%)

| ID | Task statement |
|---|---|
| [4.1](../tasks/4-1.md) | Design prompts with explicit criteria to improve precision and reduce false positives |
| [4.2](../tasks/4-2.md) | Apply few-shot prompting to improve output consistency and quality |
| [4.3](../tasks/4-3.md) | Enforce structured output using tool use and JSON schemas |
| [4.4](../tasks/4-4.md) | Implement validation, retry, and feedback loops for extraction quality |
| [4.5](../tasks/4-5.md) | Design efficient batch processing strategies |
| [4.6](../tasks/4-6.md) | Design multi-instance and multi-pass review architectures |

### Domain 5 — Context Management & Reliability (15%)

| ID | Task statement |
|---|---|
| [5.1](../tasks/5-1.md) | Manage conversation context to preserve critical information across long interactions |
| [5.2](../tasks/5-2.md) | Design effective escalation and ambiguity resolution patterns |
| [5.3](../tasks/5-3.md) | Implement error propagation strategies across multi-agent systems |
| [5.4](../tasks/5-4.md) | Manage context effectively in large codebase exploration |
| [5.5](../tasks/5-5.md) | Design human review workflows and confidence calibration |
| [5.6](../tasks/5-6.md) | Preserve information provenance and handle uncertainty in multi-source synthesis |

## Scenarios

Four of these six frame your exam. Each is a production context that a cluster of items refers back to.

| # | Scenario | Primary domains |
|---|---|---|
| [1](../scenarios/1-customer-support-resolution-agent.md) | Customer Support Resolution Agent | 1, 2, 5 |
| [2](../scenarios/2-code-generation-with-claude-code.md) | Code Generation with Claude Code | 3, 5 |
| [3](../scenarios/3-multi-agent-research-system.md) | Multi-Agent Research System | 1, 2, 5 |
| [4](../scenarios/4-developer-productivity-with-claude.md) | Developer Productivity with Claude | 2, 3, 1 |
| [5](../scenarios/5-claude-code-for-continuous-integration.md) | Claude Code for Continuous Integration | 3, 4 |
| [6](../scenarios/6-structured-data-extraction.md) | Structured Data Extraction | 4, 5 |

Note the asymmetry: Domain 1 and Domain 5 appear as primary domains in three scenarios each; Domain 4 in only two. This is why a mock exam cannot be both scenario-faithful and weight-exact — see the allocation rule in `.claude/skills/mock-exam/SKILL.md`.

## Where to go next

- [format-and-scoring.md](format-and-scoring.md) — how you are scored, and why this kit does not fake a scaled score
- [out-of-scope.md](out-of-scope.md) — what is explicitly *not* tested
- [preparation-plan.md](preparation-plan.md) — a 3-week schedule
- [../heuristics/](../heuristics/) — the reasoning patterns that generalise across domains
