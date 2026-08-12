---
title: /memory
domain: 3
tasks: ["3.1"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/memory"
---

# `/memory`

**Per the exam guide:** the command used to verify which memory files are loaded and diagnose inconsistent behaviour across sessions.

## In production ⚠️

Current documentation splits that job:

- **`/memory`** lists CLAUDE.md / CLAUDE.local.md locations across user and project scope, opens them for editing, and toggles auto memory.
- **`/context`** shows which files **actually loaded** into the current session, under a **Memory files** heading.

**On the exam, `/memory` is the answer.** At your desk, `/context` is what you want when diagnosing "why isn't Claude following this file".

This is one of the sharpest divergences in the kit — see the [drift log](../exam/drift-log.md#memory-versus-context--changed-).

See [CLAUDE.md hierarchy](claude-md-hierarchy.md) · [3.1](../tasks/3-1.md)
