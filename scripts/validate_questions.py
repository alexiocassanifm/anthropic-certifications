#!/usr/bin/env python3
"""Validate the CCAR-F practice question bank.

Checks structural integrity, blueprint coverage, and style-guide conformance.
Exits 0 when the bank is clean, 1 otherwise.

    python scripts/validate_questions.py
    python scripts/validate_questions.py --quiet
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install it with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "questions" / "bank"
TASKS = ROOT / "wiki" / "tasks"

# Blueprint: domain -> (weight %, items on a 60-item form)
BLUEPRINT = {1: (27, 16), 2: (18, 11), 3: (20, 12), 4: (20, 12), 5: (15, 9)}

DISTRACTOR_FAMILIES = {
    "prompt-instead-of-enforcement",
    "over-engineered",
    "solves-different-problem",
    "blames-wrong-component",
    "unreliable-proxy",
    "suppresses-signal",
    "shifts-burden",
}

ID_RE = re.compile(r"^d(\d)-(\d\.\d)-(\d{3})$")


def load_bank() -> list[tuple[Path, dict]]:
    """Return every item paired with the file it came from."""
    items: list[tuple[Path, dict]] = []
    for path in sorted(BANK.glob("*.yaml")):
        loaded = yaml.safe_load(path.read_text()) or []
        if not isinstance(loaded, list):
            sys.exit(f"{path.name}: expected a YAML list of items")
        items.extend((path, item) for item in loaded)
    return items


def known_task_statements() -> set[str]:
    """Task statement ids that have a wiki note, e.g. '1.1' from 1-1.md."""
    return {p.stem.replace("-", ".") for p in TASKS.glob("*.md")}


def check_item(path: Path, item: dict, seen_ids: set[str], tasks: set[str]) -> list[str]:
    errs: list[str] = []
    where = f"{path.name}"
    item_id = item.get("id", "<no id>")

    def err(msg: str) -> None:
        errs.append(f"{where} [{item_id}]: {msg}")

    for field in ("id", "domain", "task_statement", "select_count", "stem",
                  "options", "correct", "source"):
        if field not in item:
            err(f"missing required field '{field}'")
    if errs:
        return errs
    if "scenario" not in item:
        err("missing required field 'scenario' (use null for domain-generic)")

    m = ID_RE.match(str(item_id))
    if not m:
        err("id must match d<domain>-<task>-<NNN>")
    else:
        if int(m.group(1)) != item["domain"]:
            err("id domain prefix does not match the domain field")
        if m.group(2) != item["task_statement"]:
            err("id task segment does not match the task_statement field")

    if item_id in seen_ids:
        err("duplicate id")
    seen_ids.add(item_id)

    ts = item["task_statement"]
    if ts not in tasks:
        err(f"task_statement '{ts}' has no note in wiki/tasks/")
    elif not str(ts).startswith(f"{item['domain']}."):
        err(f"task_statement '{ts}' does not belong to domain {item['domain']}")

    if item["source"] != "original":
        err("source must be 'original'")

    scen = item.get("scenario")
    if scen is not None:
        if not isinstance(scen, list) or not all(isinstance(s, int) and 1 <= s <= 6 for s in scen):
            err("scenario must be null or a list of ids in 1..6")

    options = item["options"]
    if not isinstance(options, list) or len(options) != 4:
        err("expected exactly 4 options")
        return errs

    ids = [o.get("id") for o in options]
    if ids != ["A", "B", "C", "D"]:
        err(f"option ids must be A, B, C, D in order (got {ids})")

    correct_from_verdict = []
    for opt in options:
        oid = opt.get("id", "?")
        if not opt.get("text", "").strip():
            err(f"option {oid} has no text")
        if not opt.get("why", "").strip():
            err(f"option {oid} has no 'why' — every option must explain itself")
        verdict = opt.get("verdict")
        if verdict == "correct":
            correct_from_verdict.append(oid)
        elif verdict == "wrong":
            fam = opt.get("distractor_family")
            if not fam:
                err(f"option {oid} is wrong but has no distractor_family")
            elif fam not in DISTRACTOR_FAMILIES:
                err(f"option {oid} has unknown distractor_family '{fam}'")
        else:
            err(f"option {oid} has invalid verdict '{verdict}'")

    correct = item["correct"]
    if not isinstance(correct, list) or not correct:
        err("'correct' must be a non-empty list of option ids")
    else:
        if sorted(correct) != sorted(correct_from_verdict):
            err(f"'correct' {sorted(correct)} disagrees with option verdicts "
                f"{sorted(correct_from_verdict)}")
        if len(correct) != item["select_count"]:
            err(f"select_count is {item['select_count']} but 'correct' has {len(correct)}")
        if len(set(correct)) != len(correct):
            err("'correct' contains duplicates")

    if item["select_count"] > 1 and "select" not in item["stem"].lower():
        err("multiple-response item should state the count in the stem "
            "(e.g. 'Select TWO.')")

    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quiet", action="store_true", help="only print problems")
    args = ap.parse_args()

    tasks = known_task_statements()
    if not tasks:
        sys.exit("No task statement notes found in wiki/tasks/")

    entries = load_bank()
    if not entries:
        sys.exit("No items found in questions/bank/")

    errors: list[str] = []
    seen_ids: set[str] = set()
    per_domain: Counter[int] = Counter()
    per_task: Counter[str] = Counter()
    per_family: Counter[str] = Counter()
    per_scenario: Counter[int] = Counter()
    generic = 0

    for path, item in entries:
        errors.extend(check_item(path, item, seen_ids, tasks))
        if isinstance(item.get("domain"), int):
            per_domain[item["domain"]] += 1
        per_task[str(item.get("task_statement"))] += 1
        for opt in item.get("options", []) or []:
            if opt.get("distractor_family"):
                per_family[opt["distractor_family"]] += 1
        scen = item.get("scenario")
        if scen:
            for s in scen:
                per_scenario[s] += 1
        else:
            generic += 1

    uncovered = sorted(tasks - set(per_task), key=lambda t: tuple(map(int, t.split("."))))
    for t in uncovered:
        errors.append(f"coverage: task statement {t} has no items")

    if not args.quiet:
        print(f"Loaded {len(entries)} items from {len(list(BANK.glob('*.yaml')))} files\n")

        print("Per-domain coverage vs blueprint")
        print(f"  {'domain':<8}{'items':>7}{'weight':>9}{'on a 60-item form':>20}")
        for d in sorted(BLUEPRINT):
            weight, at60 = BLUEPRINT[d]
            print(f"  {d:<8}{per_domain[d]:>7}{weight:>8}%{at60:>20}")
        print(f"  {'total':<8}{sum(per_domain.values()):>7}{'100%':>9}{60:>20}\n")

        thin = [t for t, n in sorted(per_task.items()) if n < 3]
        print(f"Task statements covered: {len(per_task)}/{len(tasks)}")
        if thin:
            print(f"  Fewer than 3 items ({len(thin)}): {', '.join(thin)}")
        print()

        print("Distractor family distribution")
        for fam, n in per_family.most_common():
            print(f"  {fam:<32}{n:>4}")
        unused = DISTRACTOR_FAMILIES - set(per_family)
        if unused:
            print(f"  unused: {', '.join(sorted(unused))}")
        print()

        print("Scenario tagging")
        for s in range(1, 7):
            print(f"  scenario {s}: {per_scenario[s]}")
        print(f"  domain-generic (scenario: null): {generic}\n")

    if errors:
        print(f"FAILED — {len(errors)} problem(s):\n", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1

    print("OK — bank is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
