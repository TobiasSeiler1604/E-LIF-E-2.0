# ✔️ E-life(e) – Habit Tracker

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# ✔️ TEMPLATE for documentation
## 📝 Analysis

**Problem**
💡 In a busy lifestyle, individuals often lack a simple, consolidated way to track and assess their daily wellness habits (e.g., sleep, stress, water, exercise). This lack of immediate feedback makes it difficult to maintain awareness, identify patterns, and make necessary adjustments to achieve their health and habit goals. 

**Scenario**
💡 The E-lif(e) Tracker is designed for quick, end-of-day use. The user runs the application from the console, is prompted with quick questions about their day’s habits, and, upon completion, automatically generates a clear status report with a personalized wellness score and actionable advice. This provides an immediate, clear overview without complex setup or extensive data entry. 1 User will log her/his daily data’s into the program. 

**User stories:**
1. As a User, I want to track my daily habits by answering simple, quick questions in order to stay strong and healthy. 
2. As a User, I want to quickly add information about my lifestyle (nutrition, sport, sleep) in order to get decisive and valuable information for improvement. 
3. As a User, I want to receive a daily status report that gives personalized advice based on my input in order to keep me motivated. 
4. As a User, I want the history of my daily reports to be saved so I can view my progress over time in order to track my improvement and development. 

**Use cases:**
1. Enter daily wellness data (sleep, stress, exercise, etc.) 
2. Validate each entry to prevent invalid input
3. Save all inputs to a file (e.g., ‘weekly_data.txt’). Saving inputs for 28 days 
4. Generate a weekly status report (‘report.txt’) with advice and summaries 

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

---
The application interacts with the user via the console. Users can:
- View all the habits 
- Select habit and answer the question 
- See the results of each habit - Receive a daily/weekly overview of the habits

---


### 2. Data Validation 

To ensure the application collects accurate and meaningful information, every user input is validated before it is stored or used for calculations. The program uses predefined categories, data types, and validation rules to prevent invalid values and keep the dataset consistent.

All validation is implemented directly in main.py, mainly through the helper functions ask_choice() and ask_number(). These functions repeatedly prompt the user until valid input is provided.

**Sleep quality validation:**
```python
Category: Sleep rating
Data type: String (input) → mapped to Integer (stored)
Validation rule: Must be one of: good, medium, bad
Storage: sleep is saved as a numeric score using SLEEP_MAP


	def ask_choice(prompt, mapping):
    while True:
        value = input(prompt).lower().strip()
        if value in mapping:
            return mapping[value]
        print("Invalid input.")

Example usage:

	day["sleep"] = ask_choice("Sleep (good/medium/bad): ", SLEEP_MAP)
```

**Stress level validation:**

```python
When the user enters their daily stress level, the program ensures that the input is a number between 1 and 5:
Category: Daily stress measurement (1–5)
Data type: Integer
Validation rule: Must be an integer between 1 and 5

	
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

Example usage:

	day["stress"] = ask_number("Stress (1-5): ", 1, 5)
```

- **Yes/No questions (friends, exercise, hobbies, medication):** 

```python
For binary inputs, the program checks if the user enters only yes or no:
Category: Social & health habits (friends, exercise, hobbies, meds)
Data type: String (input) → mapped to Integer (stored)
Validation rule: Must be yes or no
Storage: Stored as numeric values using YES_NO_MAP

day["exercise"] = ask_choice("Exercise? (yes/no): ", YES_NO_MAP)
day["friends"] = ask_choice("Hung out with friends? (yes/no): ", YES_NO_MAP)
```

- **Water intake validation:** 

```python
Water intake is checked to confirm that the input is numeric and within realistic limits:
Category: Daily water consumption (liters)
Data type: Float (input) → categorized to Integer (stored)
Validation rule: Must be a non-negative number
Storage rule: liters are categorized into 3 levels

	def classify_water():
    w = ask_number("Water (liters): ", 0, None, True)
    return 1 if w < 1 else 2 if w <= 1.5 else 3
```

- **Step count validation:**

```python
The number of steps is verified to be a positive integer:
Category: Physical activity measurement
Data type: Integer (input) → categorized to Integer (stored)
Validation rule: Must be a non-negative integer
Storage rule: categorized into 3 levels

	def classify_steps():
    s = ask_number("Steps: ", 0)
    return 1 if s < 4000 else 2 if s < 10000 else 3
```

**Date Validation (Optional Change):**

