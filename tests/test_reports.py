"""
test_reports.py - Test reports module
Run: python test_reports.py
"""

from reports import generate_weekly_report, generate_monthly_advice

print("\n🧪 TESTING REPORTS MODULE\n")

# Test 1: Weekly report
print("Test 1: Generating weekly report...")
test_data = [
    {"date": "2025/12/01", "sleep": 2, "stress": 2, "friends": 2,
     "water": 3, "exercise": 2, "mood": 3, "work_hours": 8,
     "hobbies": 2, "steps": 2, "meds": 2, "score": 20},
    {"date": "2025/12/02", "sleep": 3, "stress": 1, "friends": 3,
     "water": 3, "exercise": 3, "mood": 3, "work_hours": 8,
     "hobbies": 2, "steps": 3, "meds": 2, "score": 24},
    {"date": "2025/12/03", "sleep": 1, "stress": 4, "friends": 1,
     "water": 1, "exercise": 1, "mood": 1, "work_hours": 10,
     "hobbies": 1, "steps": 1, "meds": 1, "score": 8},
]
report = generate_weekly_report(test_data)
print("✅ Weekly report generated:")
print(report[:200] + "...\n")

# Test 2: Monthly advice
print("Test 2: Generating monthly advice...")
averages = {
    "sleep": 2.3, "stress": 2.3, "friends": 2.0,
    "water": 2.3, "exercise": 2.0, "mood": 2.3,
    "work_hours": 8.7, "hobbies": 1.7, "steps": 2.0, "meds": 1.7
}
advice = generate_monthly_advice(averages)
print(f"✅ Generated {len(advice)} advice items:")
for adv in advice[:5]:
    print(f"   - {adv}")

print("\n✅ reports.py tests PASSED!\n")
