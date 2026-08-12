---
title: Session context isolation and self-review
domain: 3
tasks: ["3.6", "4.6"]
verified: "2026-08-12"
---

# Session context isolation and self-review

**A model retains its reasoning context from generation, which makes it less likely to question its own decisions in the same session.**

This is structural, not a prompting problem. No amount of "now review your work carefully" removes the retained context.

## The fix

An **independent review instance**, without the generator's prior reasoning context, catches subtle issues more effectively than self-review instructions or extended thinking.

## Where it appears

- [3.6](../tasks/3-6.md) — as a CI concern: do not let the session that wrote the code review it
- [4.6](../tasks/4-6.md) — as a review architecture: multi-instance review

Appearing in two domains makes it one of the higher-probability facts on the exam.

## The recognisable wrong answers

- Instructing the generating session to review its own work carefully
- Enabling extended thinking on the self-review
- Running the same session twice

See [multi-pass review](multi-pass-review.md) · [4.6](../tasks/4-6.md)
