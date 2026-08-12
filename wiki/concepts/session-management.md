---
title: Session resumption and forking
domain: 1
tasks: ["1.7"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/agent-sdk/sessions"
---

# Session resumption and forking

## The mechanisms

- **`--resume <session-name>`** — continue a specific prior conversation
- **`fork_session`** — create an independent branch from a shared baseline, so expensive context-building happens once and divergent approaches explore from it without contaminating each other

## The judgment call

Resuming after code changes is dangerous: the session's tool results describe files as they *were*. The agent will reason confidently about a codebase that no longer exists.

| Situation | Do this |
|---|---|
| Prior context mostly still valid | Resume, and **tell it which files changed** for targeted re-analysis |
| Prior tool results are stale | **Start fresh with a structured summary** — the guide states this is *more reliable* than resuming |
| Comparing two approaches from one analysis | Fork |

The "start fresh beats resuming" point is counterintuitive — resumption feels thorough — which is exactly why it is testable.

## In production

The Agent SDK's `resume` takes a session **ID**; `fork_session` (Python) / `forkSession` (TypeScript) branches it. `--continue` resumes the most recent session with no ID. See the [drift log](../exam/drift-log.md#session-resumption--changed-nuance).

See [context degradation](context-degradation.md) · [1.7](../tasks/1-7.md)
