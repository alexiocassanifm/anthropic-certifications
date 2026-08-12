---
title: CLAUDE.md hierarchy and @import
domain: 3
tasks: ["3.1"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/memory"
---

# CLAUDE.md hierarchy and `@import`

## The three tiers the exam tests

| Level | Location | Reaches |
|---|---|---|
| **User** | `~/.claude/CLAUDE.md` | Only you, across all your projects |
| **Project** | `.claude/CLAUDE.md` or root `CLAUDE.md` | Everyone who clones, via version control |
| **Directory** | subdirectory `CLAUDE.md` | That directory's scope |

**User-level settings are not shared through version control.** This one fact answers a whole family of items — *"a new team member isn't receiving the instructions"* means they are at user level.

## `@import`

`@path/to/import` references external files, keeping CLAUDE.md modular — e.g. importing the specific standards files relevant to each package rather than inlining everything.

## In production

Two further tiers exist: **managed policy** (organisation-wide, `/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS) and **`CLAUDE.local.md`** (personal, project-specific, gitignored). Imports resolve relative to the importing file and nest up to **four hops**. See the [drift log](../exam/drift-log.md#claudemd-hierarchy--confirmed-extended).

See [.claude/rules](claude-rules-directory.md) · [/memory](memory-command.md) · [3.1](../tasks/3-1.md)
