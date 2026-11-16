import csv, json, sys, statistics

def main():
    if len(sys.argv) != 2:
        print("Error: usage: summarize.py <file.csv>")
        return
    path = sys.argv[1]
    try:
        with open(path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return
    except Exception as e:
        print(f"Error: could not read CSV: {e}")
        return

    if not rows:
        print(json.dumps({"rows": 0, "columns": [], "numeric": {}}))
        return

    numeric = {}
    for col in rows[0].keys():
        try:
            values = [float(r[col]) for r in rows if r[col] != ""]
        except ValueError:
            continue
        if values:
            numeric[col] = {
                "min": min(values),
                "max": max(values),
                "mean": round(statistics.mean(values), 2),
            }

    print(json.dumps({"rows": len(rows), "columns": list(rows[0].keys()), "numeric": numeric}, indent=2))

if __name__ == "__main__":
    main()
