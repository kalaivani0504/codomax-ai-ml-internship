"""
Student Grade Calculator
Codomax AI & ML Internship - Module 2
Beginner-friendly Python mini project
"""

def get_mark(subject):
    """Ask for a valid mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Invalid mark. Enter a number from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_grade(percentage):
    """Return a grade based on the percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    subjects = ["English", "Mathematics", "Computer Science", "Science", "Tamil"]
    marks = {}

    for subject in subjects:
        marks[subject] = get_mark(subject)

    total = sum(marks.values())
    maximum = len(subjects) * 100
    percentage = total / maximum * 100
    grade = calculate_grade(percentage)

    print("\n" + "=" * 40)
    print("RESULT")
    print("=" * 40)
    print(f"Student Name : {name}")
    print("-" * 40)

    for subject, mark in marks.items():
        print(f"{subject:<20}: {mark:g}")

    print("-" * 40)
    print(f"Total Marks  : {total:g} / {maximum}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")

    if percentage >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("=" * 40)


if __name__ == "__main__":
    main()
