---
title: Progressive summarization and the case-facts block
domain: 5
tasks: ["5.1"]
verified: "2026-08-12"
---

# Progressive summarization and the case-facts block

**Summarisation is lossy in a specific direction: it eats precision.**

Numerical values, percentages, dates, order numbers, and customer-stated expectations condense into vague prose — exactly the facts that matter most. "The discussed refund amount" is what "$247.50" becomes after three summaries.

## The fix is structural, not stylistic

**Extract transactional facts into a persistent "case facts" block, included in every prompt, outside the summarised history.**

The block is never summarised, so the numbers never decay. For multi-issue sessions, persist structured issue data — order IDs, amounts, statuses — into a separate context layer.

## Why "write a better summarisation prompt" is wrong

Summarisation is lossy **by nature**. Asking it to preserve everything defeats its purpose. The answer is to put the facts somewhere summarisation does not reach — a `prompt-instead-of-enforcement` shape applied to context.

See [lost in the middle](lost-in-the-middle.md) · [tool output trimming](tool-output-trimming.md) · [5.1](../tasks/5-1.md)
