---
name: csv-summary
description: Summarize a local CSV file: row count, column names, and a table of min/max/mean for numeric columns. Use when the user asks to inspect, profile, or get quick stats on a .csv file.
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

   The script prints the finished report: one sentence with row and column
   counts, then a markdown table of numeric columns. A line starting with
   `Error:` means the file was not found or is not valid CSV.
3. Show the script output verbatim. Do not reformat, reorder, or add to it.
4. If the output starts with `Error:`, show it and ask the user to check the path.

## Notes
- Use the `py -3.14` launcher; plain `python` is not on PATH on this machine.
- A test file lives at `.claude/skills/csv-summary/samples/sales.csv`.
- The report layout lives in `scripts/summarize.py` (`format_table`). To change
  how results look, edit the script.
