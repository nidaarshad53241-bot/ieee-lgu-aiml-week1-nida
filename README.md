# IEEE LGU AI/ML Cohort One — Week 1 Assignment

**Name:** Nida Arshad
**Cohort:** IEEE LGU AI/ML Cohort One
**Projects Chosen:** Option 1 (Number Guessing Game) & Option 2 (Student Grade & Attendance Tracker)

---

## Project 1: Number Guessing Game

**Folder:** `task1_number_guessing/number_guessing.py`

### Description
A console-based game where the computer randomly picks a secret number and the
player tries to guess it within a limited number of attempts. The player can choose
a difficulty level (Easy, Normal, Hard), gets "Too High"/"Too Low" hints after every
guess, sees remaining attempts, and can play multiple rounds. Invalid input (letters,
out-of-range numbers) is handled gracefully without crashing the program.

### How to Run
```bash
python task1_number_guessing/number_guessing.py
```

---

## Project 2: Student Grade & Attendance Tracker

**Folder:** `task2_student_tracker/student_tracker.py`

### Description
A console program that collects a student's name, roll number, and marks for 3
subjects, then calculates their average percentage and letter grade (A/B/C/F). It
also takes attendance data (classes held vs. attended) to calculate an attendance
percentage and checks whether the student meets the 75% minimum attendance rule
for exam eligibility. Finally, it prints a clean, formatted report card. All numeric
inputs are validated so the program doesn't crash on invalid entries.

### How to Run
```bash
python task2_student_tracker/student_tracker.py
```

---

## Screenshots

- `task1_output.png` — Number Guessing Game running successfully
- `task2_output.png` — Student Tracker running successfully

---

## Concepts Used
- Variables & data types (int, float, str, bool)
- Conditionals (`if` / `elif` / `else`)
- Loops (`for`, `while`)
- Functions for clean, reusable code
- Dictionaries & lists for storing data
- Input validation with `try`/`except`
