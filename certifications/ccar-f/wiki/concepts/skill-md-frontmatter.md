---
title: SKILL.md frontmatter
domain: 3
tasks: ["3.2"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/skills"
---

# SKILL.md frontmatter

Skills live in `.claude/skills/` as `SKILL.md` files. Three frontmatter options are tested.

| Field | Per the guide |
|---|---|
| **`context: fork`** | Run the skill in an isolated sub-agent context, so its output does not pollute the main conversation |
| **`allowed-tools`** | Restrict tool access during skill execution |
| **`argument-hint`** | Prompt the developer for required parameters when the skill is invoked without arguments |

## `context: fork`

Use it for skills producing **verbose output** (codebase analysis) or **exploratory context** (brainstorming alternatives). Same underlying idea as the [Explore subagent](explore-subagent.md): keep noise out of the main thread.

## Personal variants

Create customised skills in `~/.claude/skills/` **under a different name**, so you do not affect teammates who depend on the shared one.

## Skills versus CLAUDE.md

The question is **when the content is needed**, not how important it is:

- **Skill** — on-demand, task-specific workflow
- **CLAUDE.md** — always loaded, universal standards

## `allowed-tools` semantics ⚠️

Current docs define it as a **pre-approval** — *"tools Claude can use without asking permission"* — not a restriction. **Answer the guide's framing on the exam.** For real enforcement use `permissions.deny` or a `PreToolUse` hook. See the [drift log](../exam/drift-log.md#skillmd-frontmatter--confirmed-fields-inverted-semantics-).

See [slash commands](slash-commands.md) · [3.2](../tasks/3-2.md)
