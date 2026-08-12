---
title: Tool output trimming
domain: 5
tasks: ["5.1"]
verified: "2026-08-12"
---

# Tool output trimming

**Tool results consume context disproportionately to their relevance.**

The guide's example: an order lookup returning **40+ fields when only 5 are relevant**. Those 35 irrelevant fields are then carried in every subsequent request, forever.

## The fix

Trim tool outputs to the relevant fields **before they accumulate in context**. Not after — accumulation is the problem.

## The multi-agent version

When downstream agents have limited context budgets, modify **upstream** agents to return structured data — key facts, citations, relevance scores — instead of verbose content and reasoning chains. The trimming happens at the source.

See [progressive summarization](progressive-summarization.md) · [context degradation](context-degradation.md) · [5.1](../tasks/5-1.md)
