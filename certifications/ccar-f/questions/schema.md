# Question item schema

Items live in `questions/bank/d<N>-*.yaml`, one file per domain. Each file is a YAML list of item objects.

Validate with:

```bash
python scripts/validate_questions.py
```

## Shape

```yaml
- id: d1-1.1-003              # <domain>-<task statement>-<3-digit sequence>, unique across the bank
  domain: 1                   # 1-5
  task_statement: "1.1"       # must exist in wiki/tasks/
  scenario: [1, 3]            # exam scenario ids this fits; null = domain-generic
  select_count: 1             # how many responses to select; stated in the stem
  stem: >
    Production logs show ...
  options:
    - id: A
      text: "..."
      verdict: correct
      why: "Why this is right."
    - id: B
      text: "..."
      verdict: wrong
      why: "Why this is wrong."
      distractor_family: over-engineered
  correct: [A]                # array, always — even for single-answer items
  source: original
```

## Fields

| Field | Required | Notes |
|---|---|---|
| `id` | ✅ | `d<domain>-<task>-<NNN>`. Unique across the whole bank. |
| `domain` | ✅ | Integer 1–5. Must match the `task_statement` prefix. |
| `task_statement` | ✅ | Quoted string, e.g. `"1.1"`. Must correspond to a file in `wiki/tasks/`. |
| `scenario` | ✅ | List of exam scenario ids (1–6), or `null` for domain-generic items. |
| `select_count` | ✅ | Integer ≥ 1. Must equal `len(correct)`. |
| `stem` | ✅ | The question. Describe a production symptom, not a definition. |
| `options` | ✅ | 4 options, ids `A`–`D`. |
| `options[].verdict` | ✅ | `correct` or `wrong`. |
| `options[].why` | ✅ | On **every** option. This is the study material. |
| `options[].distractor_family` | ✅ on wrong options | One of the families in [`question-style-guide.md`](question-style-guide.md). |
| `correct` | ✅ | List of option ids. Length must equal `select_count`. |
| `source` | ✅ | Always `original`. See [`../DISCLAIMER.md`](../../../DISCLAIMER.md). |

## Why `correct` is a list

The exam uses **multiple-choice and multiple-response** items, and each item states how many responses to select. Modelling `correct` as an array from the start means multiple-response items need no schema migration — and the grading logic in `/quiz` and `/mock-exam` has one code path instead of two.

For a single-answer item, `select_count: 1` and `correct: [A]`.

## Multiple-response items

```yaml
- id: d2-2.2-002
  select_count: 2
  stem: >
    ... Select TWO.
  correct: [B, D]
```

State the count in the stem, exactly as the real exam does. The validator enforces that `select_count == len(correct)`, but only a human can check that the stem says so.

## Naming and coverage

`scripts/validate_questions.py` enforces:

- unique ids
- `len(correct) == select_count`
- every option carries a `why`
- every wrong option carries a valid `distractor_family`
- `task_statement` resolves to a real wiki note
- `domain` matches the task statement prefix
- **every one of the 30 task statements has at least one item**

It reports per-domain counts so you can see the bank against the [blueprint](../wiki/exam/blueprint.md) weights.
