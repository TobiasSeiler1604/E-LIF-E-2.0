import json
import pathlib
import datetime

def load_log():
    """Load existing log from file."""
    now = datetime.datetime.now()
    filename = pathlib.Path(f"./data/{now.year}-{now.month}.json")
    
    if not filename.exists():
        return {}
    
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
