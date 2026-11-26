---
name: csv-profile
description: Profile a local CSV file and report it as both JSON and a table: row count, columns, and min/max/mean of numeric columns. Use when the user asks to profile, inspect, or get quick stats on a .csv file.
allowed-tools: Bash(py -3.14 .claude/skills/csv-profile/scripts/profile.py:*), Read
---

# CSV profile

## When to use
- The user names a .csv file and wants to know what is in it or asks for quick stats.
- Do not use for Excel files or for editing the CSV.

## How to run
1. Resolve the file path the user gave. If none is given, ask which file.
2. Run from the project root:

   ```bash
   py -3.14 .claude/skills/csv-profile/scripts/profile.py "<path>"
   ```

   The script prints the finished report: a lead sentence, a fenced JSON
   block, then a markdown table of numeric columns and a note on text columns.
   A line starting with `Error:` means the file was not found or is not valid CSV.
3. Show the script output verbatim. Do not reformat, reorder, or add to it.
4. If the output starts with `Error:`, read `templates/report.md` in this
   skill's folder and fill in its error section.

## Notes
- Use the `py -3.14` launcher; plain `python` is not on PATH on this machine.
- A test file lives at `.claude/skills/csv-profile/samples/sales.csv`.
- The report layout lives in `scripts/profile.py` (`format_json` and
  `format_table`). To change how results look, edit the script. Only the
  error message layout remains in `templates/report.md`.
