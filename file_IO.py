import csv
import json
from pathlib import Path
import os

# -----------------------------------------------------------
# 1) Simple text write / read (original example, with notes)
# -----------------------------------------------------------
BASE = Path(".")  # current folder (use pathlib for clarity)


def write_lines(path: Path, lines):
    """Write a list of lines to a text file (overwrites)."""
    path = Path(path)
    with path.open("w", encoding="utf-8") as f:
        for L in lines:
            f.write(L + "\n")  # add newline explicitly
    print(f"Wrote {len(lines)} lines to {path}")


def read_whole_file(path: Path) -> str:
    """Read entire file contents into memory (small files only)."""
    with Path(path).open("r", encoding="utf-8") as f:
        return f.read()


# demo
lines = ["First line", "Second line", "Third"]
write_lines("example.txt", lines)
contents = read_whole_file("example.txt")
print("File contents:\n", contents)


# -----------------------------------------------------------
# 2) Appending vs writing and safe exists check
# -----------------------------------------------------------
def append_line(path: Path, line: str):
    with Path(path).open("a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Appended line to {path}")


if not BASE.joinpath("example.txt").exists():
    write_lines("example.txt", ["Created because file was missing"])
append_line("example.txt", "Appended line")


# -----------------------------------------------------------
# 3) Read file line-by-line (memory friendly)
# -----------------------------------------------------------
def read_lines_iter(path: Path):
    """Yield lines one by one (useful for large files)."""
    with Path(path).open("r", encoding="utf-8") as f:
        for ln in f:
            yield ln.rstrip("\n")


print("\nReading example.txt line-by-line:")
for ln in read_lines_iter("example.txt"):
    print(">", ln)

# -----------------------------------------------------------
# 4) CSV write/read (rows as tuples) - original style
# -----------------------------------------------------------
rows = [
    ("name", "score"),
    ("Alice", 90),
    ("Bob", 75),
]
with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("\nCSV (row) readout:")
with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print("Row:", row)


# -----------------------------------------------------------
# 5) CSV with DictReader/DictWriter (recommended for headers)
# -----------------------------------------------------------
def write_scores_dict(path: Path, records):
    """records: list of dicts like {'name': 'Alice', 'score': 90}"""
    path = Path(path)
    if not records:
        return
    keys = list(records[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in records:
            writer.writerow(r)
    print(f"Wrote {len(records)} records to {path}")


def read_scores_dict(path: Path):
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


# Demo: write/read using dicts
records = [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 75}]
write_scores_dict("scores_dict.csv", records)
data = read_scores_dict("scores_dict.csv")
print("\nCSV DictReader output:", data)

# Convert score strings to ints
for d in data:
    try:
        d["score"] = int(d["score"])
    except (KeyError, ValueError):
        d["score"] = 0

# sort and top-3
top = sorted(data, key=lambda x: x["score"], reverse=True)[:3]
print("Top players:", top)


# -----------------------------------------------------------
# 6) JSON read/write (very handy to persist Python objects)
# -----------------------------------------------------------
def write_json(path: Path, obj):
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"Wrote JSON to {path}")


def read_json(path: Path):
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


prefs = {"theme": "dark", "recent_files": ["example.txt", "scores.csv"]}
write_json("prefs.json", prefs)
print("Read JSON:", read_json("prefs.json"))


# -----------------------------------------------------------
# 7) Safe handling: missing files, exceptions
# -----------------------------------------------------------
def safe_read(path: Path):
    try:
        return read_whole_file(path)
    except FileNotFoundError:
        print(f"File {path} not found.")
        return ""


print("\nSafe read (non-existent file):")
_ = safe_read("no_such_file.txt")


# -----------------------------------------------------------
# 8) Useful real-world tiny tasks (helpers + small challenges)
# -----------------------------------------------------------
def csv_to_json(csv_path: Path, json_path: Path):
    try:
        rows = read_scores_dict(csv_path)
        # try to coerce numeric strings to ints when possible
        for r in rows:
            for k, v in r.items():
                if isinstance(v, str) and v.isdigit():
                    r[k] = int(v)
        write_json(json_path, rows)
    except FileNotFoundError:
        print(f"CSV {csv_path} not found; skipping conversion.")


def top_k_from_csv(csv_path: Path, k=3):
    rows = read_scores_dict(csv_path)
    for r in rows:
        try:
            r["score"] = int(r.get("score", 0))
        except ValueError:
            r["score"] = 0
    return sorted(rows, key=lambda x: x["score"], reverse=True)[:k]


# Interactive small utilities
if input("\nConvert scores.csv to JSON? (y/N): ").strip().lower() == "y":
    csv_to_json("scores.csv", "scores.json")
    print("Converted scores.csv -> scores.json (if csv existed)")

if input("\nShow top-3 from scores_dict.csv? (y/N): ").strip().lower() == "y":
    print("Top 3:", top_k_from_csv("scores_dict.csv", 3))


# -----------------------------------------------------------
# 9) File system utilities: list files, find largest file
# -----------------------------------------------------------
def find_largest_file(folder: Path):
    folder = Path(folder)
    if not folder.exists() or not folder.is_dir():
        return None
    files = [p for p in folder.iterdir() if p.is_file()]
    if not files:
        return None
    return max(files, key=lambda p: p.stat().st_size)


largest = find_largest_file(".")
if largest:
    print(
        f"\nLargest file in current directory: {largest} ({largest.stat().st_size} bytes)"
    )
