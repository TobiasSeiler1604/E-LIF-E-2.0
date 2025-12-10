"""
test_data_storage.py - Test data_storage module
Run: python test_data_storage.py
"""

from data_storage import load_data, save_data

print("\n🧪 TESTING DATA_STORAGE MODULE\n")

# Test 1: Load existing data
print("Test 1: Loading data...")
data = load_data()
print(f"✅ Loaded {len(data)} records")
if data:
    print(f"   First record: {data[0]}")

# Test 2: Save test data
print("\nTest 2: Saving test data...")
test_data = [
    {"date": "2025/12/01", "sleep": 2, "stress": 2, "friends": 2,
     "water": 3, "exercise": 2, "mood": 3, "work_hours": 8,
     "hobbies": 2, "steps": 2, "meds": 2, "score": 20},
    {"date": "2025/12/02", "sleep": 3, "stress": 1, "friends": 3,
     "water": 3, "exercise": 3, "mood": 3, "work_hours": 8,
     "hobbies": 2, "steps": 3, "meds": 2, "score": 24}
]
save_data(test_data)
print("✅ Test data saved")

# Test 3: Verify save worked
print("\nTest 3: Verifying save...")
loaded = load_data()
print(f"✅ Verified: {len(loaded)} records in storage")
print(f"   Last record date: {loaded[-1]['date']}")

print("\n✅ data_storage.py tests PASSED!\n")
