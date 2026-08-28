#!/usr/bin/env python3

import csv
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "avedon-portrait" if (ROOT / "avedon-portrait").is_dir() else ROOT
POOL = ROOT / "research" / "reference-pool.csv"
PILOT = ROOT / "research" / "pilot-corpus.csv"
CORPUS = ROOT / "research" / "annotated-corpus.csv"
CITATION_FILES = (
    ROOT / "research" / "corpus-findings.md",
    ROOT / "research" / "v2-framing-search.md",
    SKILL_ROOT / "references" / "transformation-fallbacks.md",
    SKILL_ROOT / "references" / "style-dna.md",
    SKILL_ROOT / "references" / "portrait-routes.md",
    SKILL_ROOT / "references" / "supported-routes.md",
)

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff", ".bmp", ".heic"}
POOL_REQUIRED = {
    "pool_id",
    "title",
    "work_date",
    "source_institution",
    "source_url",
    "practice",
    "subject_count_from_title",
    "v1_candidate",
    "source_checked_on",
}
PILOT_REQUIRED = {
    "record_id",
    "title",
    "source_institution",
    "source_url",
    "analysis_subset",
    "subject_count",
    "image_structure",
    "framing_scale",
    "head_view",
    "head_tilt",
    "chin_angle",
    "torso_view",
    "face_visibility",
    "crop_pattern",
    "pose_motion",
    "black_border_visible",
    "observed_notes",
    "annotation_confidence",
    "annotated_on",
}

ENUMS = {
    "analysis_subset": {"formal_portrait_general", "in_the_american_west"},
    "practice": {"portrait", "fashion", "reportage", "advertising", "unclear"},
    "v1_candidate": {"true", "review", "false"},
    "framing_scale": {
        "face_detail",
        "tight_head",
        "head_and_shoulders",
        "bust",
        "waist_up",
        "three_quarter_body",
        "full_body",
        "unclear",
    },
    "face_visibility": {"full", "partial", "none", "occluded", "unclear"},
    "annotation_confidence": {"high", "medium", "low"},
    "needs_review": {"true", "false"},
    "image_structure": {"single_frame", "diptych", "triptych", "other_composite", "unclear"},
    "head_view": {
        "frontal",
        "three_quarter_facing_image_left",
        "three_quarter_facing_image_right",
        "profile_facing_image_left",
        "profile_facing_image_right",
        "back",
        "over_shoulder",
        "unclear",
    },
    "head_tilt": {"level", "toward_image_left", "toward_image_right", "not_assessable", "unclear"},
    "chin_angle": {"neutral", "raised", "lowered", "not_assessable", "unclear"},
    "torso_view": {
        "frontal",
        "three_quarter_facing_image_left",
        "three_quarter_facing_image_right",
        "profile_facing_image_left",
        "profile_facing_image_right",
        "back",
        "not_visible",
        "unclear",
    },
    "crop_pattern": {
        "none",
        "face_fragment_image_left_edge",
        "face_fragment_image_right_edge",
        "top_of_head",
        "chin_or_jaw",
        "hand_or_arm",
        "leg_or_foot",
        "multiple",
        "other",
        "unclear",
    },
    "pose_motion": {"still", "gesture_in_progress", "dynamic", "not_assessable", "unclear"},
    "black_border_visible": {"yes", "no", "unclear"},
}


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def validate_required_headers(path: Path, fields, required, errors):
    missing = sorted(required - set(fields))
    if missing:
        errors.append(f"{path.name}: missing headers {missing}")


def validate_unique(rows, field, label, errors):
    values = [row.get(field, "").strip() for row in rows]
    duplicates = sorted(value for value, count in Counter(values).items() if value and count > 1)
    if duplicates:
        errors.append(f"{label}: duplicate {field} values {duplicates[:10]}")
    if any(not value for value in values):
        errors.append(f"{label}: blank {field}")


def validate_urls(rows, label, errors):
    for index, row in enumerate(rows, start=2):
        url = row.get("source_url", "").strip()
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{label}:{index}: invalid source_url {url!r}")


def validate_enums(rows, label, errors):
    for index, row in enumerate(rows, start=2):
        for field, allowed in ENUMS.items():
            if field not in row:
                continue
            value = row[field].strip()
            if value and value not in allowed:
                errors.append(f"{label}:{index}: invalid {field}={value!r}")


