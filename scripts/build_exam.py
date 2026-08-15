#!/usr/bin/env python3
"""Assemble a blueprint-weighted 60-item mock exam form.

Mirrors the real exam's structure: 4 scenarios drawn from a bank of 6, with
per-domain item counts matching the published blueprint weights.

    python scripts/build_exam.py                     # random form
    python scripts/build_exam.py --cert ccar-f       # pick a certification
    python scripts/build_exam.py --seed 1            # reproducible form
    python scripts/build_exam.py --json              # machine-readable
    python scripts/build_exam.py --check 20          # 20 forms, report shortfalls

Allocation rule
---------------
Because each exam scenario declares only 2-3 primary domains (scenario 2 covers
domains 3 and 5 only), a form cannot be both scenario-pure and weight-exact.
The blueprint weights win. For each domain, in turn:

  1. Prefer items tagged with one of the four selected scenarios.
  2. Fall back to domain-generic items (scenario: null).
  3. If still short, take any remaining item in that domain and record it as an
     off-scenario fill.

Option order
------------
Each item's four options are permuted per form. The bank stores them in a fixed
order, so without this a learner who runs several forms starts recognising
positions instead of reasoning. The form reports, per item, which bank option
sits in each presentation slot and which slots are correct.

Shortfalls and off-scenario fills are always reported, never silent.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install it with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent

CERTS = ROOT / "certifications"


def resolve_cert(slug: str | None) -> Path:
    """Return the certification directory to operate on.

    With one certification present, it is the default. With several, --cert is
    required — guessing would silently validate the wrong bank.
    """
    available = sorted(p.name for p in CERTS.iterdir()
                       if p.is_dir() and (p / "questions" / "bank").is_dir())
    if not available:
        sys.exit(f"No certifications found under {CERTS}/")
    if slug:
        if slug not in available:
            sys.exit(f"Unknown certification '{slug}'. Available: {', '.join(available)}")
        return CERTS / slug
    if len(available) == 1:
        return CERTS / available[0]
    sys.exit(f"Several certifications present ({', '.join(available)}). "
             f"Pass --cert <slug>.")

# Blueprint weights applied to 60 items, rounded to sum to exactly 60.
DOMAIN_QUOTA = {1: 16, 2: 11, 3: 12, 4: 12, 5: 9}
TOTAL = sum(DOMAIN_QUOTA.values())
SCENARIOS_PER_FORM = 4
SCENARIO_POOL = [1, 2, 3, 4, 5, 6]

SCENARIO_NAMES = {
    1: "Customer Support Resolution Agent",
    2: "Code Generation with Claude Code",
    3: "Multi-Agent Research System",
    4: "Developer Productivity with Claude",
    5: "Claude Code for Continuous Integration",
    6: "Structured Data Extraction",
}


def load_items(bank: Path) -> list[dict]:
    items: list[dict] = []
    for path in sorted(bank.glob("*.yaml")):
        items.extend(yaml.safe_load(path.read_text()) or [])
    return items


SLOTS = ["A", "B", "C", "D"]


def order_options(item: dict, rng: random.Random) -> tuple[list[str], list[str]]:
    """Permute one item's options for presentation.

    Returns (order, correct) where order[i] is the bank option id to show in
    slot SLOTS[i], and correct is the slot letters that are correct. Callers
    present the options in `order` relabelled A-D and grade against `correct` —
    never against the bank's own 'correct' field, which refers to bank ids.
    """
    order = [o["id"] for o in item["options"]]
    rng.shuffle(order)
    slot_of = {bank_id: SLOTS[i] for i, bank_id in enumerate(order)}
    return order, sorted(slot_of[c] for c in item["correct"])


def build_form(items: list[dict], rng: random.Random) -> dict:
    scenarios = sorted(rng.sample(SCENARIO_POOL, SCENARIOS_PER_FORM))
    chosen = set(scenarios)

    by_domain: dict[int, list[dict]] = defaultdict(list)
    for it in items:
        by_domain[it["domain"]].append(it)

    selected: list[dict] = []
    off_scenario: list[str] = []
    shortfalls: list[str] = []

    for domain in sorted(DOMAIN_QUOTA):
        quota = DOMAIN_QUOTA[domain]
        pool = by_domain[domain][:]
        rng.shuffle(pool)

        on = [i for i in pool if i.get("scenario") and chosen & set(i["scenario"])]
        generic = [i for i in pool if not i.get("scenario")]
        other = [i for i in pool if i.get("scenario") and not chosen & set(i["scenario"])]

        picked = on[:quota]
        if len(picked) < quota:
            picked += generic[: quota - len(picked)]
        if len(picked) < quota:
            fill = other[: quota - len(picked)]
            off_scenario.extend(i["id"] for i in fill)
            picked += fill
        if len(picked) < quota:
            shortfalls.append(
                f"domain {domain}: needed {quota}, found {len(picked)} "
                f"(bank has {len(pool)} items in this domain)"
            )
        selected.extend(picked)

    rng.shuffle(selected)

    orders: dict[str, list[str]] = {}
    correct: dict[str, list[str]] = {}
    for it in selected:
        orders[it["id"]], correct[it["id"]] = order_options(it, rng)

    return {
        "scenarios": scenarios,
        "items": selected,
        "option_order": orders,
        "correct": correct,
        "off_scenario": off_scenario,
        "shortfalls": shortfalls,
    }


def print_form(form: dict) -> None:
    counts: dict[int, int] = defaultdict(int)
    for it in form["items"]:
        counts[it["domain"]] += 1

    print("Mock exam form")
    print(f"  items:     {len(form['items'])} / {TOTAL}")
    print(f"  time limit: 120 minutes")
    print(f"  seed:      {form['seed']}  (rebuild with --seed {form['seed']})\n")

    print("Scenarios in this form (4 of 6):")
    for s in form["scenarios"]:
        print(f"  {s}. {SCENARIO_NAMES[s]}")
    print()

    print("Per-domain allocation:")
    ok = True
    for d in sorted(DOMAIN_QUOTA):
        got, want = counts[d], DOMAIN_QUOTA[d]
        mark = "ok" if got == want else "MISMATCH"
        if got != want:
            ok = False
        print(f"  domain {d}: {got:>2} / {want:<2}  {mark}")
    print()

    if form["off_scenario"]:
        print(f"Off-scenario fills ({len(form['off_scenario'])}) — these items are tagged")
        print("to scenarios not in this form, used to meet the domain quota:")
        for i in form["off_scenario"]:
            print(f"  {i}")
        print()

    if form["shortfalls"]:
        print("SHORTFALLS — the bank could not fill these quotas:")
        for s in form["shortfalls"]:
            print(f"  {s}")
        print()

    print("Item ids, in presentation order.")
    print("'opts' is which bank option goes in slot A, B, C, D:")
    for n, it in enumerate(form["items"], 1):
        scen = ",".join(map(str, it["scenario"])) if it.get("scenario") else "generic"
        opts = "".join(form["option_order"][it["id"]])
        print(f"  {n:>2}. {it['id']:<16} ts {it['task_statement']:<5} "
              f"[{scen}]  opts {opts}")

    if not ok or form["shortfalls"]:
        print("\nForm did not meet the blueprint exactly. See above.")


def check(items: list[dict], runs: int) -> int:
    """Build many forms and report whether any could not be filled."""
    bad = 0
    fills = 0
    for n in range(runs):
        form = build_form(items, random.Random(n))
        counts: dict[int, int] = defaultdict(int)
        for it in form["items"]:
            counts[it["domain"]] += 1
        exact = all(counts[d] == DOMAIN_QUOTA[d] for d in DOMAIN_QUOTA)
        fills += len(form["off_scenario"])
        if not exact or form["shortfalls"]:
            bad += 1
            print(f"seed {n}: FAILED — {form['shortfalls'] or dict(counts)}")
    print(f"\n{runs} forms built, {runs - bad} met the blueprint exactly.")
    if runs:
        print(f"Off-scenario fills across all forms: {fills} "
              f"(avg {fills / runs:.1f} per form).")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cert", help="certification slug, e.g. ccar-f")
    ap.add_argument("--seed", type=int, help="reproducible form")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--check", type=int, metavar="N",
                    help="build N forms and report shortfalls")
    args = ap.parse_args()

    cert = resolve_cert(args.cert)
    items = load_items(cert / "questions" / "bank")
    if not items:
        sys.exit(f"No items found in {cert / 'questions' / 'bank'}")

    if args.check is not None:
        return check(items, args.check)

    # An unseeded run must still be reproducible after the fact, so draw the seed
    # explicitly and report it rather than letting Random() take system entropy.
    seed = args.seed if args.seed is not None else random.randrange(2**31)
    form = build_form(items, random.Random(seed))
    form["seed"] = seed

    if args.json:
        print(json.dumps({
            "seed": seed,
            "scenarios": form["scenarios"],
            "item_ids": [i["id"] for i in form["items"]],
            "items": {
                i["id"]: {
                    "domain": i["domain"],
                    "task_statement": i["task_statement"],
                    "select_count": i["select_count"],
                    "scenario": i.get("scenario"),
                }
                for i in form["items"]
            },
            "option_order": form["option_order"],
            "correct": form["correct"],
            "off_scenario": form["off_scenario"],
            "shortfalls": form["shortfalls"],
        }, indent=2))
    else:
        print_form(form)

    return 1 if form["shortfalls"] else 0


if __name__ == "__main__":
    sys.exit(main())
