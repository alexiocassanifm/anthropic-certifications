---
title: Drift Log
last_verified: "2026-08-12"
guide_version: "1.0"
---

# Drift Log

The exam is written against **Exam Guide v1.0 (July 2026)**. The underlying tooling moves faster than the guide. This note records every place where **current documentation differs from what the guide describes**.

## How to use this note

**On the exam, answer according to the guide.** The blueprint is the contract, and items are written against the published objectives. This log exists so you are not blindsided when your own machine behaves differently from what you studied — and so you do not "correct" a right answer into a wrong one because you read a newer doc page last night.

Each entry is tagged:

| Tag | Meaning |
|---|---|
| **CONFIRMED** | Current docs match the guide. Nothing to worry about. |
| **EXTENDED** | The guide is still correct, but the feature has grown. Extra capability the exam will not test. |
| **CHANGED** | Current behaviour or terminology differs from the guide. Know both; answer per the guide. |
| **INVERTED** | Current docs describe the mechanism *differently in kind* from the guide. The highest-risk category. |

Last verification pass: **2026-08-12**. Re-run it with `/refresh-kb`.

---

## Domain 1 — Agentic Architecture & Orchestration

### `fork_session` — CONFIRMED
Exact spellings verified: `fork_session=True` (Python), `forkSession: true` (TypeScript). Used together with `resume` to branch a session; the fork gets its own ID and the original is untouched. Matches [1.7](../tasks/1-7.md).

*Source: `code.claude.com/docs/en/agent-sdk/sessions`*

### Session resumption — CHANGED (nuance)
The guide describes *"named session resumption using `--resume <session-name>`"*. Both halves are true but live in different places:

- **CLI**: `--resume` / `-r` accepts a session **ID or name**, or shows an interactive picker.
- **Agent SDK**: the `resume` option takes a session **ID**. Names are set separately via `rename_session()` / `renameSession()` and `tag_session()` / `tagSession()`.

Answer the guide's framing on the exam. In production, capture the ID from the result message.

### `continue` — EXTENDED
Not mentioned in the guide. `--continue` / `-c` (CLI) and `continue_conversation=True` / `continue: true` (SDK) resume the **most recent** session in the current directory with no ID tracking. It sits between "start fresh" and "resume a specific session" in [1.7](../tasks/1-7.md)'s decision space.

### Session storage — EXTENDED
Sessions persist at `~/.claude/projects/<encoded-cwd>/*.jsonl`. Useful context for [5.4](../tasks/5-4.md)'s crash-recovery discussion, not itself tested.

---

## Domain 2 — Tool Design & MCP Integration

### MCP scopes — CHANGED
The guide contrasts **two** scopes: project-level `.mcp.json` versus user-level `~/.claude.json`. Current docs define **three**:

| Scope | Loads in | Shared | Stored in |
|---|---|---|---|
| **Local** (the default) | Current project only | No | `~/.claude.json` |
| **Project** | Current project only | Yes, via version control | `.mcp.json` in project root |
| **User** | All your projects | No | `~/.claude.json` |

Precedence when a name collides: **local > project > user**. Note that *two different scopes both live in `~/.claude.json`* — the guide's "user-level `~/.claude.json` for personal/experimental servers" describes what the docs now split into local and user.

The exam's distinction — *shared team tooling versus personal/experimental* — is unaffected. See [2.4](../tasks/2-4.md).

*Source: `code.claude.com/docs/en/mcp`*

### Environment variable expansion — CONFIRMED
`${VAR}` expansion in `.mcp.json` is verified, and `${VAR:-default}` (with a fallback) is also supported. Matches [2.4](../tasks/2-4.md).

### MCP resources — CONFIRMED
Resources exist as a first-class concept alongside tools and prompts (`resources/list`). Servers can push `list_changed` notifications and Claude Code refreshes tools, prompts, and resources without a reconnect. Matches [2.4](../tasks/2-4.md).

### Project-server approval in headless mode — EXTENDED
Interactive sessions prompt for approval before using project-scoped `.mcp.json` servers. **`claude -p` runs, Agent SDK sessions, and cloud sessions cannot show that prompt and load project-scoped servers without asking.** Relevant to [3.6](../tasks/3-6.md) if you are wiring MCP into CI — not something the guide covers.

---

## Domain 3 — Claude Code Configuration & Workflows

### CLAUDE.md hierarchy — CONFIRMED, EXTENDED
The guide's three tiers are verified exactly:

