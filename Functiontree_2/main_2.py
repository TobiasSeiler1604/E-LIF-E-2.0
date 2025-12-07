import datetime
import json
import os
from Menu import decision

DATA_FILE = "girlypop_data.json"

# Placeholder-Funktionen (werden später implementiert)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def collect_daily_inputs():
    # Placeholder
    pass


def process_day(day):
    # Placeholder
    pass


def save_monthly_report(data):
    # Placeholder
    pass


def run():
    month_data = load_data()
    print(f"Loaded {len(month_data)} previous days.")

    while True:
        choice = decision()

        if choice == 1:
            day = collect_daily_inputs()

            # Allow changing the date
            change_date = input(
                f"Change date from {day['date']}? (yes/no): ").lower().strip()
            if change_date == "yes":
                while True:
                    date_input = input("Enter date (yyyy/mm/dd): ").strip()
                    try:
                        datetime.datetime.strptime(date_input, "%Y/%m/%d")
                        day["date"] = date_input
                        break
                    except ValueError:
                        print("Invalid format. Please use yyyy/mm/dd")

            processed, advice = process_day(day)
            month_data.append(processed)
            save_data(month_data)
            print(
                f"\n✅ Data saved! {processed['date']} → Score {processed['score']}")
            if advice:
                print("Advice:")
                for a in advice:
                    print("-", a)

        elif choice == 2:
            print("\n📊 Generating monthly report...")
            save_monthly_report(month_data)
            print("")  # Add space before menu repeats

        elif choice == 3:
            print("Goodbye queen ✨")
            break


run()
