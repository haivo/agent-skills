import csv
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


def format_table(stats):
    lines = ["| Column | Min | Max | Mean |", "|--------|-----|-----|------|"]
    for name, s in stats.items():
        lines.append(f"| {name} | {s['min']} | {s['max']} | {s['mean']} |")
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Error: usage: summarize.py <file.csv>")
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
        print(f"`{path}` has 0 rows.")
        return

    columns = list(rows[0].keys())
    stats = numeric_stats(rows)

    print(f"{len(rows)} rows, {len(columns)} columns: {', '.join(columns)}.")
    print()
    if stats:
        print(format_table(stats))
    else:
        print("No numeric columns.")


if __name__ == "__main__":
    main()
