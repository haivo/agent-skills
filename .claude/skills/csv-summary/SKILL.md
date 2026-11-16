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

   The script prints raw JSON only. It does no formatting. The object has:
   - `file`: the path that was read
   - `rows`: row count (header excluded)
   - `columns`: list of column names in file order
   - `numeric`: map of column name to `{min, max, mean}` for columns whose
     non-empty values all parse as numbers. Text columns are absent from it.

   If the object has an `error` key instead, the file was not found or is not
   valid CSV.
3. Write the report yourself from the JSON, in this layout:
   - One sentence: `<rows> rows, <n> columns: <col1>, <col2>, ...`
   - A blank line, then a markdown table with columns `Column | Min | Max | Mean`,
     one row per entry in `numeric`, in the order the JSON lists them. Print
     numbers as they appear in the JSON; do not round further.
   - If `numeric` is empty, write `No numeric columns.` instead of the table.
   - If `rows` is 0, write only `<file> has 0 rows.`
4. If the JSON has an `error` key, show its message and ask the user to check
   the path.

## Notes
- Use the `py -3.14` launcher; plain `python` is not on PATH on this machine.
- A test file lives at `.claude/skills/csv-summary/samples/sales.csv`.
- The script owns the numbers; this file owns the layout. To change how the
  report looks, edit step 3 above, not the script.
