# Progress state

Your personal study state lives in `progress/state.json`. It is **gitignored** —
never commit it.

`state.example.json` is an **empty** starting point. The skills create it for you
on first run, so you normally do not need to copy it by hand. It contains no
sample data deliberately: a dashboard that reports a mock exam you never sat is
worse than no dashboard.

## Shape

```jsonc
{
  "schema_version": 1,
  "created": "2026-08-12",         // ISO date, set on first write
  "last_session": "2026-08-12",
  "task_statements": {
    "1.1": {                        // keyed by task statement id
      "confidence": 3,              // 0-5, your current grasp
      "seen": 6,                    // items answered for this statement
      "correct": 5,
      "last_reviewed": "2026-08-12",
      "ease": 2.5,                  // SM-2-lite, starts 2.5, range 1.3-2.8
      "interval_days": 4,           // days until next review
      "due": "2026-08-16",
      "seen_ids": ["d1-1.1-001"],   // item ids already served
      "notes": "Solid on stop_reason control flow."
    }
  },
  "mock_exams": [
    {
      "date": "2026-08-12",
      "scenarios": [1, 3, 4, 6],
      "items": 60,
      "correct": 41,
      "percent_overall": 68,
      "percent_by_domain": { "1": 69, "2": 64, "3": 75, "4": 67, "5": 67 },
      "duration_minutes": 96
    }
  ]
}
```

## Which skill writes what

| Skill | Writes |
|---|---|
| `/study` | `confidence`, `last_reviewed`, `seen_ids`, `notes` |
| `/quiz` | `seen`, `correct`, `seen_ids`, `last_reviewed`, `confidence` |
| `/drill` | the SM-2-lite fields — `ease`, `interval_days`, `due` — plus the above |
| `/mock-exam` | appends to `mock_exams`, and updates per-statement entries |
| `/progress` | reads only |

No scaled score is ever recorded. See
[`../wiki/exam/format-and-scoring.md`](../wiki/exam/format-and-scoring.md).
