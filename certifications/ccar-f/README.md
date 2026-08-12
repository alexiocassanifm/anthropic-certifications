# Claude Certified Architect – Foundations (CCAR-F)

One certification kit inside [anthropic-certifications](../../README.md).

An open-source, local-first study toolkit for the **Claude Certified Architect – Foundations** exam (exam code `CCAR-F`).

It gives you two things:

1. **A wiki** — a linked knowledge base covering all 5 domains, all 30 task statements, the 6 exam scenarios, and ~40 atomic concept notes. Plain Markdown, readable on GitHub and in Obsidian.
2. **A study agent** — a set of Claude Code skills that teach from the wiki, quiz you, run a blueprint-weighted 60-item mock exam, and track which task statements are still weak.

> **Unofficial.** This project is not affiliated with, endorsed by, or sponsored by Anthropic. It contains **no exam content**. See [DISCLAIMER.md](../../DISCLAIMER.md).

---

## What the exam looks like

| | |
|---|---|
| Credential | Claude Certified Architect – Foundations |
| Exam code | `CCAR-F` |
| Items | 60 (multiple-choice **and** multiple-response) |
| Structure | 4 scenarios drawn from a bank of 6 |
| Time | 120 minutes |
| Passing score | Scaled 720 on a 100–1,000 range |
| Validity | 12 months |

Content domains and weights:

| # | Domain | Weight | Items at 60 |
|---|---|---|---|
| 1 | [Agentic Architecture & Orchestration](wiki/domains/1-agentic-architecture-and-orchestration.md) | 27% | 16 |
| 2 | [Tool Design & MCP Integration](wiki/domains/2-tool-design-and-mcp-integration.md) | 18% | 11 |
| 3 | [Claude Code Configuration & Workflows](wiki/domains/3-claude-code-configuration-and-workflows.md) | 20% | 12 |
| 4 | [Prompt Engineering & Structured Output](wiki/domains/4-prompt-engineering-and-structured-output.md) | 20% | 12 |
| 5 | [Context Management & Reliability](wiki/domains/5-context-management-and-reliability.md) | 15% | 9 |

Full breakdown: [wiki/exam/blueprint.md](wiki/exam/blueprint.md).

---

## Quick start

```bash
git clone https://github.com/alexiocassanifm/anthropic-certifications.git
cd anthropic-certifications
pip install -r requirements.txt      # PyYAML, for the validator and exam builder
claude                                # open Claude Code at the repo ROOT
```

Then, inside Claude Code:

```
/study 1.4          # learn one task statement
/quiz --domain 2    # short targeted quiz
/mock-exam          # full 60-item timed simulation
/progress           # readiness dashboard
/drill              # spaced repetition on your weak areas
/refresh-kb         # re-verify the wiki against current official docs
```

Or install it as a plugin, from any project:

```
/plugin install alexiocassanifm/anthropic-certifications
```

### Reading the wiki without Claude

Everything under [`wiki/`](wiki/README.md) is plain Markdown with relative links. Browse it on GitHub, or point Obsidian at the repo folder — both resolve the same links.

---

## How to study with this

The kit assumes you already build with Claude; it is not an introduction to the SDK. A workable loop:

1. Read [wiki/exam/blueprint.md](wiki/exam/blueprint.md) and [wiki/exam/out-of-scope.md](wiki/exam/out-of-scope.md) so you know the boundary of what is tested.
2. Read the three [heuristics](wiki/heuristics/) notes first. They generalise across domains and predict more answers than any single fact.
3. Work through [wiki/tasks/](wiki/tasks/) domain by domain, heaviest weight first (Domain 1).
4. Run `/quiz` after each domain, `/mock-exam` when you have covered everything.
5. Let `/drill` schedule the review.
6. Run `/refresh-kb` once before exam day, and read the [drift log](wiki/exam/drift-log.md).

## Verified, not assumed

The exam is written against **Exam Guide v1.0 (July 2026)**. The tooling it
describes — Claude Code, the Agent SDK, MCP, the Claude API — moves faster than the
guide does.

So every technical claim in this wiki was checked against official documentation,
and each note records a `verified` date and its sources. Where current docs differ
from the guide, the difference is **recorded in [`wiki/exam/drift-log.md`](wiki/exam/drift-log.md), not
silently applied** — the guide is what the exam was written against, so it stays
authoritative for answering, while the drift log keeps you from being surprised
when your own machine behaves differently.

The log tags each finding CONFIRMED, EXTENDED, CHANGED, or INVERTED. Three worth
knowing before you sit the exam:

- **`allowed-tools` in SKILL.md frontmatter** — the guide frames it as *restricting*
  tool access; current docs define it as a *pre-approval*. Opposite in kind.
- **`/memory` vs `/context`** — the guide uses `/memory` to verify which memory
  files loaded; current docs assign that job to `/context`.
- **Structured output** — the guide teaches `tool_use` + JSON Schema; the API now
  also offers native structured outputs via `output_config.format`.

Re-run the check any time with `/refresh-kb`.

A suggested 3-week schedule is in [wiki/exam/preparation-plan.md](wiki/exam/preparation-plan.md).

---

## Repository layout

```
wiki/
  exam/         blueprint, scoring, out-of-scope, logistics, preparation plan
  heuristics/   cross-domain reasoning patterns the exam rewards
  domains/      one note per content domain
  scenarios/    the 6 exam scenarios and what each one tests
  tasks/        all 30 task statements — the core study unit
  concepts/     ~40 atomic notes (stop_reason, tool_choice, .claude/rules, ...)
questions/
  schema.md               item schema
  question-style-guide.md distractor taxonomy used to author items
  bank/                   ~90 original practice items, YAML, one file per domain
scripts/        validate_questions.py, build_exam.py
.claude/        skills and slash commands
progress/       your local progress state (gitignored)
```

---

## The official exam guide

This kit is written **against** the official exam guide but does not reproduce it. Download your own copy from the **Anthropic Partner Academy** certification page for CCAR-F. All content here is written against *Exam Guide v1.0, July 2026*.

If a newer guide version changes the blueprint, open an issue — the version is recorded in [wiki/exam/blueprint.md](wiki/exam/blueprint.md).

---

## Contributing

Practice items, corrections, and new concept notes are welcome. The one hard rule: **never contribute real exam content.** See [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Licence

Code is MIT. Wiki and question content are CC BY-SA 4.0. See [LICENSE](../../LICENSE).
