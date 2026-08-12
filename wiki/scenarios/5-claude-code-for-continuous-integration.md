---
title: "Scenario 5: Claude Code for Continuous Integration"
scenario: 5
primary_domains: [3, 4]
---

# Scenario 5: Claude Code for Continuous Integration

**Primary domains:** [3 — Claude Code Configuration & Workflows](../domains/3-claude-code-configuration-and-workflows.md) · [4 — Prompt Engineering & Structured Output](../domains/4-prompt-engineering-and-structured-output.md)

## The situation

Claude Code integrated into a CI/CD pipeline. The system runs automated code reviews, generates test cases, and posts feedback on pull requests. The stated goals: **actionable feedback** and **minimised false positives**.

## What makes this scenario generative

Only two primary domains, and they interlock tightly: CI is where a configuration problem and a prompting problem look identical from the outside. A review that posts noise might be failing because the prompt has no explicit criteria (Domain 4) or because CLAUDE.md never told it what the project's testing standards are (Domain 3).

Three details do the work:

1. **"Minimise false positives"** — precision is a stated requirement, so any item can measure against it. This is [4.1](../tasks/4-1.md)'s home ground.
2. **Automated, non-interactive** — nobody is at a terminal. Everything about headless operation and machine-parseable output lives here.
3. **Pull requests** — a repeated, incremental workflow. The same review runs again after every push, which creates the duplicate-comment and stale-findings problems.

## Failure modes to expect

| Symptom | Where it points |
|---|---|
| The CI job hangs forever waiting for input | `-p` / `--print` for non-interactive mode — [3.6](../tasks/3-6.md) |
| Findings arrive as prose nobody can post as inline comments | `--output-format json` with `--json-schema` — [3.6](../tasks/3-6.md) |
| The review re-posts the same twelve comments on every push | Include prior findings in context; instruct it to report only new or still-unaddressed issues — [3.6](../tasks/3-6.md) |
| Test generation proposes scenarios the suite already covers | Provide the existing test files in context — [3.6](../tasks/3-6.md) |
| Generated tests are low-value and ignore project fixtures | Document testing standards, valuable test criteria, and available fixtures in CLAUDE.md — [3.6](../tasks/3-6.md) |
| The session that wrote the code reviews it and finds nothing | Use an independent review instance without the generator's reasoning context — [3.6](../tasks/3-6.md), [4.6](../tasks/4-6.md) |
| One category floods PRs with false positives; developers stop reading | Temporarily disable that category to restore trust while you fix its prompt — [4.1](../tasks/4-1.md) |
| "Be conservative" / "only high-confidence findings" changes nothing | Replace with explicit categorical criteria: which issues to report, which to skip — [4.1](../tasks/4-1.md) |
| Severity labels are applied inconsistently across runs | Define explicit severity criteria with concrete code examples per level — [4.1](../tasks/4-1.md) |
| Output format varies run to run despite detailed instructions | Few-shot examples showing location, issue, severity, suggested fix — [4.2](../tasks/4-2.md) |
| The model flags acceptable local patterns as problems | Few-shot examples distinguishing acceptable patterns from genuine issues — [4.2](../tasks/4-2.md) |
| A 14-file PR gets detailed feedback on some files, superficial on others, and contradicts itself | Split into per-file passes plus a cross-file integration pass — [4.6](../tasks/4-6.md) |
| Nobody can tell which code constructs trigger the most dismissals | Add a `detected_pattern` field to structured findings — [4.4](../tasks/4-4.md) |
| A blocking pre-merge check is moved to the Batches API | Wrong: no latency SLA, up to 24h. Batch is for the overnight report only — [4.5](../tasks/4-5.md) |

## The three traps this scenario sets

**1. Vague instructions instead of categorical criteria.** *"Be conservative"* and *"only report high-confidence findings"* are the guide's named examples of what does **not** work. The fix is always specific: define which categories to report (bugs, security) and which to skip (minor style, local patterns). See [4.1](../tasks/4-1.md).

**2. Shifting the burden to developers.** *"Require smaller PRs"* is a recurring wrong answer. It does not improve the system; it makes humans work around it. See [4.6](../tasks/4-6.md) and the `shifts-burden` family in [`question-style-guide.md`](../../questions/question-style-guide.md).

**3. Consensus voting.** *"Run three passes and flag only issues appearing in at least two"* sounds rigorous and is wrong: it suppresses real bugs that are only caught intermittently. See [4.6](../tasks/4-6.md).

## The self-review fact

A model retains its reasoning context from generation, which makes it less likely to question its own decisions in the same session. **An independent review instance catches more than any amount of "now review your own work carefully" instruction, or extended thinking.** This appears in both [3.6](../tasks/3-6.md) and [4.6](../tasks/4-6.md), which makes it one of the highest-probability facts in the whole scenario.

## Batch versus synchronous, decided

| Workflow | API | Why |
|---|---|---|
| Blocking pre-merge check | Synchronous | A developer is waiting; batch has no latency SLA |
| Overnight technical-debt report | Batch | Latency-tolerant, 50% cheaper |
| Nightly test generation | Batch | Same |
| Weekly audit | Batch | Same |

When an item proposes moving *both* workflows to batch for the cost saving, the answer splits them. See [4.5](../tasks/4-5.md).

## Task statements most likely to be tested here

[3.6](../tasks/3-6.md) · [4.1](../tasks/4-1.md) · [4.2](../tasks/4-2.md) · [4.5](../tasks/4-5.md) · [4.6](../tasks/4-6.md) · [3.1](../tasks/3-1.md) · [4.4](../tasks/4-4.md)

## How to prepare for it

Run `claude -p` in a script and watch it not hang. Add `--output-format json` with `--json-schema` and post the result as PR comments. Then deliberately write a review prompt with one high-false-positive category, watch developers stop trusting the whole thing, and practise the fix: disable that category, rewrite its criteria with concrete examples, re-enable.
