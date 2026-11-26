import csv
import json
import statistics
import sys


def load_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def numeric_stats(rows):
    stats = {}
    for col in rows[0].keys():
        try:
            values = [float(r[col]) for r in rows if r[col] != ""]
        except ValueError:
            continue
        if values:
            stats[col] = {
                "min": min(values),
                "max": max(values),
                "mean": round(statistics.mean(values), 2),
            }
    return stats


def format_json(path, rows, columns, stats):
    report = {
        "file": path,
        "rows": len(rows),
        "columns": columns,
        "numeric": stats,
        "text_columns": [c for c in columns if c not in stats],
    }
    return "```json\n" + json.dumps(report, indent=2) + "\n```"


def format_table(columns, stats):
    lines = ["| Column | Min | Max | Mean |", "|--------|-----|-----|------|"]
    for name, s in stats.items():
        lines.append(f"| {name} | {s['min']} | {s['max']} | {s['mean']} |")
    text_cols = [c for c in columns if c not in stats]
    lines.append("")
    lines.append(
        "Text columns with no numeric stats: "
        + (", ".join(text_cols) if text_cols else "none")
        + "."
    )
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Error: usage: profile.py <file.csv>")
        return
    path = sys.argv[1]
    try:
        rows = load_rows(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return
    except Exception as e:
        print(f"Error: could not read CSV: {e}")
        return

    if not rows:
        print(f"Profile of `{path}`: 0 rows.")
        return

    columns = list(rows[0].keys())
    stats = numeric_stats(rows)

    print(f"Profile of `{path}`:")
    print()
    print(format_json(path, rows, columns, stats))
    print()
    if stats:
        print(format_table(columns, stats))
    else:
        print("No numeric columns.")


if __name__ == "__main__":
    main()