def main():
    errors = []
    pool_fields, pool_rows = read_csv(POOL)
    pilot_fields, pilot_rows = read_csv(PILOT)
    corpus_fields, corpus_rows = read_csv(CORPUS)

    validate_required_headers(POOL, pool_fields, POOL_REQUIRED, errors)
    validate_required_headers(PILOT, pilot_fields, PILOT_REQUIRED, errors)
    validate_required_headers(CORPUS, corpus_fields, PILOT_REQUIRED, errors)
    validate_unique(pool_rows, "pool_id", "reference-pool.csv", errors)
    validate_unique(pilot_rows, "record_id", "pilot-corpus.csv", errors)
    validate_unique(corpus_rows, "record_id", "annotated-corpus.csv", errors)
    validate_urls(pool_rows, "reference-pool.csv", errors)
    validate_urls(pilot_rows, "pilot-corpus.csv", errors)
    validate_urls(corpus_rows, "annotated-corpus.csv", errors)
    validate_enums(pool_rows, "reference-pool.csv", errors)
    validate_enums(pilot_rows, "pilot-corpus.csv", errors)
    validate_enums(corpus_rows, "annotated-corpus.csv", errors)

    if len(pool_rows) < 80:
        errors.append(f"reference-pool.csv: expected at least 80 rows, found {len(pool_rows)}")
    if len(pilot_rows) != 20:
        errors.append(f"pilot-corpus.csv: expected exactly 20 rows, found {len(pilot_rows)}")
    if len(corpus_rows) < 80:
        errors.append(f"annotated-corpus.csv: expected at least 80 rows, found {len(corpus_rows)}")

    pilot_ids = {row["record_id"] for row in pilot_rows}
    corpus_ids = {row["record_id"] for row in corpus_rows}
    if missing_pilot_ids := sorted(pilot_ids - corpus_ids):
        errors.append(f"annotated-corpus.csv: missing pilot IDs {missing_pilot_ids}")

    pool_urls = {row["source_url"].strip() for row in pool_rows}
    corpus_urls = {row["source_url"].strip() for row in corpus_rows}
    if missing_corpus_urls := sorted(corpus_urls - pool_urls):
        errors.append(f"reference-pool.csv: missing annotated source URLs {missing_corpus_urls}")

    route_eligible = [
        row
        for row in corpus_rows
        if row["v1_candidate"] == "true"
        and row["image_structure"] == "single_frame"
        and row["needs_review"] == "false"
    ]
    subset_counts = Counter(row["analysis_subset"] for row in corpus_rows)
    if subset_counts["formal_portrait_general"] < 30:
        errors.append("annotated-corpus.csv: general subset has fewer than 30 records")
    if subset_counts["in_the_american_west"] < 30:
        errors.append("annotated-corpus.csv: In the American West subset has fewer than 30 records")

    for path in CITATION_FILES:
        cited_ids = set(re.findall(r"AP-(?:PIL|EXP)-[A-Z]+-\d+", path.read_text(encoding="utf-8")))
        if missing_ids := sorted(cited_ids - corpus_ids):
            errors.append(f"{path.name}: unknown corpus IDs {missing_ids}")

    image_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in IMAGE_SUFFIXES
        and "release" not in path.relative_to(ROOT).parts
    ]
    visual_eval_root = ROOT / "evals" / "visual"
    disallowed_images = [path for path in image_files if visual_eval_root not in path.parents]
    if disallowed_images:
        errors.append(
            "copyright boundary: image files outside evals/visual: "
            + ", ".join(str(path.relative_to(ROOT)) for path in disallowed_images)
        )
    if image_files and not (visual_eval_root / "manifest.md").is_file():
        errors.append("evals/visual: image fixtures require manifest.md")

    domains = Counter(urlparse(row["source_url"]).netloc.lower() for row in pool_rows if row.get("source_url"))
    print(f"reference pool rows: {len(pool_rows)}")
    print(f"pilot rows: {len(pilot_rows)}")
    print(f"annotated rows: {len(corpus_rows)}")
    print(f"route-eligible rows: {len(route_eligible)}")
    print(
        "annotated subsets: "
        + ", ".join(f"{subset}={count}" for subset, count in sorted(subset_counts.items()))
    )
    print("source domains: " + ", ".join(f"{domain}={count}" for domain, count in sorted(domains.items())))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("research validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
