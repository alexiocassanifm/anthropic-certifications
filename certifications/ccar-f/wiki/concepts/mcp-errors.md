---
title: MCP structured errors
domain: 2
tasks: ["2.2"]
verified: "2026-08-12"
---

# MCP structured errors

An error is an **input to a decision**, not a log line. The `isError` flag communicates failure; the metadata alongside it determines what the agent does next.

## The four categories

| Category | Example | Agent should |
|---|---|---|
| **Transient** | Timeout, service unavailable | Retry |
| **Validation** | Invalid input | Fix input, retry |
| **Business** | Policy violation | Explain to the user — do **not** retry |
| **Permission** | Insufficient access | Escalate or explain — do **not** retry |

## The metadata that makes recovery possible

- `errorCategory` — transient / validation / business / permission
- `isRetryable` — boolean
- A human-readable description

For business rule violations, `retryable: false` **plus a customer-friendly explanation**, so the agent communicates rather than retries.

## Local recovery first

Subagents handle transient failures themselves and propagate to the coordinator only what they cannot resolve — along with **partial results and what was attempted**.

## The anti-pattern

Generic `"Operation failed"`. Every failure looks alike, so the agent responds alike — usually retrying, sometimes forever.

See [access failure vs empty result](access-failure-vs-empty-result.md) · [structured error context](structured-error-context.md) · [2.2](../tasks/2-2.md)
