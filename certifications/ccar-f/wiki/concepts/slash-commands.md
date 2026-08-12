---
title: Custom slash commands
domain: 3
tasks: ["3.2"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/skills"
---

# Custom slash commands

| Location | Scope |
|---|---|
| `.claude/commands/` | **Project** — shared via version control |
| `~/.claude/commands/` | **User** — personal |

## The exam item

*"You want a custom `/review` command available to every developer when they clone the repository. Where does the file go?"* → **`.claude/commands/` in the project repository.**

Know why the distractors fail:

| Distractor | Why |
|---|---|
| `~/.claude/commands/` | Personal, not shared through version control |
| The `CLAUDE.md` file | Project instructions and context, not command definitions |
| A `.claude/config.json` with a commands array | Describes a configuration mechanism that does not exist |

That last one is worth noting as a pattern: **this exam uses non-existent features as distractors**, especially in Domain 3.

## In production

Custom commands have **merged into skills** — `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both produce `/deploy`. Existing files keep working, and the scoping facts above are unchanged. See the [drift log](../exam/drift-log.md#slash-commands-and-skills-have-merged--changed).

See [SKILL.md frontmatter](skill-md-frontmatter.md) · [3.2](../tasks/3-2.md)
