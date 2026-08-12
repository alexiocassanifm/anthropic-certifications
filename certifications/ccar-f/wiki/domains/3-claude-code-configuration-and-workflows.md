---
title: "Domain 3: Claude Code Configuration & Workflows"
domain: 3
weight: 20
items_at_60: 12
task_statements: 6
---

# Domain 3: Claude Code Configuration & Workflows

**20% of the exam — 12 items at 60.**

## What this domain is about

Configuring Claude Code for a team, and knowing which workflow to reach for. Where instructions live and who receives them; how commands and skills are scoped and restricted; how conventions load conditionally by file path; when planning earns its cost; how to iterate toward a correct result; and how to run Claude Code non-interactively in CI.

This is the **most verifiable** domain on the exam. Every fact in it can be confirmed on your own machine in an afternoon. If you are short on time, this is where study converts to marks most reliably.

## Task statements

| ID | Title | Core idea |
|---|---|---|
| [3.1](../tasks/3-1.md) | Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization | User vs project vs directory; `@import`; `.claude/rules/` |
| [3.2](../tasks/3-2.md) | Create and configure custom slash commands and skills | Project vs user scope; `context: fork`, `allowed-tools`, `argument-hint` |
| [3.3](../tasks/3-3.md) | Apply path-specific rules for conditional convention loading | YAML `paths:` globs beat directory-bound CLAUDE.md for scattered files |
| [3.4](../tasks/3-4.md) | Determine when to use plan mode vs direct execution | Complexity and multiple valid approaches, versus a well-scoped change |
| [3.5](../tasks/3-5.md) | Apply iterative refinement techniques for progressive improvement | Concrete input/output examples; test-driven iteration; the interview pattern |
| [3.6](../tasks/3-6.md) | Integrate Claude Code into CI/CD pipelines | `-p`, `--output-format json`, `--json-schema`, CLAUDE.md as CI context |

## The through-lines

**Scope determines who receives an instruction.** `~/.claude/CLAUDE.md` is yours alone and is not shared through version control. `.claude/CLAUDE.md` or a root `CLAUDE.md` is the project's, and reaches every teammate who clones. Subdirectory `CLAUDE.md` files apply to their directory. Nearly every configuration item on this exam is a scope question wearing a costume: *"a new team member is not getting the instruction"* means it was written at user level. See [3.1](../tasks/3-1.md).

**Directory-bound versus path-pattern.** A subdirectory `CLAUDE.md` covers a directory. A `.claude/rules/` file with a YAML `paths:` glob covers a *pattern* — `**/*.test.tsx` catches every test file wherever it lives. When conventions must follow file **type** across a codebase rather than file **location**, glob-scoped rules are the answer and directory CLAUDE.md files cannot do it cleanly. See [3.3](../tasks/3-3.md).

**Skills versus CLAUDE.md.** CLAUDE.md is always loaded and holds universal standards. A skill is invoked on demand for a task-specific workflow. Choosing between them is a question about *when the content is needed*, not about how important it is. See [3.2](../tasks/3-2.md).

**Isolation is a configuration option.** `context: fork` runs a skill in a separate sub-agent context so verbose or exploratory output never pollutes the main conversation. `allowed-tools` restricts what a skill can do while it runs. The Explore subagent does the same job for discovery phases. All three are the same idea: keep noise and risk out of the main thread. See [3.2](../tasks/3-2.md), [3.4](../tasks/3-4.md), [least-privilege tooling](../heuristics/least-privilege-tooling.md).

**Plan mode is for uncertainty, not for size alone.** It earns its cost when there are architectural implications, multiple valid approaches, or large multi-file change — a monolith-to-microservices split, a migration touching 45 files. It does not earn it for a single-file bug fix with a clear stack trace. And "start direct, switch to plan if it gets complicated" is wrong when the complexity is already stated in the requirements. See [3.4](../tasks/3-4.md).

**In CI, `-p` or nothing.** The `-p` (`--print`) flag runs Claude Code non-interactively; without it the job waits for input and hangs. `--output-format json` with `--json-schema` produces machine-parseable findings you can post as inline PR comments. And CLAUDE.md is how you give a CI-invoked Claude the project context — testing standards, fixture conventions, review criteria — that an interactive user would have supplied by conversation. See [3.6](../tasks/3-6.md).

**A generator is a poor reviewer of its own work.** The same session that wrote the code retains its reasoning context and is less likely to question its own decisions. An independent instance catches more. This fact sits in Domain 3 as a CI concern and in [4.6](../tasks/4-6.md) as an architecture concern. See [3.6](../tasks/3-6.md).

## Where the failures live

- An instruction that works for one developer and nobody else
- A monolithic CLAUDE.md so large that the relevant section is diluted
- Test conventions that apply in `src/components/` but not in the twelve other places tests live
- A CI job hanging forever, waiting for interactive input
- A review re-posting the same twelve comments on every push because prior findings were not supplied as context
- Test generation proposing scenarios the suite already covers, because the existing test files were never shown
- Direct execution on a migration that turns out to need architectural decisions, discovered at file 30 of 45

## Preparation

Configure a real project end to end: project CLAUDE.md, a `.claude/rules/` file with a `paths:` glob, a project skill using `context: fork` and `allowed-tools`, an MCP server in `.mcp.json` with env expansion, and a personal one in `~/.claude.json`. Then run the same task in plan mode and in direct execution, on a single-file fix and on a multi-file migration, and observe where planning paid.

Use `/memory` to confirm which memory files actually loaded when behaviour surprises you — that command is both a real debugging tool and a testable fact.

## Related

- Scenarios: [2](../scenarios/2-code-generation-with-claude-code.md), [4](../scenarios/4-developer-productivity-with-claude.md), [5](../scenarios/5-claude-code-for-continuous-integration.md)
- [Domain 4](4-prompt-engineering-and-structured-output.md) — CI review quality is a prompting problem as much as a configuration one
