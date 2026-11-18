"""Tool registry: maps each tool name to its function and its schema.

TOOLS is what we send to the model so it knows what it can call.
FUNCTIONS is what we use to actually run a call the model asked for.
"""

import json

from . import csv_checks

_PATH_SCHEMA = {
    "type": "object",
    "properties": {
        "path": {"type": "string", "description": "Path to the CSV file."}
    },
    "required": ["path"],
    "additionalProperties": False,
}

TOOLS = [
    {
        "name": "describe_csv",
        "description": "Get the row count, column names, and the first three rows of a CSV file. Call this first.",
        "input_schema": _PATH_SCHEMA,
        "strict": True,
    },
    {
        "name": "find_blank_cells",
        "description": "Count blank cells in each column of a CSV file.",
        "input_schema": _PATH_SCHEMA,
        "strict": True,
    },
    {
        "name": "check_column_types",
        "description": "For each column, report the dominant value type (number or text) and list cells that do not match it.",
        "input_schema": _PATH_SCHEMA,
        "strict": True,
    },
    {
        "name": "find_duplicate_rows",
        "description": "Find rows that appear more than once in a CSV file.",
        "input_schema": _PATH_SCHEMA,
        "strict": True,
    },
]

FUNCTIONS = {
    "describe_csv": csv_checks.describe_csv,
    "find_blank_cells": csv_checks.find_blank_cells,
    "check_column_types": csv_checks.check_column_types,
    "find_duplicate_rows": csv_checks.find_duplicate_rows,
}


def execute_tool(name: str, tool_input: dict) -> tuple[str, bool]:
    """Run one tool. Returns (result_text, is_error)."""
    fn = FUNCTIONS.get(name)
    if fn is None:
        return f"Unknown tool: {name}", True
    try:
        return json.dumps(fn(**tool_input), indent=2), False
    except FileNotFoundError:
        return f"File not found: {tool_input.get('path')}", True
    except Exception as e:  # report the error to the model instead of crashing
        return f"{type(e).__name__}: {e}", True
