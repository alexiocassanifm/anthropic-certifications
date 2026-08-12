# Anthropic Certifications

Open-source study kits for the Anthropic certification program. Each certification
gets a linked wiki, an original practice-question bank, and a set of Claude Code
skills that teach, quiz, and track readiness against it.

> **Unofficial.** Not affiliated with, endorsed by, or sponsored by Anthropic.
> Contains **no exam content**. See [DISCLAIMER.md](DISCLAIMER.md).

## Certifications

| Slug | Certification | Exam code | Status |
|---|---|---|---|
| [`ccar-f`](certifications/ccar-f/) | Claude Certified Architect – Foundations | `CCAR-F` | Complete — 30 task statements, 90 practice items |

More will be added as they are studied. See [Adding a certification](certifications/README.md).

## What you get, per certification

- **A wiki** — every task statement in the blueprint, plus atomic concept notes,
  domain overviews, exam scenarios, and the cross-domain reasoning heuristics that
  generalise across items. Plain Markdown with relative links, so it renders on
  GitHub and navigates in Obsidian.
- **A practice bank** — original items with a documented schema, tagged by task
  statement, scenario, and distractor family. Every option carries an explanation;
  the explanations *are* the study material.
- **A drift log** — where current official documentation diverges from the exam
  guide the certification was written against. Recorded, not silently applied.

## Quick start

```bash
git clone https://github.com/alexiocassanifm/anthropic-certifications.git
cd anthropic-certifications
pip install -r requirements.txt      # PyYAML, for the scripts
claude                                # open Claude Code at the repo root
```

Then:

```
/study 1.4          # learn one task statement
/quiz --domain 2    # short targeted quiz
/mock-exam          # full timed simulation
/progress           # readiness dashboard
/drill              # spaced repetition on weak areas
/refresh-kb         # re-verify a wiki against current official docs
```

The skills resolve which certification you mean: they use the only one present, or
you name it. Run them from the **repo root**, not from inside a certification
directory — the skills and scripts live at the root and are shared.

Or install as a Claude Code plugin, from any project:

```
/plugin install alexiocassanifm/anthropic-certifications
```

## Layout

```
├── certifications/
│   ├── README.md            conventions + how to add one
│   └── ccar-f/
│       ├── README.md        this certification's overview
│       ├── wiki/            the knowledge base
│       ├── questions/       schema, style guide, item bank
│       └── progress/        your local state (gitignored)
├── .claude/
│   ├── skills/              seven shared, certification-aware skills
│   └── commands/            slash command wrappers
├── scripts/                 shared validator + mock exam builder
├── DISCLAIMER.md            applies to every kit here
├── CONTRIBUTING.md
└── LICENSE                  MIT (code) + CC BY-SA 4.0 (content)
```

**Shared at the root:** skills, scripts, licence, disclaimer, contributing guide.
**Per certification:** wiki, questions, progress.

That split is the point of the parent repo — write the tooling once, and each new
certification is content rather than plumbing.

## Scripts

```bash
python scripts/validate_questions.py              # the only certification
python scripts/validate_questions.py --cert ccar-f
python scripts/build_exam.py --cert ccar-f --seed 1
```

With one certification present it is the default. With several, `--cert` is
required — guessing would silently validate the wrong bank.

## Reading a wiki without Claude

Everything under `certifications/<slug>/wiki/` is plain Markdown. Browse it on
GitHub, or point Obsidian at the repo — both resolve the same relative links. If
you keep an Obsidian vault elsewhere, symlink the wiki into it:

```bash
ln -s "$(pwd)/certifications/ccar-f/wiki" /path/to/vault/ccar-f
```

## Contributing

Practice items, corrections, and new certifications are all welcome. The one hard
rule: **never contribute real exam content.** See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Code is MIT. Wiki and question content are CC BY-SA 4.0. See [LICENSE](LICENSE).
