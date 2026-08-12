---
title: Message Batches API
domain: 4
tasks: ["4.5"]
verified: "2026-08-12"
---

# Message Batches API

| Property | Value |
|---|---|
| Cost | **50% saving** |
| Processing window | **Up to 24 hours** |
| Latency SLA | **None guaranteed** |
| Multi-turn tool calling in one request | **Not supported** |
| Correlation | `custom_id` on request/response pairs |

## The decision

| Workload | API |
|---|---|
| Blocking pre-merge check (a developer is waiting) | **Synchronous** |
| Overnight report, weekly audit, nightly test generation | **Batch** |

**No multi-turn tool calling** means an agentic loop cannot run inside a single batch request — it cannot execute tools mid-request and return results.

## Failure handling

Resubmit **only the failed documents**, identified by `custom_id`, with appropriate modifications — e.g. chunking documents that exceeded context limits. Refine prompts on a sample set before batching large volumes.

## SLA arithmetic

If processing takes up to 24 hours and you must guarantee 30, submit every 4 hours. Do the subtraction rather than eyeballing it.

## The named wrong answers

- Moving a **blocking** workflow to batch for the cost saving
- "Batch usually completes faster than the maximum" — design against the **guarantee**, not the average
- "Results come back out of order so we can't use it" — a misconception; `custom_id` correlates them

See [4.5](../tasks/4-5.md)
