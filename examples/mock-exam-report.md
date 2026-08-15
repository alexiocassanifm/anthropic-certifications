# Sample output — CCAR-F mock exam report

> Unedited output from one 60-item run of `/mock-exam`, kept in the repo so you can see what
> the diagnostic produces before installing anything. The collapsed domain is left in on
> purpose — a strong average hiding one weak domain is exactly the case this report exists
> to catch, and a sample where everything went well would show you nothing.

**Form** · seed `815` · scenarios 1, 3, 5, 6 · 60 items · 51 of 120 minutes used · 11 off-scenario fills

---

## Result

**46/60 = 77% correct**

**Would this have passed? Not computable.** The exam passes at a scaled 720 on a 100–1,000
range, and the raw percentage that maps to 720 varies by form. A result in the low-to-mid
70s is the trap case: it looks like it clears "720 must be 72%", which is exactly the
inference the official scoring notes warn against. This kit never emits a scaled score.

**Against the bar it *can* apply — not ready.** Target is above 80% overall with no domain
below 70%. Both fail: 77% overall, Domain 2 at 55%.

## By domain

| Domain | Weight | Score | % | |
|---|---|---|---|---|
| 1 — Agentic Architecture & Orchestration | 27% | 13/16 | **81%** | 🟢 |
| 2 — Tool Design & MCP Integration | 18% | 6/11 | **55%** | 🔴 |
| 3 — Claude Code Configuration & Workflows | 20% | 11/12 | **92%** | 🟢 |
| 4 — Prompt Engineering & Structured Output | 20% | 9/12 | **75%** | 🟡 |
| 5 — Context Management & Reliability | 15% | 7/9 | **78%** | 🟡 |

## Per-task-statement misses, with the command to fix each

| Task statement | Score | Teach it | Then test it |
|---|---|---|---|
| 2.4 — MCP server integration | 0/1 | `/study 2.4` | `/quiz --task 2.4` |
| 4.5 — Batch processing strategies | 0/1 | `/study 4.5` | `/quiz --task 4.5` |
| 2.3 — Tool distribution and `tool_choice` | 1/3 | `/study 2.3` | `/quiz --task 2.3` |
| 3.2 — Custom commands and skills | 1/2 | `/study 3.2` | `/quiz --task 3.2` |
| 5.6 — Provenance and multi-source synthesis | 1/2 | `/study 5.6` | `/quiz --task 5.6` |
| 1.1 — Agentic loops | 2/3 | `/study 1.1` | `/quiz --task 1.1` |
| 1.2 — Coordinator-subagent patterns | 2/3 | `/study 1.2` | `/quiz --task 1.2` |
| 1.3 — Subagent invocation and context passing | 2/3 | `/study 1.3` | `/quiz --task 1.3` |
| 2.1 — Tool interfaces and descriptions | 2/3 | `/study 2.1` | `/quiz --task 2.1` |
| 2.2 — Structured error responses | 2/3 | `/study 2.2` | `/quiz --task 2.2` |
| 4.1 — Explicit criteria and precision | 2/3 | `/study 4.1` | `/quiz --task 4.1` |
| 4.6 — Multi-instance and multi-pass review | 2/3 | `/study 4.6` | `/quiz --task 4.6` |
| 5.1 — Preserving context across long interactions | 2/3 | `/study 5.1` | `/quiz --task 5.1` |

## Distractor families — ranked by rate, not count

Rate is `chosen ÷ times that family appeared as a wrong option on this form`.

| Family | Chosen | Present | Rate |
|---|---|---|---|
| `prompt-instead-of-enforcement` | 3 | 15 | **20.0%** |
| `blames-wrong-component` | 2 | 20 | **10.0%** |
| `suppresses-signal` | 1 | 13 | **7.7%** |
| `solves-different-problem` | 6 | 82 | **7.3%** |
| `unreliable-proxy` | 1 | 16 | **6.2%** |
| `over-engineered` | 1 | 25 | **4.0%** |

`solves-different-problem` has the largest raw count and **carries no signal** — it is
roughly half the wrong options on any form, so sitting at its base rate means the general
skill of matching a fix to the stated cause is intact. Ranking by count would have named it
the problem. The real finding is `prompt-instead-of-enforcement` at ~2.6× its availability:
reaching for an instruction where a configuration value already guaranteed the outcome, or
where the information did not yet exist to be reasoned about.

---

## Every missed item (14)

### Item 1 · `d2-2.3-003` · Domain 2, TS 2.3
*Scenario 6 — Structured Data Extraction*

> You have several extraction schemas and the document type is not known in advance. You need to guarantee the model returns structured output rather than a prose reply. Which tool_choice configuration is appropriate?

**Chose B** — tool_choice set to "auto", with a system prompt instruction always to call an extraction tool.
❌ This makes a guarantee depend on instruction compliance when a configuration value provides it outright. *(`prompt-instead-of-enforcement`)*

**Correct A** — tool_choice set to "any".
✅ "any" forces a tool call while leaving the model free to select the schema that fits the document, which is exactly the situation described.

### Item 6 · `d2-2.3-002` · Domain 2, TS 2.3
*Scenario 3 — Multi-Agent Research System*

