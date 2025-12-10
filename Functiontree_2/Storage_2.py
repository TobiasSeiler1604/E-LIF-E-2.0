import datetime
import json
import pathlib
from menu import main_menu

# Input-to-number mappings
SLEEP_MAP = {"bad": 1, "medium": 2, "good": 3}
MOOD_MAP = {"angry": 1, "anxious": 1, "irritable": 1,
            "hyper": 2, "calm": 3, "relaxed": 3, "happy": 3}
YES_NO_MAP = {"no": 1, "yes": 2}

FIELDS_NUMERIC = ["sleep", "stress", "friends", "water",
                  "exercise", "mood", "work_hours", "hobbies", "steps", "meds"]


def load_data():
    """Load monthly data from JSON file."""
    now = datetime.datetime.now()
    filename = pathlib.Path(f"./data/{now.year}-{now.month}.json")

    if not filename.exists():
        return {}

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    """Save data to monthly JSON file."""
    now = datetime.datetime.now()
    filename = pathlib.Path(f"./data/{now.year}-{now.month}.json")

    if not filename.parent.exists():
        filename.parent.mkdir(parents=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def collect_daily_inputs():
    day = {}
    now = datetime.datetime.now()
    day_key = f"{now.year}-{now.month}-{now.day}"

    while True:
        val = input("Sleep (good/medium/bad): ").lower().strip()
        if val in SLEEP_MAP:
            day["sleep"] = SLEEP_MAP[val]
            break
        print("Invalid input.")

    while True:
        try:
            val = int(input("Stress (1-5): "))
            if 1 <= val <= 5:
                day["stress"] = val
                break
        except:
            pass
        print("Invalid input.")

    while True:
        val = input("Hung out with friends? (yes/no): ").lower().strip()
        if val in YES_NO_MAP:
            day["friends"] = YES_NO_MAP[val]
            break
        print("Invalid input.")

    while True:
        try:
            val = float(input("Water (liters): "))
            if val >= 0:
                if val < 1:
                    day["water"] = 1
                elif val <= 1.5:
                    day["water"] = 2
                else:
                    day["water"] = 3
                break
        except:
            pass
        print("Invalid input.")

    while True:
        val = input("Exercise? (yes/no): ").lower().strip()
        if val in YES_NO_MAP:
            day["exercise"] = YES_NO_MAP[val]
            break
        print("Invalid input.")

    valid = list(MOOD_MAP.keys())
    while True:
        val = input(f"Mood {valid}: ").lower().strip()
        if val in MOOD_MAP:
            day["mood"] = MOOD_MAP[val]
            break
        print("Invalid input.")

    while True:
        try:
            val = float(input("Work hours: "))
            if val >= 0:
                day["work_hours"] = val
                break
        except:
            pass
        print("Invalid input.")

    while True:
        val = input("Hobbies today? (yes/no): ").lower().strip()
        if val in YES_NO_MAP:
            day["hobbies"] = YES_NO_MAP[val]
            break
        print("Invalid input.")

    while True:
        try:
            val = int(input("Steps: "))
            if val >= 0:
                if val < 4000:
                    day["steps"] = 1
                elif val < 10000:
                    day["steps"] = 2
                else:
                    day["steps"] = 3
                break
        except:
            pass
        print("Invalid input.")

    while True:
        val = input("Meds taken? (yes/no): ").lower().strip()
        if val in YES_NO_MAP:
            day["meds"] = YES_NO_MAP[val]
            break
        print("Invalid input.")

    return day_key, day


def process_day(day):
    score = 0
    advice = []

    score += day["sleep"]
    if day["stress"] <= 2:
        score += 3
    elif day["stress"] == 3:
        score += 1
    else:
        advice.append("Lower your stress bestie!")

    score += day["friends"]
    if day["friends"] == 1:
        advice.append("Touch grass with friends!")

    score += day["water"]
    if day["water"] == 1:
        advice.append("Hydrate queen!")

    score += day["exercise"]
    if day["exercise"] == 1:
        advice.append("Move your body!")

    score += day["mood"]
    if day["mood"] == 1:
        advice.append("Your mood needs attention!")

    score += day["steps"]
    if day["steps"] == 1:
        advice.append("Walk more!")

    score += day["hobbies"]
    if day["hobbies"] == 1:
        advice.append("Do something fun!")

    score += day["meds"]
    if day["meds"] == 1:
        advice.append("Don't forget your meds!")

    day["score"] = score
    return day, advice


def generate_monthly_summary(data):
    if not data:
        return "No days logged this month 😭"

    # Filter out entries without score
    valid_entries = [d for d in data.values() if "score" in d]

    if not valid_entries:
        return "No days logged this month 😭"

    report = f"\n💗 MONTHLY SUMMARY 💗\nDays logged: {len(valid_entries)}\n"

    total_score = sum(d["score"] for d in valid_entries)
    avg_score = total_score / len(valid_entries)
    report += f"Average total score: {avg_score:.1f}\n"

    for field in FIELDS_NUMERIC:
        if field in valid_entries[0]:
            avg = sum(d[field] for d in valid_entries) / len(valid_entries)
            report += f"- Average {field}: {avg:.1f}\n"

    return report


def save_monthly_report(data):
    """Generate and display monthly report in terminal."""
    if not data:
        print("\n❌ No days logged this month 😭")
        return

    now = datetime.datetime.now()

    print(f"\n✅ Monthly report for {now.month}/{now.year}")
    print(generate_monthly_summary(data))


def run():
    month_data = load_data()
    print(f"Loaded {len(month_data)} previous days.")

    while True:
        choice = main_menu()

        if choice == 1:
            day_key, day = collect_daily_inputs()

            # Allow changing the date
            change_date = input(
                f"Change date from {day_key}? (yes/no): ").lower().strip()
            if change_date == "yes":
                while True:
                    date_input = input("Enter date (yyyy-mm-dd): ").strip()
                    try:
                        datetime.datetime.strptime(date_input, "%Y-%m-%d")
                        day_key = date_input
                        break
                    except ValueError:
                        print("Invalid format. Please use yyyy-mm-dd")

            processed, advice = process_day(day)
            month_data[day_key] = processed
            save_data(month_data)
            print(
                f"\n✅ Data saved! {day_key} → Score {processed['score']}")
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
