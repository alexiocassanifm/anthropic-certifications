---
name: refresh-kb
description: Re-verify the CCAR-F wiki against current official documentation, report where the tooling has drifted from the exam guide, and update the drift log. Use before exam day or when tooling has changed.
argument-hint: [--domain N | <task-statement> | --all]
---

# Refresh the knowledge base

The exam is written against **Exam Guide v1.0 (July 2026)**. Claude Code, the
Agent SDK, MCP, and the Claude API all move faster than the guide. This skill
re-checks the wiki's technical claims against live documentation and records
divergence.

## The governing principle

**The guide stays authoritative for the exam. Current docs are recorded as drift.**

Never silently rewrite a note to match current documentation. An item writer built
the exam against the guide, so a note "corrected" to match today's docs can turn a
right answer into a wrong one. Divergence goes in `wiki/exam/drift-log.md`, and the
note gets an "In production, beyond the guide" section pointing at it.

## Scope

| Argument | Verify |
|---|---|
| `<task-statement>` e.g. `2.4` | That note and its linked concepts |
| `--domain N` | All task statements in that domain |
| `--all` (default) | Everything with a `verified` frontmatter field |

If the user gives no argument, propose `--domain 3` and explain why: every CHANGED
and INVERTED entry in the current drift log is in Domain 3 or 4, because those are
the domains anchored to named commands, flags, and frontmatter fields. Domains 1,
2, and 5 test architectural judgment and age well.

## Verify

For each note in scope:

1. Read its frontmatter — `verified` date and any `sources`.
2. Identify the **checkable claims**: exact file paths, flag names, frontmatter
   field names, configuration keys, API parameter values, numeric limits. Prose
   about judgment and architecture is not checkable and is not in scope.
3. Fetch the authoritative source. Use these first:

   | Area | Source |
   |---|---|
   | CLAUDE.md, rules, memory | `code.claude.com/docs/en/memory` |
   | Skills, slash commands | `code.claude.com/docs/en/skills` |
   | CLI flags | `code.claude.com/docs/en/cli-reference` |
   | MCP | `code.claude.com/docs/en/mcp` |
   | Agent SDK sessions | `code.claude.com/docs/en/agent-sdk/sessions` |
   | Subagents | `code.claude.com/docs/en/sub-agents` |
   | Claude API | invoke the `claude-api` skill, or `platform.claude.com/docs` |

   For API questions the `claude-api` skill is faster and more reliable than
   fetching docs pages — use it.

4. Compare claim by claim and classify:

   | Tag | Meaning |
   |---|---|
   | **CONFIRMED** | Docs match the guide |
   | **EXTENDED** | Guide still correct; the feature has grown |
   | **CHANGED** | Behaviour or terminology differs |
   | **INVERTED** | Docs describe the mechanism differently *in kind* — highest risk |

## Report before writing

Present the findings first, grouped by tag, most severe first. For each
non-CONFIRMED finding give:

- The note and the specific claim
- What the guide says
- What current docs say, with the source URL
- Your classification and why
- Whether the **exam answer changes** — it usually does not

Then ask before editing. Do not touch files until the user has seen the findings.

## Update

On approval:

1. **`wiki/exam/drift-log.md`** — add or update the entry under the right domain
   heading, keeping the tag vocabulary and the existing structure. Update
   `last_verified` in the frontmatter.
2. **The note** — add or update its "In production, beyond the guide" section,
   linking to the drift log anchor. Leave the Knowledge and Skills sections alone
   unless the guide itself was misread, which is a correction rather than drift.
3. **Frontmatter** — set `verified` to today's date and record the `sources` URLs
   you actually fetched.
4. For an **INVERTED** finding, add a ⚠️ marker in both the note and the drift log,
   and state explicitly which framing to use on the exam.

## When a source cannot be reached

Say so; do not guess. Leave the note's `verified` date unchanged rather than
stamping it with an unverified pass — a stale date that is honest is more useful
than a fresh one that is not.

## Close

Summarise: notes checked, findings by tag, and whether any exam answer changed. If
nothing drifted, say that plainly — a clean pass is a real result, and it means the
material can be trusted as written.

Finally, remind the user that a new **exam guide version** would be a bigger event
than tooling drift: it could change the blueprint itself. The version in force is
recorded in `wiki/exam/blueprint.md`.
