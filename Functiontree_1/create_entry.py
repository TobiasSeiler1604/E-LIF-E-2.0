import datetime

# Input-to-number mappings
SLEEP_MAP = {"bad": 1, "medium": 2, "good": 3}
MOOD_MAP = {"angry": 1, "anxious": 1, "irritable": 1,
            "hyper": 2, "calm": 3, "relaxed": 3, "happy": 3}
YES_NO_MAP = {"no": 1, "yes": 2}


def create_entry():
    """Collect daily input from user."""
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
