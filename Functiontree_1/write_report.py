import json
import pathlib
import datetime


def write_report(data):
    """Write entry to log file."""
    now = datetime.datetime.now()
    filename = pathlib.Path(f"./data/{now.year}-{now.month}.json")

    if not filename.parent.exists():
        filename.parent.mkdir(parents=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Data saved to {filename}")
