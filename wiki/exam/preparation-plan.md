---
title: Preparation Plan
---

# Preparation Plan

A three-week schedule assuming ~8 hours a week and existing hands-on experience with Claude. Compress or stretch it, but keep the **order** — it front-loads the heaviest domains and leaves the last week for weakness repair rather than first exposure.

## Before you start

1. Read [blueprint.md](blueprint.md) — know the weights.
2. Read [out-of-scope.md](out-of-scope.md) — know the boundary. This one page saves hours.
3. Read all three [heuristics](../heuristics/) notes. They are short and they generalise; every domain's items are decided by them.
4. Run a **cold** `/mock-exam` before studying anything. A 45% baseline you can name is more useful than a vague sense of readiness, and the per-domain breakdown tells you where week 3 will go.

## Week 1 — Agentic architecture and tool design (45% of the exam)

**Domain 1 (27%)** — 7 task statements, the largest block on the exam.

| Day | Work |
|---|---|
| 1 | [1.1](../tasks/1-1.md) agentic loops, [1.2](../tasks/1-2.md) coordinator-subagent. `/quiz --task 1.1 --task 1.2` |
| 2 | [1.3](../tasks/1-3.md) subagent invocation and context passing, [1.4](../tasks/1-4.md) enforcement and handoff |
| 3 | [1.5](../tasks/1-5.md) hooks, [1.6](../tasks/1-6.md) task decomposition, [1.7](../tasks/1-7.md) sessions |
| 4 | **Domain 2 (18%)**: [2.1](../tasks/2-1.md) tool interfaces, [2.2](../tasks/2-2.md) structured errors |
| 5 | [2.3](../tasks/2-3.md) tool distribution and `tool_choice`, [2.4](../tasks/2-4.md) MCP integration, [2.5](../tasks/2-5.md) built-in tools |
| — | Close the week with `/quiz --domain 1` and `/quiz --domain 2` |

**Hands-on that pays off here** (from the guide's own preparation exercises): build a small agent with 3–4 MCP tools, at least two of them deliberately similar, and watch it misroute. Implement the loop on `stop_reason`. Add structured errors with `errorCategory` and `isRetryable`. Add one hook that blocks a tool call above a threshold. Nothing teaches [2.1](../tasks/2-1.md) like watching an agent pick `analyze_content` when you meant `extract_web_results`.

## Week 2 — Claude Code and prompting (40% of the exam)

| Day | Work |
|---|---|
| 1 | **Domain 3 (20%)**: [3.1](../tasks/3-1.md) CLAUDE.md hierarchy, [3.2](../tasks/3-2.md) commands and skills |
| 2 | [3.3](../tasks/3-3.md) path-specific rules, [3.4](../tasks/3-4.md) plan mode vs direct execution |
| 3 | [3.5](../tasks/3-5.md) iterative refinement, [3.6](../tasks/3-6.md) CI/CD integration |
| 4 | **Domain 4 (20%)**: [4.1](../tasks/4-1.md) explicit criteria, [4.2](../tasks/4-2.md) few-shot, [4.3](../tasks/4-3.md) tool use + JSON Schema |
| 5 | [4.4](../tasks/4-4.md) validation and retry, [4.5](../tasks/4-5.md) batch processing, [4.6](../tasks/4-6.md) multi-pass review |
| — | `/quiz --domain 3` and `/quiz --domain 4` |

**Hands-on:** configure a real project. Project-level `CLAUDE.md`, a `.claude/rules/` file with a `paths:` glob, one skill with `context: fork` and `allowed-tools`, one MCP server in `.mcp.json` with `${ENV_VAR}` expansion plus a personal one in `~/.claude.json`. Then run the same task in plan mode and in direct execution and notice where plan mode earned its cost. Domain 3 is the most *verifiable* domain — you can check every fact on your own machine in an afternoon.

## Week 3 — Reliability, scenarios, and repair

| Day | Work |
|---|---|
| 1 | **Domain 5 (15%)**: [5.1](../tasks/5-1.md) context preservation, [5.2](../tasks/5-2.md) escalation |
| 2 | [5.3](../tasks/5-3.md) error propagation, [5.4](../tasks/5-4.md) large codebase exploration |
| 3 | [5.5](../tasks/5-5.md) human review and confidence, [5.6](../tasks/5-6.md) provenance and uncertainty |
| 4 | Read all six [scenarios](../scenarios/) end to end. For each, ask yourself which failure modes it invites — that is how items are built. |
| 5 | Full `/mock-exam` under timed conditions. Then `/progress`, and study only what it flags. |
| 6–7 | `/drill` on weak task statements. Re-read the [heuristics](../heuristics/). Second `/mock-exam` if time allows. |

## The last 48 hours

Do not learn anything new. Instead:

- Re-read the three [heuristics](../heuristics/) notes.
- Re-read the **Anti-patterns** section of every task statement note you scored below 70% on. The exam's wrong answers are drawn from anti-patterns far more often than from obscure facts.
- Re-read [out-of-scope.md](out-of-scope.md), so you do not talk yourself into an answer built on untested material.
- Check [logistics.md](logistics.md): ID name matches registration, workspace clear, quiet room booked.

## If you have one week, not three

Do this and accept the risk:

1. All three [heuristics](../heuristics/) notes.
2. Domain 1 and Domain 3 in full (47% of the exam, and the two most learnable domains).
3. The **Anti-patterns** and **Exam angle** sections only, for Domains 2, 4, and 5.
4. One full `/mock-exam`, then `/drill` on whatever it exposes.

## Signals you are ready

- `/mock-exam` overall consistently **above 80%**, on a form you have not seen before
- **No domain below 70%** — the weights mean a collapsed Domain 1 cannot be rescued by a strong Domain 5
- You can state, without looking, why prompt-based enforcement loses to a hook when money is involved, and why an over-engineered classifier loses to a better tool description
- You finish 60 items in under 110 minutes

If your overall is 85% but Domain 2 sits at 55%, you are not ready. Fix the floor, not the average.
