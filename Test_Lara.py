import datetime
import json
import os
from Menu import decision

DATA_FILE = "girlypop_data.json"

# ------------------------------
# Mappings
# ------------------------------
SLEEP_MAP = {"bad": 1, "medium": 2, "good": 3}
MOOD_MAP = {
    "angry": 1, "anxious": 1, "irritable": 1,
    "hyper": 2,
    "calm": 3, "relaxed": 3, "happy": 3
}
YES_NO_MAP = {"no": 1, "yes": 2}

FIELDS_NUMERIC = ["sleep", "stress", "friends", "water",
                  "exercise", "mood", "work_hours", "hobbies", "steps", "meds"]

# ------------------------------
# Helper: JSON I/O
# ------------------------------


def load_data():
    return json.load(open(DATA_FILE)) if os.path.exists(DATA_FILE) else []


def save_data(data):
    json.dump(data, open(DATA_FILE, "w"), indent=4)

# ------------------------------
# Helper: Generic input functions
# ------------------------------


def ask_choice(prompt, mapping):
    while True:
        value = input(prompt).lower().strip()
        if value in mapping:
            return mapping[value]
        print("Invalid input.")


def ask_number(prompt, min_val=None, max_val=None, is_float=False):
    while True:
        try:
            value = float(input(prompt)) if is_float else int(input(prompt))
            if (min_val is None or value >= min_val) and \
               (max_val is None or value <= max_val):
                return value
        except:
            pass
        print("Invalid input.")

# ------------------------------
# Collect all inputs
# ------------------------------


def collect_daily_inputs():
    today = datetime.datetime.now().strftime("%Y/%m/%d")

    day = {
        "date": today,
        "sleep": ask_choice("Sleep (good/medium/bad): ", SLEEP_MAP),
        "stress": ask_number("Stress (1-5): ", 1, 5),
        "friends": ask_choice("Hung out with friends? (yes/no): ", YES_NO_MAP),
        "water": classify_water(),
        "exercise": ask_choice("Exercise? (yes/no): ", YES_NO_MAP),
        "mood": ask_choice(f"Mood {list(MOOD_MAP.keys())}: ", MOOD_MAP),
        "work_hours": ask_number("Work hours: ", 0, None, True),
        "hobbies": ask_choice("Hobbies today? (yes/no): ", YES_NO_MAP),
        "steps": classify_steps(),
        "meds": ask_choice("Meds taken? (yes/no): ", YES_NO_MAP)
    }
    return day


def classify_water():
    w = ask_number("Water (liters): ", 0, None, True)
    return 1 if w < 1 else 2 if w <= 1.5 else 3


def classify_steps():
    s = ask_number("Steps: ", 0)
    return 1 if s < 4000 else 2 if s < 10000 else 3

# ------------------------------
# PROCESS DAY
# ------------------------------


def process_day(day):
    score = sum([
        day["sleep"], day["friends"], day["water"], day["exercise"],
        day["mood"], day["steps"], day["hobbies"], day["meds"]
    ])

    advice = []

    if day["stress"] <= 2:
        score += 3
    elif day["stress"] == 3:
        score += 1
    else:
        advice.append("Lower your stress bestie!")

    if day["friends"] == 1:
        advice.append("Touch grass with friends!")
    if day["water"] == 1:
        advice.append("Hydrate queen!")
    if day["exercise"] == 1:
        advice.append("Move your body!")
    if day["mood"] == 1:
        advice.append("Your mood needs attention!")
    if day["steps"] == 1:
        advice.append("Walk more!")
    if day["hobbies"] == 1:
        advice.append("Do something fun!")
    if day["meds"] == 1:
        advice.append("Don't forget your meds!")

    day["score"] = score
    return day, advice

# ------------------------------
# MONTHLY REPORT
# ------------------------------


def save_monthly_report(data):
    if not data:
        print("❌ No days logged this month 😭")
        return

    today = datetime.datetime.now()

    averages = {
        field: sum(d[field] for d in data) / len(data)
        for field in FIELDS_NUMERIC
    }

    report = {
        "month": today.month,
        "year": today.year,
        "days_logged": len(data),
        "total_score": sum(d["score"] for d in data),
        "average_score": sum(d["score"] for d in data) / len(data),
        "averages": averages
    }

    # Save JSON
    json_name = f"monthly_report_{today.year}_{today.month:02d}.json"
    json.dump(report, open(json_name, "w"), indent=4)

    # Save TXT
    txt_name = f"monthly_report_{today.year}_{today.month:02d}.txt"
    with open(txt_name, "w") as f:
        f.write("💗 MONTHLY GIRLYPOP REPORT 💗\n")
        f.write(f"Month: {today.month}/{today.year}\n")
        f.write(f"Days logged: {report['days_logged']}\n")
        f.write(f"Total score: {report['total_score']}\n")
        f.write(f"Average score: {report['average_score']:.1f}\n\n")
        f.write("AVERAGES BY METRIC:\n")
        for k, v in averages.items():
            f.write(f" - {k}: {v:.1f}\n")

    print(f"\n✅ Reports saved!\n- JSON: {json_name}\n- TXT: {txt_name}")

# ------------------------------
# MAIN
# ------------------------------


def run():
    data = load_data()
    print(f"Loaded {len(data)} previous days.")

    while True:
        choice = decision()

        if choice == 1:
            day = collect_daily_inputs()

            if input("Change date? (yes/no): ").lower().strip() == "yes":
                while True:
                    new = input("Enter date (yyyy/mm/dd): ").strip()
                    try:
                        datetime.datetime.strptime(new, "%Y/%m/%d")
                        day["date"] = new
                        break
                    except ValueError:
                        print("Invalid format.")

            processed, advice = process_day(day)
            data.append(processed)
            save_data(data)

            print(
                f"\n✅ Saved {processed['date']} → Score {processed['score']}")
            if advice:
                print("Advice:")
                for a in advice:
                    print("-", a)

        elif choice == 2:
            save_monthly_report(data)

        elif choice == 3:
            print("Goodbye queen ✨")
            break


run()
