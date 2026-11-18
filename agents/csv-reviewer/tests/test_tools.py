"""Tests for the tools only. No model, no network, no API key needed."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools import execute_tool  # noqa: E402
from tools.csv_checks import (  # noqa: E402
    check_column_types,
    describe_csv,
    find_blank_cells,
    find_duplicate_rows,
)

CLEAN = "region,product,units,price\nNorth,Desk,12,199.99\nSouth,Chair,30,89.50\n"
MESSY = (
    "region,product,units,price\n"
    "North,Desk,12,199.99\n"
    "South,Chair,,89.50\n"        # blank units
    "East,Lamp,many,24.00\n"      # text in a number column
    "North,Desk,12,199.99\n"      # duplicate of line 2
)


def write(tmp_path, text):
    p = tmp_path / "data.csv"
    p.write_text(text, encoding="utf-8")
    return str(p)


def test_describe_csv(tmp_path):
    out = describe_csv(write(tmp_path, CLEAN))
    assert out["rows"] == 2
    assert out["columns"] == ["region", "product", "units", "price"]


def test_clean_file_has_no_problems(tmp_path):
    p = write(tmp_path, CLEAN)
    assert find_blank_cells(p) == {"blank_cells": {}}
    assert find_duplicate_rows(p) == {"duplicates": []}
    assert all(c["mismatches"] == [] for c in check_column_types(p)["columns"].values())


def test_blank_cells_are_counted(tmp_path):
    out = find_blank_cells(write(tmp_path, MESSY))
    assert out == {"blank_cells": {"units": 1}}


def test_type_mismatch_is_found(tmp_path):
    out = check_column_types(write(tmp_path, MESSY))
    units = out["columns"]["units"]
    assert units["dominant"] == "number"
    assert units["mismatches"] == [{"row": 4, "value": "many"}]


def test_duplicate_rows_are_found(tmp_path):
    out = find_duplicate_rows(write(tmp_path, MESSY))
    assert out["duplicates"] == [
        {"row_lines": [2, 5], "values": ["North", "Desk", "12", "199.99"]}
    ]


def test_execute_tool_reports_missing_file():
    text, is_error = execute_tool("describe_csv", {"path": "nope.csv"})
    assert is_error is True
    assert "not found" in text


def test_execute_tool_rejects_unknown_name():
    text, is_error = execute_tool("make_coffee", {})
    assert is_error is True