- `~/.claude/CLAUDE.md` — user level, not shared through version control
- `./CLAUDE.md` or `./.claude/CLAUDE.md` — project level
- subdirectory `CLAUDE.md` files — directory level, loaded on demand when Claude reads files there

Two tiers the guide does not mention:

- **Managed policy** (organisation-wide, cannot be excluded by user settings): `/Library/Application Support/ClaudeCode/CLAUDE.md` on macOS, `/etc/claude-code/CLAUDE.md` on Linux/WSL, `C:\Program Files\ClaudeCode\CLAUDE.md` on Windows.
- **`./CLAUDE.local.md`** — personal, project-specific, gitignored.

Load order runs broadest to most specific, and all discovered files are concatenated rather than overriding one another. See [3.1](../tasks/3-1.md).

### `@import` — CONFIRMED
`@path/to/import` verified. Relative and absolute paths both work; relative paths resolve against the *importing file*, not the working directory. Maximum depth is **four hops**. Imports inside code spans or fenced blocks are skipped. Matches [3.1](../tasks/3-1.md).

### `.claude/rules/` with `paths:` globs — CONFIRMED, EXTENDED
YAML frontmatter with a `paths:` list of glob patterns is verified, and rules without a `paths` field load unconditionally at launch with the same priority as `.claude/CLAUDE.md`. Matches [3.3](../tasks/3-3.md) exactly.

Extensions beyond the guide: `~/.claude/rules/` for user-level rules (loaded *before* project rules, so project rules win), recursive discovery through subdirectories, symlink support, and brace expansion (`src/**/*.{ts,tsx}`).

### `/memory` versus `/context` — CHANGED ⚠️
**This one can cost you an item if you study only current docs.**

The guide lists, under [3.1](../tasks/3-1.md): *"Using the `/memory` command to verify which memory files are loaded and diagnose inconsistent behavior across sessions."*

Current docs split that job in two:

- **`/memory`** lists CLAUDE.md / CLAUDE.local.md locations across user and project scope, lets you open and edit them, and toggles auto memory.
- **`/context`** is what shows which files **actually loaded** into the current session, under a **Memory files** heading.

On the exam, `/memory` is the answer. In production, reach for `/context` when you are diagnosing "why isn't Claude following this file".

### Auto memory — EXTENDED
Entirely absent from the guide. Claude now writes its own notes to `~/.claude/projects/<project>/memory/`, with `MEMORY.md` as an index; the first 200 lines or 25 KB are loaded into every session. It is a second memory system alongside CLAUDE.md. Not exam material — but do not let it confuse your mental model of [3.1](../tasks/3-1.md).

### SKILL.md frontmatter — CONFIRMED fields, INVERTED semantics ⚠️

All three fields the guide names are verified to exist:

| Field | Status |
|---|---|
| `context: fork` | **CONFIRMED** — runs the skill in a forked subagent context |
| `argument-hint` | **CONFIRMED** — hint shown during autocomplete, e.g. `[issue-number]` |
| `allowed-tools` | **INVERTED** — see below |

**`allowed-tools` is the important one.** The guide describes it as a restriction:

> *"Configuring allowed-tools in skill frontmatter to restrict tool access during skill execution (e.g., limiting to file write operations to prevent destructive actions)."*

Current documentation defines it as a **pre-approval**:

> *"Tools Claude can use without asking permission during the turn that invokes this skill. The grant clears when you send your next message."*

Those are opposite in kind: the guide frames it as *taking capability away*, the docs frame it as *granting permission without a prompt*. **On the exam, answer the guide's framing** — restriction, least privilege, preventing destructive actions. It sits squarely in [least-privilege tooling](../heuristics/least-privilege-tooling.md), and item writers built against the guide. In production, know that it does not block anything; use `permissions.deny` in settings, or a `PreToolUse` hook, for actual enforcement.

Fields that exist but the guide does not mention: `name`, `disable-model-invocation`, `user-invocable`, `model`, `agent`.

*Source: `code.claude.com/docs/en/skills`*

### Slash commands and skills have merged — CHANGED
Current docs state plainly: *"Custom commands have been merged into skills."* A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both produce `/deploy` and behave the same way. Existing `.claude/commands/` files keep working.

The guide treats them as two mechanisms ([3.2](../tasks/3-2.md)), and the **scoping** facts it tests are unchanged and still correct:

- `.claude/commands/` — project-scoped, shared via version control
- `~/.claude/commands/` — user-scoped, personal

