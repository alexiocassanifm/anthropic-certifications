---
name: setup
description: Clone the anthropic-certifications study kit into a repository you own, and check that its scripts can run. Use once, to get set up.
disable-model-invocation: true
---

# Set up the study kit

This plugin does not contain the study kit. It clones it.

The kit is a repository you work *in*: `/refresh-kb` rewrites wiki notes when the
official documentation moves, `/author-question` appends to the question bank, and
every session writes your progress. Those edits are only worth something in a
working tree you can commit and open a pull request from. A plugin is copied into
`~/.claude/plugins/cache/`, where the next `/plugin update` discards whatever you
wrote. So the kit lives in a clone, and this skill puts one where you want it.

## 1. Check you are not already there

If the current directory contains both `certifications/` and `.claude/skills/study/`,
the user is already inside a clone. Say so, tell them to run `/study 1.1` or
`/progress`, and stop. Do not clone again.

## 2. Check git

Run `git --version`. If git is missing, say so and stop — point them at
<https://git-scm.com/downloads>. Everything below needs it.

## 3. Agree on a location

Ask where to put the kit, offering `~/anthropic-certifications` as the default and
saying they can accept it or name another path. This will be a git repository they
own and study in, so somewhere they will find it again.

Before cloning, check the path:

- Exists and is not empty → say so and ask for a different path. Never clone into
  or over an existing directory's contents.
- Exists and is empty, or does not exist → fine, proceed.

## 4. Clone

```bash
git clone https://github.com/alexiocassanifm/anthropic-certifications.git <path>
```

If the clone fails, report the actual error rather than guessing — no network, no
proxy, and a full disk all look different.

## 5. Check the Python scripts can run

Two skills shell out to Python: `/mock-exam` builds a form with
`scripts/build_exam.py`, and `/author-question` validates with
`scripts/validate_questions.py`. Both need PyYAML. Nothing else does — the wiki,
`/study`, `/quiz`, `/drill`, and `/progress` need no dependencies at all.

Check it:

```bash
python3 -c "import yaml; print(yaml.__version__)"
```

If that fails, offer to install it, and say which command you are about to run:

```bash
python3 -m pip install -r <path>/requirements.txt
```

Mention that a virtual environment is the tidier option if they prefer one, and
that declining is fine — five of the seven skills work without it, and they can
install it later.

## 6. Hand over

Print the next step plainly. They must open Claude Code *in the clone*, because the
seven study skills are project-scoped under the repo's `.claude/` and load only
when the repo is the working directory:

```bash
cd <path>
claude
```

Then, in that session:

```
/study 1.1          # learn one task statement, then get checked on it
/mock-exam          # 60-item timed simulation and a diagnostic report
/progress           # readiness dashboard
```

Tell them two more things:

- The first launch in the clone asks them to trust the folder, because the repo
  ships a `SessionStart` hook that checks how long ago the wiki was verified.
  Declining is fine — everything still works, they just run `/refresh-kb`
  themselves.
- The skills are `/study`, not `/cert-study-kit:study`. This plugin's only skill is
  the one they just ran; the study skills come from the clone.

Finally, point at the repository's `README.md` for what the kit does and
`CONTRIBUTING.md` for how to add practice items, and note that the kit is
unofficial — not written, reviewed, or endorsed by Anthropic, and containing no
exam content. `DISCLAIMER.md` in the clone is the full version.
