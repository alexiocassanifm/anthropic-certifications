---
title: "Domain 4: Prompt Engineering & Structured Output"
domain: 4
weight: 20
items_at_60: 12
task_statements: 6
---

# Domain 4: Prompt Engineering & Structured Output

**20% of the exam — 12 items at 60.**

## What this domain is about

Getting reliable, machine-usable output. Writing criteria specific enough to control precision; using examples where instructions fail; guaranteeing shape with tool use and JSON schemas; recovering when the output is wrong; choosing between synchronous and batch processing; and structuring review so that quality does not dissolve under load.

The unifying idea: **specificity beats exhortation.** Almost every wrong answer in this domain is a version of asking the model to try harder — "be conservative", "only report high-confidence findings", "be accurate". Almost every right answer replaces that with something concrete: a categorical criterion, an example, a schema, a validation rule.

## Task statements

| ID | Title | Core idea |
|---|---|---|
| [4.1](../tasks/4-1.md) | Design prompts with explicit criteria to improve precision and reduce false positives | Categorical criteria, not confidence thresholds |
| [4.2](../tasks/4-2.md) | Apply few-shot prompting to improve output consistency and quality | Examples where instructions alone produce variation |
| [4.3](../tasks/4-3.md) | Enforce structured output using tool use and JSON schemas | Tool use eliminates syntax errors, not semantic ones |
| [4.4](../tasks/4-4.md) | Implement validation, retry, and feedback loops for extraction quality | Retry with the specific error; know when retry cannot help |
| [4.5](../tasks/4-5.md) | Design efficient batch processing strategies | Batch for latency-tolerant work, never for blocking work |
| [4.6](../tasks/4-6.md) | Design multi-instance and multi-pass review architectures | Independent instances and focused passes beat one big pass |

## The through-lines

**"Be conservative" is not a criterion.** General instructions to raise the bar do not improve precision. What does: defining which categories to report (bugs, security) and which to skip (minor style, local patterns), with concrete code examples for each severity level. And when one category floods developers with false positives, the move is to **disable that category temporarily** to restore trust while you fix its prompt — not to lower a global threshold. Trust is per-category, and a noisy category poisons confidence in the accurate ones. See [4.1](../tasks/4-1.md).

**Examples teach judgment; instructions teach rules.** Few-shot is the most effective technique when detailed instructions still produce inconsistent results, when the hard part is an ambiguous case, and when you need the model to **generalise** to patterns you did not enumerate. Two to four targeted examples that show *why* one action was chosen over a plausible alternative beat a long list of rules. Notice the count: the guide talks about 2–4 targeted examples, not 5–8 generic ones — volume is not the mechanism. See [4.2](../tasks/4-2.md).

**Tool use is the structured-output mechanism.** Define the extraction schema as a tool's input schema and read the result from the `tool_use` response. This eliminates JSON syntax errors entirely. It does **not** prevent semantic errors — line items that do not sum to the stated total, values placed in the wrong field. Knowing exactly where that guarantee stops is the most testable point in the domain. See [4.3](../tasks/4-3.md).

**`tool_choice` is the guarantee knob.** `"auto"` lets the model reply in prose instead of calling anything. `"any"` forces a tool call but leaves the choice open — right when several extraction schemas exist and the document type is unknown. Forced selection (`{"type": "tool", "name": "extract_metadata"}`) pins a specific tool, which is how you make one extraction run before an enrichment step. See [4.3](../tasks/4-3.md).

**Nullable fields prevent fabrication.** If a source document may not contain the information, make the field optional. A required field is an instruction to produce *something*, and the model will comply. Add `"unclear"` enum values for ambiguous cases and an `"other"` + detail string for extensible categories. See [4.3](../tasks/4-3.md).

**Retry only fixes what retry can fix.** Sending back the original document, the failed extraction, and the specific validation error lets the model self-correct format and structural problems. It cannot conjure information that is simply absent from the source. Distinguishing "the model got it wrong" from "the data is not there" is the whole of [4.4](../tasks/4-4.md).

**Batch is a latency trade, not a cost lever you can pull anywhere.** 50% cheaper, up to a 24-hour window, no latency SLA, and **no multi-turn tool calling within a request**. Right for overnight reports, weekly audits, nightly test generation. Wrong for anything blocking — a pre-merge check where a developer is waiting. When a manager proposes moving everything to batch, the answer splits the workflows. See [4.5](../tasks/4-5.md).

**Attention dilutes across a large pass.** One review of fourteen files produces detailed feedback on some, superficial comments on others, and contradictions between them. Splitting into per-file local passes plus a separate cross-file integration pass fixes it at the cause. Requiring humans to submit smaller PRs shifts the burden without improving the system; consensus voting across three runs suppresses real findings that are only caught intermittently. See [4.6](../tasks/4-6.md).

## Where the failures live

- A review category with a 40% false positive rate that has quietly destroyed trust in the other four
- Extractions that "succeed" with fabricated values because every field was required
- A validation-retry loop that burns tokens re-asking for information the document never contained
- A blocking pre-merge check moved to the Batches API and now completing sometime tomorrow
- A single-pass review contradicting itself within one pull request
- The generating session reviewing its own code and finding nothing

## Preparation

Build a small extraction pipeline: a tool with a JSON schema containing required, optional, and nullable fields plus an `"other"` + detail enum; documents where some fields are genuinely absent; a validation-retry loop that feeds back specific errors; few-shot examples covering structurally varied documents. Then submit 100 documents through the Message Batches API, handle failures by `custom_id`, and compute whether your total processing time fits a stated SLA.

## Related

- Scenarios: [5](../scenarios/5-claude-code-for-continuous-integration.md), [6](../scenarios/6-structured-data-extraction.md)
- [Domain 5](5-context-management-and-reliability.md) — confidence calibration and human review continue where validation ends
