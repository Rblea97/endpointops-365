from __future__ import annotations

import csv
from pathlib import Path


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def validate_required_columns(rows: list[dict[str, str]], required_fields: list[str]) -> list[str]:
    errors: list[str] = []
    for index, row in enumerate(rows, start=1):
        for field in required_fields:
            if field not in row or row[field] in (None, ""):
                errors.append(f"row {index} missing required field: {field}")
    return errors
