# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
def show_menu():
    """Displays the main menu options."""
    print("============================")
    print("   STUDENT RECORD SYSTEM")
    print("============================")
    print("1. Add student record")
    print("2. Display all records")
    print("3. Calculate average score")
    print("4. Quit")


def add_student(students):
    """Prompts for student details and adds a new record dictionary to the list."""
    name = input("Student name: ").strip()
    student_id = input("Student ID: ").strip()

    scores_count_input = input("How many scores? ").strip()
    if not scores_count_input.isdigit() or int(scores_count_input) <= 0:
        print("Error: Invalid number of scores.\n")
        return

    scores_count = int(scores_count_input)
    scores = []

    for i in range(1, scores_count + 1):
        score_input = input(f"Enter score {i}: ").strip()
        try:
            score = float(score_input)
            scores.append(score)
        except ValueError:
            print(f"Error: Invalid score '{score_input}'. Record creation canceled.\n")
            return

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.\n')


def display_records(students):
    """Displays all student records formatted in a neat table."""
    if not students:
        print("No student records available.\n")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<8}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(
            str(int(s)) if s.is_integer() else f"{s:.2f}" for s in student["scores"]
        )
        avg = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0
        print(f"{student['name']:<15}{str(student['id']):<12}{scores_str:<15}{avg:.2f}")

    print("-" * 50 + "\n")


def calculate_average(students):
    """Finds a student by ID and prints their average score."""
    student_id = input("Enter student ID: ").strip()

    for student in students:
        if str(student["id"]) == student_id:
            if student["scores"]:
                avg = sum(student["scores"]) / len(student["scores"])
                print(f"{student['name']}'s average score: {avg:.2f}\n")
            else:
                print(f"{student['name']} has no scores recorded.\n")
            return

    print(f"Error: Student with ID {student_id} not found.\n")


def main():
    """Main program loop."""
    students = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_records(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()
# =============================================================================