```python
After input collection, users can manually overwrite the automatically generated date. The entered date must match the format YYYY/MM/DD.

	new = input("Enter date (yyyy/mm/dd): ").strip()
	datetime.datetime.strptime(new, "%Y/%m/%d")
```

These validation checks ensure that:

- the program does not crash due to invalid input,
- stored data remains consistent across days,
- summaries and score calculations remain reliable.


### 3. File Processing 

The application uses JSON files for persistent storage and reporting.

- **Input file/ Storage File:** 

File name: girlypop_data.json
Purpose: Stores all logged days
Format: A list of dictionaries (one dictionary per day)

Each entry contains standardized numeric values for all tracked metrics plus the computed total score.

Example structure:

	```json
				[
  {
    "date": "2025/12/13",
    "sleep": 3,
    "stress": 2,
    "friends": 2,
    "water": 2,
    "exercise": 1,
    "mood": 3,
    "work_hours": 8.0,
    "hobbies": 2,
    "steps": 2,
    "meds": 2,
    "score": 22
  }
]
```
- The application reads this file to generate a weekly or monthly summary and give personalized advice.
- Loading and saving: the file (example implementation):

	```python
	def load_data():
    return json.load(open(DATA_FILE)) if os.path.exists(DATA_FILE) else []

	def save_data(data):
    json.dump(data, open(DATA_FILE, "w"), indent=4)


- **Output file(Monthly/Weekly Reports):** 
When the user selects “Generate monthly report”, the program creates two files:

1. JSON report file
Filename format: monthly_report_YYYY_MM.json
Contains: month/year, days logged, total score, average score, and averages per metric.

2. TXT report file
Filename format: monthly_report_YYYY_MM.txt
Human-readable summary including the same key statistics.

Writing output:

	```python
		json_name = f"monthly_report_{today.year}_{today.month:02d}.json"
		json.dump(report, open(json_name, "w"), indent=4)

		txt_name = f"monthly_report_{today.year}_{today.month:02d}.txt"
		with open(txt_name, "w") as f:
		```


## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- OpenAI
- No external libraries

### 📂 Repository Structure
	```text
	e_life_project/
