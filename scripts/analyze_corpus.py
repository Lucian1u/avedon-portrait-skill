#!/usr/bin/env python3

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "research" / "annotated-corpus.csv"
FIELDS = (
    "framing_scale",
    "head_view",
    "face_visibility",
    "crop_pattern",
    "gaze_direction",
    "mouth_state",
    "hands_visibility",
    "hand_relation",
    "subject_placement",
    "background_tone",
    "key_direction",
    "shadow_hardness",
    "overall_contrast",
    "black_border_visible",
)


def first_year(value):
    match = re.search(r"(?:18|19|20)\d{2}", value or "")
    return int(match.group()) if match else None


def method_period(value):
    year = first_year(value)
    if year is None:
        return "unclear"
    return "mature_1969_onward" if year >= 1969 else "pre_mature_before_1969"


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def format_counts(values):
    counts = Counter(values)
    return ", ".join(f"{value}={count}" for value, count in counts.most_common())


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CORPUS
    rows = read_rows(path)
    if not rows:
        raise SystemExit(f"no corpus rows in {path}")

    print(f"corpus: {path}")
    print(f"records: {len(rows)}")
    print("subsets: " + format_counts(row["analysis_subset"] for row in rows))
    print("review: " + format_counts(row["needs_review"] for row in rows))
    print("method_period: " + format_counts(method_period(row["work_date"]) for row in rows))

    scope_eligible = [
        row
        for row in rows
        if row["v1_candidate"] == "true" and row["image_structure"] == "single_frame"
    ]
    route_eligible = [row for row in scope_eligible if row["needs_review"] == "false"]
    mature_route_eligible = [
        row for row in route_eligible if method_period(row["work_date"]) == "mature_1969_onward"
    ]
    print(f"scope_eligible: {len(scope_eligible)}")
    print(f"route_eligible: {len(route_eligible)}")
    print(f"mature_route_eligible: {len(mature_route_eligible)}")

    for subset in ("formal_portrait_general", "in_the_american_west"):
        subset_rows = [row for row in rows if row["analysis_subset"] == subset]
        print(f"\n[{subset}] records={len(subset_rows)}")
        for field in FIELDS:
            print(f"{field}: {format_counts(row[field] for row in subset_rows)}")

    support = defaultdict(list)
    for row in route_eligible:
        support[
            (
                row["analysis_subset"],
                row["framing_scale"],
                row["head_view"],
                row["face_visibility"],
                row["crop_pattern"],
            )
        ].append(row["record_id"])

    print("\n[exact structural support ids; route-eligible records]")
    for key in sorted(support):
        print(" / ".join(key) + f" ({len(support[key])}): " + ", ".join(support[key]))


if __name__ == "__main__":
    main()