> An agent has grown from five tools to eighteen as new capabilities were added. Tool selection accuracy has measurably declined even though each new tool is well described. What is the most likely explanation?

**Chose A** — The newer tools' descriptions must conflict with the original five, which needs a consistency review.
❌ The stem states each new tool is well described. Breadth degrades selection even when every description is individually good. *(`blames-wrong-component`)*

**Correct D** — Giving an agent access to many tools increases decision complexity and degrades selection reliability, independently of individual description quality.
✅ Breadth itself is the cost. Each additional tool is another candidate to discriminate among at selection time, and reliability falls as the set grows.

### Item 9 · `d2-2.2-002` · Domain 2, TS 2.2
*Scenario 1 — Customer Support Resolution Agent*

> A refund request exceeds the customer's eligibility window. The tool correctly rejects it. What should the error response contain so the agent responds appropriately?

**Chose B** — errorCategory of validation, retryable set to true, so the agent can prompt the customer for corrected input.
❌ The input was valid; the request is ineligible. Marking it retryable invites a pointless retry loop, and no corrected input would succeed. *(`solves-different-problem`)*

**Correct D** — errorCategory of business, retryable set to false, and a customer-friendly explanation of the eligibility rule.
✅ A business rule violation is not retryable, and the agent's correct next action is to communicate rather than retry. The customer-friendly explanation gives it the words to do so.

### Item 15 · `d4-4.6-003` · Domain 4, TS 4.6
*Scenario 5 — Claude Code for Continuous Integration*

> You are designing a review architecture for large changes. Which TWO approaches are consistent with the guide's recommendations? Select TWO.

**Chose A** — Run three passes and report only findings that appear in at least two.
❌ Consensus filtering discards intermittently detected bugs, which are the ones most worth surfacing. *(`suppresses-signal`)*

**Correct B** — Run verification passes in which the model self-reports confidence alongside each finding, to enable calibrated review routing.
✅ Finding-level confidence used to route reviewer attention is an endorsed skill, distinct from using self-reported confidence as a proxy for overall case complexity.

**Correct C** — Split large reviews into per-file passes for local issues plus a separate cross-file integration pass.
✅ Multi-pass review addresses attention dilution directly, and the integration pass covers what per-file analysis structurally cannot.

### Item 19 · `d4-4.1-002` · Domain 4, TS 4.1
*Scenario 5 — Claude Code for Continuous Integration*

> One of five review categories has a roughly 40% false positive rate. Developers have begun ignoring all review comments, including from the four accurate categories. What is the most effective immediate action?

**Chose A** — Lower the global confidence threshold across all five categories.
❌ This degrades four working categories to compensate for one, and relies on an uncalibrated confidence signal. *(`unreliable-proxy`)*

**Correct C** — Temporarily disable the high-false-positive category while its criteria are improved, restoring trust in the remaining four.
✅ Trust is per-category and one noisy category undermines confidence in the accurate ones. Removing the noise recovers the value of the categories that work while the broken one is fixed.

### Item 20 · `d4-4.5-003` · Domain 4, TS 4.5
*Scenario 6 — Structured Data Extraction*

> You must guarantee that every submitted document is processed within 30 hours, using an API whose batch processing window is up to 24 hours. What submission cadence satisfies the requirement?

**Chose A** — Submit every four hours and escalate to synchronous processing for any batch still running at 24 hours.
❌ The four-hour cadence already satisfies the SLA, so the fallback path adds complexity with no benefit. *(`over-engineered`)*

**Correct C** — Submit batches every four hours, leaving headroom between the maximum processing window and the SLA.
✅ A document arriving just after a submission waits up to four hours to be included, then up to 24 to process, for a worst case of 28 hours — inside the 30-hour commitment.

### Item 26 · `d2-2.1-003` · Domain 2, TS 2.1
*Scenario 3 — Multi-Agent Research System*

> After rewriting two tool descriptions to be detailed and clearly differentiated, misrouting between them persists at the same rate. The system prompt includes the line "For any question about content, use the content analysis tool." What should you investigate next?

**Chose A** — The tools' input schemas — overlapping parameter names cause the model to confuse them.
❌ Schemas describe what a tool accepts once chosen. They are not the primary selection signal, and the stem gives no indication of a schema problem. *(`blames-wrong-component`)*

**Correct D** — The system prompt — keyword-sensitive instructions can create unintended tool associations that override well-written descriptions.
✅ A system prompt phrase that names a tool by a keyword pulls selection toward it regardless of description quality. When good descriptions do not change behaviour, the prompt is the next place to look.

### Item 38 · `d3-3.2-003` · Domain 3, TS 3.2
*Off-scenario fill*

> Your team has a shared release skill. You want a personal variant with an extra step, without changing behaviour for anyone else. What is the appropriate approach?

**Chose D** — Copy the project skill into ~/.claude/skills/ under the same name so yours takes precedence.
❌ Reusing the name creates a shadowing relationship that is easy to forget and hard to diagnose when the shared skill later changes. *(`solves-different-problem`)*

