"""Plain Python functions that inspect a CSV file.

None of these know anything about the model. They take a path, return a
dictionary, and can be tested directly.
"""

import csv
from collections import Counter


def _load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _guess_type(value):
    if value == "":
        return "blank"
    try:
        float(value)
        return "number"
    except ValueError:
        return "text"


def describe_csv(path: str) -> dict:
    """Row count, column names, and the first three rows."""
    rows = _load(path)
    columns = list(rows[0].keys()) if rows else []
    return {"rows": len(rows), "columns": columns, "sample": rows[:3]}


def find_blank_cells(path: str) -> dict:
    """Count blank cells per column."""
    rows = _load(path)
    columns = list(rows[0].keys()) if rows else []
    blanks = {c: sum(1 for r in rows if r[c] == "") for c in columns}
    return {"blank_cells": {c: n for c, n in blanks.items() if n > 0}}


def check_column_types(path: str) -> dict:
    """For each column, the dominant type and any cells that do not match it."""
    rows = _load(path)
    columns = list(rows[0].keys()) if rows else []
    result = {}
    for c in columns:
        types = Counter(_guess_type(r[c]) for r in rows if r[c] != "")
        if not types:
            result[c] = {"dominant": "blank", "mismatches": []}
            continue
        dominant = types.most_common(1)[0][0]
        mismatches = [
            {"row": i + 2, "value": r[c]}  # header is line 1, data starts at line 2
            for i, r in enumerate(rows)
            if r[c] != "" and _guess_type(r[c]) != dominant
        ]
        result[c] = {"dominant": dominant, "mismatches": mismatches}
    return {"columns": result}


def find_duplicate_rows(path: str) -> dict:
    """Rows that appear more than once, with their line numbers."""
    rows = _load(path)
    seen = {}
    for i, r in enumerate(rows):
        key = tuple(r.values())
        seen.setdefault(key, []).append(i + 2)
    dupes = [
        {"row_lines": lines, "values": list(k)}
        for k, lines in seen.items()
        if len(lines) > 1
    ]
    return {"duplicates": dupes}
