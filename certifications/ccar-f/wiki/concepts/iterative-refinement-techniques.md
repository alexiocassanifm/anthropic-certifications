---
title: Iterative refinement techniques
domain: 3
tasks: ["3.5"]
verified: "2026-08-12"
---

# Iterative refinement techniques

Four named techniques for converging on a correct result.

## Concrete input/output examples

**The most effective way to communicate expected transformations** when prose descriptions get interpreted inconsistently. Two or three examples beat another paragraph — prose is where the inconsistency came from.

## Test-driven iteration

Write the test suite first — expected behaviour, edge cases, performance requirements — then iterate by **sharing test failures**. Failures are precise feedback in a form the model can act on.

## The interview pattern

Have Claude ask **you** questions to surface considerations you had not anticipated, before implementing. Valuable in unfamiliar domains — cache invalidation strategies, failure modes.

## Batched vs sequential fixes

| Problems are… | Approach |
|---|---|
| **Interacting** — fixing one affects another | All issues in **one** detailed message |
| **Independent** | Fix sequentially |

Fixing interacting problems one at a time makes each fix perturb the others, and you oscillate.

See [few-shot prompting](few-shot-prompting.md) · [3.5](../tasks/3-5.md)
