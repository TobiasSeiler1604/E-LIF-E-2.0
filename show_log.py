import json
import pathlib
import datetime

def show_log(data):
    """Display log entries in terminal."""
    if not data:
        print("\n❌ No entries logged this month 😭")
        return
    
    print("\n📋 LOG ENTRIES:")
    for date_key, entry in data.items():
        score = entry.get("score", "N/A")
        print(f"  {date_key} → Score: {score}")