**Correct B** — Create a variant in ~/.claude/skills/ under a different name.
✅ Personal customisation belongs in user scope, and using a different name avoids any collision with the shared skill your teammates depend on.

### Item 42 · `d5-5.6-002` · Domain 5, TS 5.6
*Scenario 3 — Multi-Agent Research System*

> Your synthesis agent flags a contradiction between two documents reporting adoption rates of 34% and 51%. Investigation shows the figures were collected two years apart. What change prevents this class of false contradiction?

**Chose D** — Instruct the synthesis agent to consider whether figures might be from different time periods.
❌ The agent cannot consider a date it was never given. The information has to be present before it can be reasoned about. *(`prompt-instead-of-enforcement`)*

**Correct C** — Require publication or data collection dates in subagents' structured outputs.
✅ Without dates, temporal differences are indistinguishable from disagreements. Carrying the date lets synthesis read the pair as a trend rather than a conflict.

### Item 44 · `d1-1.3-001` · Domain 1, TS 1.3
*Scenario 3 — Multi-Agent Research System*

> Your synthesis subagent produces reports that contradict the findings the search subagent returned earlier in the same run. Inspecting the synthesis subagent's prompt shows it receives only the research topic and a instruction to "synthesise the findings". What is the most effective fix?

**Chose C** — Strengthen the synthesis subagent's system prompt to instruct it to base conclusions only on findings from other agents.
❌ The agent cannot base conclusions on findings it never received. The instruction is unfollowable regardless of how it is worded. *(`prompt-instead-of-enforcement`)*

**Correct D** — Include the complete findings from the search and analysis subagents directly in the synthesis subagent's prompt.
✅ Subagents run with isolated context and do not inherit the coordinator's conversation history. If the synthesis agent is to use prior findings, they must be explicitly provided in its prompt.

### Item 49 · `d1-1.1-003` · Domain 1, TS 1.1
*Scenario 3 — Multi-Agent Research System*

> You are reviewing an agentic loop implementation before it ships. Which TWO of the following are anti-patterns that should be corrected? Select TWO.

**Chose D** — The loop executes all tool_use blocks returned in a single response before issuing the next request.
❌ Also correct behaviour. A response may contain several tool requests, and all of their results should be returned together. *(`solves-different-problem`)*

**Correct A** — The loop parses the assistant's natural-language output to decide whether the task is finished.
✅ Termination is inferred from prose rather than read from stop_reason. This is brittle and probabilistic when a reliable typed signal exists.

**Correct C** — The loop relies on a fixed iteration cap as its primary stopping mechanism.
✅ A cap is a safety net, not control flow. Used as the primary mechanism it truncates work arbitrarily at a boundary unrelated to whether the task is actually done.

### Item 50 · `d2-2.4-002` · Domain 2, TS 2.4
*Off-scenario fill*

> You added an MCP server exposing a powerful code-search tool, but Claude consistently uses the built-in Grep tool instead. The MCP tool's description reads "Searches the codebase." What is the most effective fix?

**Chose A** — Remove Grep from the agent's allowed tools so the MCP tool is the only option.
❌ This forces the outcome by removing a legitimately useful built-in tool, and leaves the description problem in place for any future overlap. *(`solves-different-problem`)*

**Correct D** — Expand the MCP tool's description to explain its capabilities and outputs in detail, including what it can do that a plain text search cannot.
✅ The model selects on descriptions. A one-line description that sounds like a subset of Grep gives it no reason to prefer the MCP tool, however capable that tool actually is.

### Item 52 · `d5-5.1-002` · Domain 5, TS 5.1
*Scenario 3 — Multi-Agent Research System*

> A synthesis agent receives a long aggregated input containing findings from four subagents. It consistently reflects the first and last subagents' findings but omits material from the middle. What is the most appropriate mitigation?

**Chose D** — Send each subagent's findings in a separate request and merge the four outputs.
❌ Synthesis requires seeing the findings together. Merging four separate syntheses loses the cross-cutting connections that synthesis exists to make. *(`solves-different-problem`)*

**Correct C** — Place a key findings summary at the beginning of the aggregated input and organise the detail under explicit section headers.
✅ Models process the beginning and end of long inputs reliably and may omit middle sections. Front-loading the summary and adding structure mitigates the position effect directly.

### Item 55 · `d1-1.2-002` · Domain 1, TS 1.2
*Scenario 3 — Multi-Agent Research System*

> A teammate proposes letting the document analysis subagent send results directly to the synthesis subagent, arguing it removes a hop through the coordinator and cuts latency. How should you evaluate this proposal?

**Chose C** — Accept it — the coordinator adds no value to a handoff between two agents that already know their roles.
❌ This optimises for latency while discarding the three properties the topology exists to provide. Latency is not the constraint the pattern was chosen to satisfy. *(`solves-different-problem`)*

**Correct B** — Reject it — routing all subagent communication through the coordinator is what provides observability, consistent error handling, and controlled information flow.
✅ The hub-and-spoke pattern centralises communication deliberately. Direct subagent links remove the single place that can observe what happened, handle failures uniformly, and decide what each agent should know.

---

Generated by `/mock-exam`. The same report can be published as a styled HTML artifact.
