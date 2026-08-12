---
title: Claude Code CLI flags for CI
domain: 3
tasks: ["3.6"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/cli-reference"
---

# Claude Code CLI flags for CI

| Flag | Effect |
|---|---|
| **`-p`** / `--print` | Non-interactive mode. **Without it, a CI job waits for input and hangs.** |
| **`--output-format json`** | Structured output instead of prose |
| **`--json-schema`** | Enforce a schema on that output — machine-parseable findings for inline PR comments |
| `--resume` | Continue a specific session |

## The exam item

*"Your pipeline runs `claude "Analyze this pull request"` but the job hangs indefinitely."* → add `-p`.

The distractors are **invented mechanisms**: a `CLAUDE_HEADLESS=true` environment variable, a `--batch` flag, redirecting stdin from `/dev/null`. None exist. This exam uses non-existent features as distractors more in Domain 3 than anywhere else — if a flag sounds unfamiliar, that is evidence.

## In production

`--output-format` also accepts `text` and `stream-json`; `--json-schema` is print-mode only. Note that `claude -p` runs load project-scoped `.mcp.json` servers **without** the interactive approval prompt.

See [session context isolation](session-context-isolation.md) · [3.6](../tasks/3-6.md)
