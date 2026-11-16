---
name: csv-summary
description: Summarize a local CSV file: row count, column names, and min/max/mean of numeric columns. Use when the user asks to inspect, profile, or get quick stats on a .csv file.
allowed-tools: Bash(py -3.14 .claude/skills/csv-summary/scripts/summarize.py:*), Read
---

# CSV summary

## When to use
- The user names a .csv file and wants to know what is in it or asks for quick stats.
- Do not use for Excel files or for editing the CSV.

## How to run
1. Resolve the file path the user gave. If none is given, ask which file.
2. Run from the project root:

   ```bash
   py -3.14 .claude/skills/csv-summary/scripts/summarize.py "<path>"
   ```

   Output is JSON with `rows`, `columns`, and `numeric` (per-column min, max, mean).
   A line starting with `Error:` means the file was not found or is not valid CSV.
3. Report rows and columns in one sentence, then a table of numeric columns.
4. If the output starts with `Error:`, show it and ask the user to check the path.

## Notes
- Use the `py -3.14` launcher; plain `python` is not on PATH on this machine.
- A test file lives at `.claude/skills/csv-summary/samples/sales.csv`.