So an exam item asking *"where do you put a shared `/review` command?"* still answers `.claude/commands/` in the repository. Only the underlying implementation converged.

### CLI flags — CONFIRMED
All verified exactly as the guide describes:

- `-p` / `--print` — non-interactive mode
- `--output-format` — accepts `text`, `json`, `stream-json`
- `--json-schema` — validated JSON output against a schema, **print mode only**
- `--resume` / `-r`

Matches [3.6](../tasks/3-6.md). The guide names `--output-format json`; note the two other accepted values.

*Source: `code.claude.com/docs/en/cli-reference`*

---

## Domain 4 — Prompt Engineering & Structured Output

### `stop_reason` values — EXTENDED
The guide names `"tool_use"` and `"end_turn"` — the two that drive the agentic loop in [1.1](../tasks/1-1.md), and both are correct. The full current set also includes:

| Value | Meaning |
|---|---|
| `max_tokens` | Hit the output cap |
| `stop_sequence` | Hit a custom stop sequence |
| `pause_turn` | A server-side tool loop paused and can be resumed |
| `refusal` | The model declined on safety grounds |

`pause_turn` in particular is a real production case the loop must handle. It is not exam material, but a loop written only against the guide's two values is incomplete in production.

### `tool_choice` — CONFIRMED, EXTENDED
`"auto"`, `"any"`, and forced selection `{"type": "tool", "name": "..."}` are all verified and match [4.3](../tasks/4-3.md). A fourth value, `{"type": "none"}`, also exists (Claude cannot use tools) — not mentioned in the guide.

### Structured output — CHANGED ⚠️
The guide teaches, in [4.3](../tasks/4-3.md):

> *"Tool use (`tool_use`) with JSON schemas as the most reliable approach for guaranteed schema-compliant structured output, eliminating JSON syntax errors."*

That remains true and remains what the exam tests. But the API now also offers **native structured outputs**, which did not exist in this form when the technique was written:

- `output_config: {format: {type: "json_schema", schema: {...}}}` on `messages.create()` constrains the *response* to a schema.
- `strict: true` on a tool definition guarantees `tool_use.input` validates exactly.

There are also SDK helpers (`client.messages.parse()` with Pydantic or Zod) that validate automatically. The older top-level `output_format` parameter is deprecated in favour of `output_config.format`.

**On the exam, `tool_use` + JSON schema is the answer.** In production, native structured outputs are usually the better tool when you want a constrained *response* rather than a constrained *tool call*. The guide's key insight survives either way: **schemas eliminate syntax errors, not semantic ones** — line items that do not sum to the stated total still validate.

### Message Batches API — CONFIRMED, EXTENDED
Every fact the guide states is verified: **50% cost saving**, up to a **24-hour** processing window, **no guaranteed latency SLA**, `custom_id` for correlating request/response pairs. Matches [4.5](../tasks/4-5.md).

Additional limits not in the guide: up to 100,000 requests or 256 MB per batch, most batches complete within an hour, results retained for 29 days.

### Assistant prefill — EXTENDED
Not an exam topic, but worth knowing if you build against the guide's era: last-assistant-turn prefills now return a **400** on current frontier models. Structured outputs or a system-prompt instruction replace them.

---

## Domain 5 — Context Management & Reliability

No drift found in this pass. Domain 5 is largely about **architectural patterns** — summarisation loss, escalation triggers, error propagation, confidence calibration, provenance — rather than named APIs, which is exactly why it ages well. The `/compact` command referenced in [5.4](../tasks/5-4.md) is verified to exist.

---

## What this tells you about studying

Notice the shape of the drift: **every CHANGED or INVERTED entry is in Domain 3 or Domain 4** — the domains anchored to named commands, flags, and frontmatter fields. Domains 1, 2, and 5, which test *architectural judgment*, are almost entirely stable.

That is the same lesson the [heuristics](../heuristics/) notes teach from the other direction. Facts rot; judgment does not. If you have limited time, spend it on the reasoning patterns and treat the flag names as something to memorise last and re-verify with `/refresh-kb` before exam day.

## Re-running verification

```
/refresh-kb              # verify everything, report drift
/refresh-kb --domain 3   # just the fast-moving domain
/refresh-kb 2.4          # one task statement
```

The skill re-fetches official documentation, compares it against each note's recorded claims, and updates this log. It never silently rewrites a note to match current docs — the guide stays authoritative for the exam, and divergence is recorded here instead.
