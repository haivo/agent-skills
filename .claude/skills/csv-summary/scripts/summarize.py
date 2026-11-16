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


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: summarize.py <file.csv>"}))
        return
    path = sys.argv[1]
    try:
        with open(path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        print(json.dumps({"error": f"file not found: {path}"}))
        return
    except Exception as e:
        print(json.dumps({"error": f"could not read CSV: {e}"}))
        return

    columns = list(rows[0].keys()) if rows else []
    report = {
        "file": path,
        "rows": len(rows),
        "columns": columns,
        "numeric": numeric_stats(rows) if rows else {},
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
