---
title: Explicit criteria
domain: 4
tasks: ["4.1"]
verified: "2026-08-12"
---

# Explicit criteria

**Specification beats exhortation.** The whole of [4.1](../tasks/4-1.md) is an argument against telling the model to try harder.

## The contrast

| Vague | Explicit |
|---|---|
| "Check that comments are accurate" | "Flag comments only when claimed behavior contradicts actual code behavior" |
| "Be conservative" | "Report bugs and security issues; skip minor style and local patterns" |
| "Only report high-confidence findings" | Categorical criteria defining what counts |

The first column asks the model to apply a standard you did not define. The second column defines it.

## Named failures

**"Be conservative"** and **"only report high-confidence findings"** are called out in the guide as *not* improving precision. They give the model nothing to apply — and the second compounds the [confidence problem](unreliable-proxies.md).

## Severity criteria

Define explicit severity levels **with concrete code examples for each**. Levels defined by adjective alone — "high", "medium", "low" — drift between runs.

See [false positive rates](false-positive-rates.md) · [few-shot prompting](few-shot-prompting.md) · [4.1](../tasks/4-1.md)
