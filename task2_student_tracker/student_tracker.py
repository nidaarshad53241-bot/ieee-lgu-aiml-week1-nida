"""
Student Grade & Attendance Tracker
IEEE LGU AI/ML Cohort One - Week 1 Assignment (Option 2)

Takes a student's name, roll number, subject marks and attendance,
then calculates their average, grade, attendance percentage and
exam eligibility, and prints a clean report card.
"""


def get_grade(average):
    """Return a letter grade based on the average marks."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def get_attendance_percentage(classes_held, classes_attended):
    """Return attendance as a percentage."""
    return (classes_attended / classes_held) * 100


def get_valid_float(prompt, min_value=0, max_value=100):
    """Ask for a float within a range, keep asking until valid."""
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_valid_int(prompt, min_value=0):
    """Ask for a whole number, keep asking until valid."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            print(f"Please enter a number of at least {min_value}.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def collect_subject_marks(num_subjects=3):
    """Ask the user for marks in a number of subjects. Returns a dictionary."""
    subjects = {}
    print(f"\nEnter marks for {num_subjects} subjects:")
    for i in range(num_subjects):
        subject = input(f"\nEnter subject {i + 1} name: ").strip()
        marks = get_valid_float(f"Enter marks for {subject} (0-100): ")
        subjects[subject] = marks
    return subjects


def collect_attendance():
    """Ask the user for total classes held and attended. Returns (held, attended)."""
    print("\n--- Attendance Information ---")
    while True:
        classes_held = get_valid_int("Enter total classes held: ", min_value=1)
        classes_attended = get_valid_int("Enter classes attended: ", min_value=0)

        if classes_attended > classes_held:
            print("Attended classes cannot be greater than total classes.")
            continue

        return classes_held, classes_attended


def print_report(name, roll_number, subjects, average, grade,
                  attendance, eligibility):
    """Print the final student report card."""
    print("\n====================================")
    print("          STUDENT REPORT")
    print("====================================")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")

    print("\nSubject Marks:")
    for subject, marks in subjects.items():
        print(f"  {subject}: {marks}")

    print(f"\nAverage: {average:.2f}%")
    print(f"Grade: {grade}")
    print(f"Attendance: {attendance:.2f}%")
    print(f"Exam Eligibility: {eligibility}")
    print("====================================")


def main():
    print("====================================")
    print("   STUDENT GRADE & ATTENDANCE")
    print("====================================")

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    subjects = collect_subject_marks(num_subjects=3)
    average = sum(subjects.values()) / len(subjects)
    grade = get_grade(average)

    classes_held, classes_attended = collect_attendance()
    attendance = get_attendance_percentage(classes_held, classes_attended)

    eligibility = "Eligible for exams" if attendance >= 75 else "Not eligible for exams"

    print_report(name, roll_number, subjects, average, grade,
                 attendance, eligibility)


if __name__ == "__main__":
    main()
