# Certifications

Each subdirectory is one certification study kit. The shared tooling — skills,
scripts, licence, disclaimer — lives at the repo root and works against any of
them.

| Slug | Certification | Exam code |
|---|---|---|
| [`ccar-f`](ccar-f/) | Claude Certified Architect – Foundations | `CCAR-F` |

## The contract

A certification directory is recognised by the tooling if it has
`questions/bank/`. Beyond that, keep this shape so the shared skills and scripts
work without special-casing:

```
certifications/<slug>/
├── README.md                    overview, exam facts at a glance, how to study
├── wiki/
│   ├── README.md                map of content — the entry point
│   ├── exam/
│   │   ├── blueprint.md         format, domain weights, task statement index
│   │   │                        + the guide version this kit is written against
│   │   ├── format-and-scoring.md
│   │   ├── out-of-scope.md      what is explicitly not tested
│   │   ├── drift-log.md         where current docs diverge from the guide
│   │   ├── logistics.md
│   │   └── preparation-plan.md
│   ├── heuristics/              cross-domain reasoning patterns
│   ├── domains/                 one note per content domain
│   ├── scenarios/               exam scenarios, if the exam uses them
│   ├── tasks/                   one note per task statement — the core unit
│   └── concepts/                atomic notes on the tested technology surface
├── questions/
│   ├── schema.md
│   ├── question-style-guide.md  distractor families for this exam
│   └── bank/d<N>-*.yaml         one file per domain
└── progress/
    ├── README.md
    └── state.example.json       empty; state.json is gitignored
```

`slug` is lowercase and hyphenated, and matches the exam code where there is one
(`ccar-f` for `CCAR-F`).

## Which parts the tooling depends on

| Path | Used by |
|---|---|
| `questions/bank/*.yaml` | `validate_questions.py`, `build_exam.py`, `/quiz`, `/mock-exam`, `/drill` |
| `wiki/tasks/<d>-<n>.md` | task statement coverage check; `/study`; every item's `task_statement` must resolve here |
| `wiki/exam/out-of-scope.md` | `/study` reads it before teaching, to decline untested topics |
| `wiki/exam/blueprint.md` | `/mock-exam` and `/progress` for weights and format |
| `wiki/exam/drift-log.md` | `/refresh-kb` writes findings here |
| `progress/state.json` | `/quiz`, `/drill`, `/progress`, `/mock-exam` |

Two things are **per-exam** rather than shared, and live in the certification's
own files: the **domain quota** in `build_exam.py` (currently CCAR-F's 60-item
split) and the **distractor families** in `question-style-guide.md`. If you add a
certification with a different blueprint, lift the quota out of the script into a
per-certification config rather than hardcoding a second one.

## Adding a certification

Open an issue first so the shape can be agreed before anyone writes 30 notes.

1. Create `certifications/<slug>/` with the layout above.
2. Write `wiki/exam/blueprint.md` first — it records the **guide version** the kit
   is written against, and every later note depends on the weights and task
   statement index it establishes.
3. Write the task statement notes. They are the core unit; concepts and heuristics
   are extracted from them, not the other way round.
4. Build the bank to a fixed items-per-task-statement target, so coverage is
   uniform and the validator's coverage check means something.
5. Run `python scripts/validate_questions.py --cert <slug>` until it exits 0.
6. Add a row to the table above and to the root [README](../README.md).

## The two rules that matter

**No exam content.** Task statement *titles* from a published guide are a factual
index and may be reproduced with attribution. Everything else — explanations,
practice items, analysis — must be original. Never reproduce a guide's sample
questions. See [DISCLAIMER.md](../DISCLAIMER.md).

**The guide governs, current docs are drift.** A kit is written against a specific
guide version, and that is what the exam was written against too. When live
documentation disagrees, record it in `drift-log.md` and note which framing the
exam expects — do not silently rewrite the note to match today's docs.
