---
title: Format and Scoring
---

# Format and Scoring

## Item types

Two formats appear:

- **Multiple-choice** — one correct response.
- **Multiple-response** — more than one correct response.

Every item states how many responses to select. Read that line. On a multiple-response item there is no partial credit implied by the format itself, and selecting the wrong number is an automatic loss.

This kit models both: every practice item carries a `select_count`, and the answer key is an array even when its length is 1. See [`questions/schema.md`](../../questions/schema.md).

## Scenario framing

The exam presents **4 scenarios drawn from a bank of 6**. Each scenario is a paragraph of production context — a customer support agent, a research pipeline, a CI integration — and a group of items hangs off it.

Practical consequences:

- **Read the scenario once, carefully, then keep it in mind for the whole cluster.** The details (the 80% first-contact-resolution target, the tool names, the fact that subagents are already working correctly) are load-bearing in the items that follow.
- Two scenarios you prepared for will not appear. Do not over-index on any one of them.
- The scenario tells you the *constraints*. Most items are decided by matching a fix to a constraint that is already stated in the scenario or the stem.

The six scenarios are documented in [`../scenarios/`](../scenarios/).

## Timing

120 minutes, 60 items — **two minutes each**.

That is not generous. Scenario stems run several lines and options are full sentences describing architectural changes. A workable pace:

- ~30 seconds reading the stem and identifying *what problem is actually stated*
- ~45 seconds on the options
- ~30 seconds confirming the choice against the stated root cause
- flag and move on if you are past three minutes

Items are not weighted by difficulty in your favour: a hard item and an easy one are worth the same. Never burn five minutes on one.

## How scoring works

The exam is **criterion-referenced**. You are measured against a fixed performance standard, not against other candidates. There is no curve and no quota — everyone who meets the standard passes.

The passing score is a **scaled 720 on a 100–1,000 range**, established through a formal standard-setting study in which trained subject matter experts judged the performance expected of a minimally qualified candidate. Scaled scoring exists so that scores are comparable across exam forms of slightly different difficulty.

Your score report gives:

- pass or fail
- a scaled score, 100–1,000
- **percent-correct within each content domain**

The domain percentages are diagnostic only. They do not determine pass/fail — that comes from the total scaled score.

### Why 720 is not "72%"

A scaled score is not a percentage. The 100–1,000 range and the 720 cut are the output of an equating model applied to raw scores; the raw percentage that maps to 720 varies by form. **Do not assume you need 72% correct.** You cannot compute your scaled score from a practice result, and neither can this kit.

### What this kit reports instead

`/mock-exam` and `/progress` report:

- **percent-correct overall**
- **percent-correct by domain** — the same diagnostic the real score report gives you
- per-task-statement hit rate, so you know exactly what to study
- a plain readiness indication, in words

They deliberately **do not** emit a scaled score. A number like "your scaled score is 743" would be fabricated: reproducing the scale would require the standard-setting study and the form-level equating data, neither of which is public. A made-up scaled score is worse than no score, because it invites you to stop studying at the wrong moment.

Use the domain percentages the way the real report intends: as a map of where to spend your remaining time.

## Retakes

If you do not pass, waiting periods increase with each attempt: **14 days** after the first failure, **30 days** after the second, **90 days** after the third. You may take a given exam up to **four times in a rolling twelve-month period**, and the fee applies to each attempt.

Limits are per exam, so failing CCAR-F does not block you from registering for a different certification.

## Recertification

The credential is valid for **12 months**. Because the underlying technology moves quickly, it is deliberately time-limited.

To renew on time you review what has changed since you certified and complete a **free, non-proctored assessment** on the Anthropic Partner Academy. If you let the credential lapse, you retake the full exam at full price. If exam content has changed significantly, Anthropic may require the full exam rather than the renewal assessment.

The practical advice: put a reminder at month 10.

## See also

- [blueprint.md](blueprint.md) — domains, weights, task statements
- [logistics.md](logistics.md) — registration, exam-day rules, policies
- [out-of-scope.md](out-of-scope.md) — what will not be tested
