---
title: "Scenario 2: Code Generation with Claude Code"
scenario: 2
primary_domains: [3, 5]
---

# Scenario 2: Code Generation with Claude Code

**Primary domains:** [3 — Claude Code Configuration & Workflows](../domains/3-claude-code-configuration-and-workflows.md) · [5 — Context Management & Reliability](../domains/5-context-management-and-reliability.md)

## The situation

A team using Claude Code to accelerate software development — code generation, refactoring, debugging, documentation. The work is to integrate it into the development workflow with custom slash commands and CLAUDE.md configuration, and to know when to use plan mode versus direct execution.

## What makes this scenario generative

This is the **narrowest** of the six scenarios: only two primary domains, and one of them dominates. It is also the most *checkable* — every fact it tests can be verified on a laptop, which makes it the best return on study time.

Three tensions drive the items:

1. **Team versus individual.** "A team uses it" means scope questions: who receives which instruction, and why did it work for one developer and not the others.
2. **Plan mode versus direct execution.** Named explicitly in the scenario, so expect items that give you a task and ask which mode fits.
3. **Long sessions.** Domain 5 is a primary domain here because refactoring and debugging sessions run long, and context degrades before it exhausts.

## Failure modes to expect

| Symptom | Where it points |
|---|---|
| A new team member does not receive the team's conventions | They live in `~/.claude/CLAUDE.md`, which is not shared — [3.1](../tasks/3-1.md) |
| A shared `/review` command needs to reach everyone who clones | `.claude/commands/` in the repository, version-controlled — [3.2](../tasks/3-2.md) |
| Test conventions must apply to test files scattered across the tree | `.claude/rules/` with a `paths:` glob, not directory CLAUDE.md files — [3.3](../tasks/3-3.md) |
| CLAUDE.md has grown monolithic and unfocused | Split into `.claude/rules/` topic files, or use `@import` — [3.1](../tasks/3-1.md) |
| Behaviour differs inconsistently between sessions | `/memory` to verify which memory files actually loaded — [3.1](../tasks/3-1.md) |
| A monolith-to-microservices restructure across dozens of files | Plan mode: architectural decisions, multiple valid approaches — [3.4](../tasks/3-4.md) |
| A single-file bug fix with a clear stack trace | Direct execution; plan mode is overhead — [3.4](../tasks/3-4.md) |
| A codebase-analysis skill floods the main conversation with output | `context: fork` in the skill frontmatter — [3.2](../tasks/3-2.md) |
| A prose description of a transformation gets interpreted inconsistently | Give 2–3 concrete input/output examples — [3.5](../tasks/3-5.md) |
| Edge cases keep breaking after each fix | Test-driven iteration: write the suite first, then share failures — [3.5](../tasks/3-5.md) |
| Working in an unfamiliar domain with unknown design considerations | The interview pattern: have Claude ask questions before implementing — [3.5](../tasks/3-5.md) |
| Long exploration session: answers turn vague, references "typical patterns" | Context degradation — scratchpads, subagent delegation, `/compact` — [5.4](../tasks/5-4.md) |
| Resuming a session after the files were modified | Tell it what changed for targeted re-analysis; or start fresh with a summary if tool results are stale — [1.7](../tasks/1-7.md) |

## The distinctions to have ready

**Skills versus CLAUDE.md.** On-demand task-specific workflow versus always-loaded universal standard. The question is *when the content is needed*, not how important it is.

**Directory CLAUDE.md versus glob-scoped rules.** Location-bound versus type-bound. Test files next to the code they test (`Button.test.tsx` beside `Button.tsx`) are the canonical case where globs win and per-directory files cannot.

**Sequential versus batched feedback.** Independent problems: fix them one at a time. Interacting problems where fixes affect each other: put them all in a single detailed message.

**Resume versus fresh start.** Resume when prior context is mostly still valid. Start fresh with an injected structured summary when the prior tool results have gone stale.

## Task statements most likely to be tested here

[3.1](../tasks/3-1.md) · [3.2](../tasks/3-2.md) · [3.3](../tasks/3-3.md) · [3.4](../tasks/3-4.md) · [3.5](../tasks/3-5.md) · [1.7](../tasks/1-7.md) · [5.4](../tasks/5-4.md)

## How to prepare for it

Configure a real repository. Project CLAUDE.md, a `.claude/rules/` file with `paths:`, a project skill with `context: fork` and `allowed-tools`, a project slash command. Then run one single-file fix and one multi-file migration through both plan mode and direct execution, and notice exactly where planning paid for itself.