├─ data_storage.py      # handles loading and saving data from/to json files
├─ input_validation.py  # handles user input and validates it
├─ main.py              # main entry point (this file)
├─ menu.py              # in order to select the menu before starting the questionary and report
├─ reports.py           # report generation module, generates weekly and monthy reports with analyses and advice
├─ weekly_data.txt      # weekly data entry in numbers
└─ wellness_score.py    # calculation module for the scoring system
```

### How to Run
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Check if files exist and handle paths.
- `datetime` → Add timestamps or weekly summaries.
- `json`: Used for data storage

### Project Modules
- `from menu import`: main_menu

All external dependencies used in this project come from Python’s standard library, so no additional installation is required. In addition, the project uses custom modules created within the codebase (e.g. for menu handling) to improve structure and readability. These components were chosen for their simplicity and effectiveness in managing data, files, and user interaction in a console application.

## Project Management

| Name       	   | Contribution (Before Project started)        |Contribution after Projectstart                          |
|------------------|----------------------------------------------|---------------------------------------------------------|
| da Costa Inês    | Menu reading (file input) and displaying menu|1.) Created input_validation.py                          |
|                  |                                              |2.) Read.me (exception project management)               |
|                  |                                              |3.) PPT -> Live demo                                     |
|                  |                                              |                                                         |
| Haefliger Sarah  | Order logic and data validation              |1.) created menu.py and data storage.py                  |
|                  |                                              |2.) putting all codes to main.py and testing             |
|                  |                                              |3.) Read.me -> Project Management & Limitations          |
|                  |                                              |4.) PPT -> Project management                            |
|                  |                                              |                                                         |
| Jegge Lara 	   | Invoice generation (file output) and slides  |1.) created reports.py and wellness_score.py             |
|                  |                                              |2.) PPT -> a.Rationale for the topic chosen              |
|                  |                                              |           b.Project for the topic chosen                |
----------------------------------------------------------------------------------------------------------------------------------------------------------

**Highlight: Data Validation & Storage Design**

One major highlight of our project was the structured validation and storage of user input.
Initially, user inputs were entered as strings (e.g. good, medium, bad). By introducing mapping dictionaries that convert these string inputs into numeric values, we were able to standardize the data and evaluate it numerically.

This approach enabled a clear and consistent scoring system, simplified calculations, and reduced repetitive conditional logic. As a result, the overall code became shorter, more readable, and easier to maintain.

**Problems**
1. Project Management & Time Management

One of the main challenges of the project was project management, particularly task distribution and time management. During the first phase of the project, progress was slower than expected, and for several weeks no concrete implementation or clear technical approach had been defined. This was partly due to uncertainty about how to translate the lecture content, which was taught step by step, into a complete and independent project.

As a result, a significant portion of the development work had to be completed closer to the submission deadline. This required increased coordination, parallel work, and fast decision-making within the team.

Through this experience, the team learned the importance of:

- defining a clear project structure early on,
- assigning responsibilities at an earlier stage,
- and aligning implementation steps more closely with lecture progress.

Despite these challenges, the team successfully reorganized tasks, focused on core functionality, and delivered a working and well-structured application.

2. Limitations

Due to the late start of the implementation phase and limited remaining time before submission, it was not possible to go into greater technical depth in all parts of the code. While the core functionality, validation, and data storage were implemented successfully, some areas could not be refined as thoroughly as initially intended.

- As a result, the project’s limitations mainly concern:
- limited time for deeper refactoring and optimization,
- fewer edge-case tests and extended error handling, reduced opportunity to explore more advanced features introduced later in the lectures.

These limitations are primarily related to time and project management constraints rather than conceptual or technical understanding. Given more time, the project could be extended with cleaner abstractions, additional tests, and more advanced logic.

2. 1 **Limitations in our current code**

**Core bugs & correctness**

1) Missing return value in classify_steps()
The classify_steps() function does not return a value, which causes the steps field to be stored as None. This affects the wellness score calculation as well as weekly and monthly averages.


    def classify_steps():
    s = ask_number("Steps: ", 0, 50000)
    return 1 if s < 5000 else 2 if s < 10000 else 3

**Code Structure & Maintainability**

2) Duplicate function definitions
The functions to_number() and process_day() are defined twice in the same file. This duplication increases maintenance effort and creates the risk of inconsistencies if only one version is modified.


**Data storage & file robustness**

3) No enforced 28-day data limit
Although comments indicate a 28-day history, the application currently stores all entries indefinitely. Older data is never trimmed, which can distort long-term reporting and increase file size.

Improvement idea:

data.append(processed)
data = data[-28:]
save_data(data)

4) Unsafe and non-robust file handling
JSON files are opened without context managers, and no error handling is implemented for corrupted or empty files. If a file becomes invalid, the program will crash.


with open(DATA_FILE, "r") as f:
    data = json.load(f)


5) Inconsistent use of data storage formats
Daily entries are written to both JSON and a TXT weekly log, but weekly reports are generated only from the JSON file. The TXT log is not used for reporting and lacks a clear functional role.

6) Lack of privacy and security measures
All data is stored in plain JSON and TXT files without encryption or access control, which raises privacy concerns.

**Reporting & time logic (weekly/monthly)**

7) Weekly report does not reflect a real calendar week
The weekly report is based on the last seven logged entries rather than the last seven calendar days. If users skip days, the report may span more than one week, and missing days are not detected.

week_data = data[-7:]

8) Monthly report is not truly monthly
The monthly report aggregates all stored data, even when entries span multiple months, reducing the accuracy of monthly insights.

averages = {field: sum((d.get(field) or 0) for d in data) / len(data)
     for field in FIELDS_NUMERIC}

**Scoring & interpretation**

9) Incomplete integration of collected metrics into scoring
Some validated inputs, such as work_hours, are collected and reported but do not contribute to the wellness score, which makes tracking feel incomplete.


"work_hours": ask_number("Work hours: ", 0, 16, True)


Show that it’s not included in score keys:

score = sum(to_number(day.get(key)) for key in ["sleep","friends","water","exercise", "mood","steps","hobbies","meds"])


10) Numeric averages are not intuitive for users
Yes/No values are stored as numeric values (1 or 2), leading to averages such as 1.6. While mathematically correct, these results are difficult to interpret.


YES_NO_MAP = {"no": 1, "yes": 2}


11) Overly simplified scoring categories
Some metrics, such as water intake and steps, are reduced to broad categories. While this simplifies scoring, it limits the ability to track gradual improvements.

Code references:
return 1 if w < 1 else 2 if w <= 1.5 else 3


Hard-coded limits may not suit all users

12) Advice is rule-based rather than trend-based
Feedback is generated from single-day thresholds and does not account for longer-term behavioral patterns.

if to_number(day.get("water")) == 1:
    advice.append("💧 Hydrate queen!")


**Input validation & user data consistency**

13) Minor edge case in numeric validation messages
Range error messages in ask_number() are not displayed correctly when the minimum value is 0 due to truthy checks.

Problem: 0 is treated like False.

14) No protection against duplicate date entries
Users can manually enter dates that already exist in the dataset, resulting in duplicate or conflicting records for the same day.

15) Hard-coded limits may not suit all users
Fixed upper limits for work hours, steps, and water intake may not reflect all lifestyles, such as athletes or night-shift workers.

16) Input Validation and Error Handling
We considered potential user input errors by validating all inputs and preventing the program from crashing. The program repeatedly prompts the user until valid input is provided, although the error messages remain simple and could be more specific.

**Dependencies & portability**

17) Dependency on an external menu module
The application depends on an external menu.py file. If this module is missing or altered, the program will not run correctly, reducing portability.




2. 3 **What We’d consider doing next (Future improvements)**

**0Core bugs & correctness**

1) Fix classify_steps() return value
We would ensure classify_steps() always returns a clear category (e.g., 1/2/3) so that steps are stored correctly and can be used reliably in scoring and reports. This would immediately improve correctness of daily scores and averages.

**Code Structure & Maintainability**

2) Remove duplicate functions (to_number(), process_day())
We would keep only one version of each function to avoid confusion and reduce maintenance risk. If time allows, we would move scoring logic into a separate file (e.g., scoring.py) so the main file stays shorter and easier to read.

**Data storage & file robustness**

3) Enforce a real 28-day history
We would actively limit stored data to the most recent 28 entries to match our documentation and keep reports focused and files small.

4) Improve file safety when loading/saving JSON
We would consistently use with open(...) when reading and writing files to ensure files are properly closed. In addition, we would add simple error handling so the program can recover if the JSON file is missing or corrupted instead of crashing.

5) Choose one “source of truth” for stored data
We would clarify the purpose of the TXT weekly log. Either:

keep JSON as the main storage and generate TXT outputs only as reports, or

remove the TXT log if it does not add value.
This would reduce duplicated storage and make the system easier to maintain.

6) Improve privacy awareness (basic level)
Since this is a beginner project, we would not implement complex security, but we would at least:

store all data in the data/ folder,

clearly mention in documentation that the file contains personal data,

optionally add a simple “warning message” at program start (“data is stored locally in plain text”).

**Reporting & time logic (weekly/monthly)**

7) Make the weekly report more accurate and clearer
We would either:

filter the report by real calendar dates (last 7 days), or

rename it in the report output to “last 7 entries” to avoid misleading the user.
We would also consider showing “days logged vs days missing” to make gaps visible.

8) Make the monthly report truly monthly
We would filter entries so that the monthly report only includes the current month and year. This would make averages and totals accurate for the month.

**Scoring & interpretation**

9) Make scoring consistent with collected metrics
We would decide whether work_hours should influence the score or be “tracking-only.” If it remains tracking-only, we would clearly label it in the report so users understand it is not part of the score.

10) Improve report interpretation for averages
We would translate numeric averages back into understandable text. Example:

1.0–1.49 → mostly “no”

1.5–2.0 → mostly “yes”
This would make weekly and monthly summaries easier to understand.

11) Keep scoring simple but explain it better
Since this is a beginner project, we would keep the simple 1–3 categories, but we would improve transparency by explaining what each category means (e.g., water level 1/2/3). This improves clarity without making the algorithm more complex.

12) Add small “trend awareness” without complexity
Instead of advanced analytics, we would implement a simple rule such as:
“If stress is high for several consecutive entries, show one extra message.”
This stays beginner-friendly but feels more personalized.

**Input validation & user data consistency**

13) Fix the small validation message edge case
We would adjust the check in ask_number() so the range message still appears correctly when min_val is 0. This improves clarity for users without changing the overall logic.

14) Prevent duplicate date entries
We would check whether an entered date already exists before saving. If it does, we would either:

ask the user if they want to overwrite, or

automatically update the existing entry.
This improves data consistency.

15) Make limits more flexible
We would keep reasonable default limits, but we would document them clearly and possibly allow adjustment in one place (constants at the top of the file). This keeps the project simple while making it more user-friendly.

16) Improve error messages and user guidance
We would make error messages slightly more specific by repeating expected input options (e.g., “Please enter yes or no”). This would reduce confusion for users while staying within beginner-level programming.

**Dependencies & portability**

17) Improve portability of the menu dependency
We would ensure the project always includes menu.py and document how to run the program. As a small improvement, we could add a basic fallback message if the menu module is missing (so the error is understandable).


## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
