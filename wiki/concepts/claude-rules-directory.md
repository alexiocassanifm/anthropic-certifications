---
title: .claude/rules/ and path-scoped conventions
domain: 3
tasks: ["3.1", "3.3"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/memory"
---

# `.claude/rules/` and path-scoped conventions

Topic-specific rule files as an alternative to one monolithic CLAUDE.md — and, more importantly, the mechanism for **conditional** loading.

## Path scoping

YAML frontmatter with a `paths` field containing glob patterns. The rule activates **only when Claude works with matching files**, reducing irrelevant context and token usage.

```markdown
---
paths:
  - "src/api/**/*.ts"
---
```

## The decision it settles

| Conventions follow… | Use |
|---|---|
| File **location** | Subdirectory `CLAUDE.md` |
| File **type**, across directories | `.claude/rules/` with globs |

Test files sitting beside the code they test (`Button.test.tsx` next to `Button.tsx`) are the canonical case: a directory-bound file cannot cover them cleanly; `**/*.test.tsx` can.

**The trigger phrase is "spread throughout" or "regardless of location".**

## Why the distractors fail

- Consolidating in root CLAUDE.md relies on **inference**, not explicit path matching
- Skills require **invocation** or a relevance judgment — not automatic application by path
- Per-subdirectory CLAUDE.md files cannot handle files spread across many directories

See [CLAUDE.md hierarchy](claude-md-hierarchy.md) · [3.3](../tasks/3-3.md)
