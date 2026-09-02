print("=== Student Records & Ranking System ===")


# ============================================================
# Student Data
# ============================================================

students = [
    {
        "id": 1,
        "name": "Anurag Bardhan",
        "marks": {
            "Python": 91,
            "Math": 84,
            "Database": 88
        }
    },
    {
        "id": 2,
        "name": "Rahul Sharma",
        "marks": {
            "Python": 78,
            "Math": 92,
            "Database": 81
        }
    },
    {
        "id": 3,
        "name": "Priya Singh",
        "marks": {
            "Python": 95,
            "Math": 89,
            "Database": 94
        }
    },
    {
        "id": 4,
        "name": "Rohan Das",
        "marks": {
            "Python": 67,
            "Math": 74,
            "Database": 70
        }
    },
    {
        "id": 5,
        "name": "Sneha Roy",
        "marks": {
            "Python": 86,
            "Math": 79,
            "Database": 84
        }
    }
]


next_student_id = 6

subjects = [
    "Python",
    "Math",
    "Database"
]


# ============================================================
# Main Menu
# ============================================================

while True:

    print("\n=== Menu ===")
    print("1. View all students")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Search students")
    print("6. Filter by grade")
    print("7. Rank students")
    print("8. Subject analysis")
    print("9. Class statistics")
    print("10. Detailed report")
    print("11. Exit")

    choice = input("Choose an option: ").strip()


    # ========================================================
    # VIEW ALL STUDENTS
    # ========================================================

    if choice == "1":

        print("\n=== All Students ===")

        if not students:
            print("No students available.")
            continue


        for student in students:

            total = sum(
                student["marks"].values()
            )

            average = (
                total
                / len(subjects)
            )


            if average >= 90:
                grade = "A"

            elif average >= 80:
                grade = "B"

            elif average >= 70:
                grade = "C"

            elif average >= 60:
                grade = "D"

            else:
                grade = "F"


            print(
                f"\n[{student['id']}] "
                f"{student['name']}"
            )

            print(
                f"  Python: "
                f"{student['marks']['Python']}"
            )

            print(
                f"  Math: "
                f"{student['marks']['Math']}"
            )

            print(
                f"  Database: "
                f"{student['marks']['Database']}"
            )

            print(
                f"  Total: "
                f"{total:.2f}"
            )

            print(
                f"  Average: "
                f"{average:.2f}"
            )

            print(
                f"  Grade: "
                f"{grade}"
            )


    # ========================================================
    # ADD STUDENT
    # ========================================================

    elif choice == "2":

        print("\n=== Add Student ===")

        name = input("Student name: ").strip()


        if not name:
            print("Name cannot be empty.")
            continue


        # Check duplicate student name

        duplicate_name = False

        for student in students:

            if student["name"].lower() == name.lower():

                duplicate_name = True
                break


        if duplicate_name:
            print("A student with this name already exists.")
            continue


        marks = {}


        for subject in subjects:

            while True:

                try:

                    score = float(
                        input(
                            f"{subject} marks: "
                        ).strip()
                    )

                    if score < 0 or score > 100:

                        print(
                            "Marks must be between "
                            "0 and 100."
                        )

                        continue


                    marks[subject] = score

                    break


                except ValueError:

                    print(
                        "Please enter a valid number."
                    )


        students.append(
            {
                "id": next_student_id,
                "name": name.title(),
                "marks": marks
            }
        )


        print(
            f"Student added successfully "
            f"with ID {next_student_id}."
        )


        next_student_id += 1


    # ========================================================
    # UPDATE STUDENT
    # ========================================================

    elif choice == "3":

        print("\n=== Update Student ===")


        try:

            student_id = int(
                input("Enter student ID: ").strip()
            )

        except ValueError:

            print("Please enter a valid ID.")
            continue


        selected_student = None


        for student in students:

            if student["id"] == student_id:

                selected_student = student
                break


        if selected_student is None:

            print("Student not found.")
            continue


        print(
            f"\nUpdating: "
            f"{selected_student['name']}"
        )


        new_name = input(
            f"New name "
            f"(press Enter to keep "
            f"'{selected_student['name']}'): "
        ).strip()


        if new_name:

            selected_student["name"] = (
                new_name.title()
            )


        print("\nEnter new marks.")
        print("Press Enter to keep the current mark.")


        for subject in subjects:

            current_mark = (
                selected_student["marks"][subject]
            )


            while True:

                new_mark = input(
                    f"{subject} "
                    f"(current {current_mark}): "
                ).strip()


                if new_mark == "":
                    break


                try:

                    new_mark = float(new_mark)


                    if new_mark < 0 or new_mark > 100:

                        print(
                            "Marks must be between "
                            "0 and 100."
                        )

                        continue


                    selected_student["marks"][subject] = (
                        new_mark
                    )

                    break


                except ValueError:

                    print(
                        "Please enter a valid number."
                    )


        print("Student updated successfully.")


    # ========================================================
    # DELETE STUDENT
    # ========================================================

    elif choice == "4":

        print("\n=== Delete Student ===")


        try:

            student_id = int(
                input("Enter student ID: ").strip()
            )

        except ValueError:

            print("Please enter a valid ID.")
            continue


        selected_student = None


        for student in students:

            if student["id"] == student_id:

                selected_student = student
                break


        if selected_student is None:

            print("Student not found.")
            continue


        students.remove(selected_student)


        print(
            f"Student "
            f"'{selected_student['name']}' "
            f"deleted successfully."
        )


    # ========================================================
    # SEARCH STUDENTS
    # ========================================================

    elif choice == "5":

        search_term = input(
            "Search by student name: "
        ).strip().lower()


        if not search_term:

            print("Search term cannot be empty.")
            continue


        matching_students = [

            student

            for student in students

            if search_term
            in student["name"].lower()
        ]


        if not matching_students:

            print("No matching students found.")
            continue


        print("\n=== Search Results ===")


        for student in matching_students:

            average = (
                sum(student["marks"].values())
                / len(subjects)
            )


            print(
                f"[{student['id']}] "
                f"{student['name']} | "
                f"Average: {average:.2f}"
            )


    # ========================================================
    # FILTER BY GRADE
    # ========================================================

    elif choice == "6":

        grade = input(
            "Enter grade (A/B/C/D/F): "
        ).strip().upper()


        if grade not in ["A", "B", "C", "D", "F"]:

            print("Invalid grade.")
            continue


        matching_students = []


        for student in students:

            average = (
                sum(student["marks"].values())
                / len(subjects)
            )


            if average >= 90:
                student_grade = "A"

            elif average >= 80:
                student_grade = "B"

            elif average >= 70:
                student_grade = "C"

            elif average >= 60:
                student_grade = "D"

            else:
                student_grade = "F"


            if student_grade == grade:

                matching_students.append(
                    student
                )


        print(
            f"\n=== Grade {grade} Students ==="
        )


        if not matching_students:

            print(
                f"No students with grade {grade}."
            )

            continue


        for student in matching_students:

            average = (
                sum(student["marks"].values())
                / len(subjects)
            )


            print(
                f"[{student['id']}] "
                f"{student['name']} | "
                f"Average: {average:.2f}"
            )


    # ========================================================
    # RANK STUDENTS
    # ========================================================

    elif choice == "7":

        if not students:

            print("No students available.")
            continue


        ranked_students = sorted(
            students,
            key=lambda student:
                sum(student["marks"].values())
                / len(subjects),
            reverse=True
        )


        print("\n=== Student Rankings ===")


        for rank, student in enumerate(
            ranked_students,
            start=1
        ):

            total = sum(
                student["marks"].values()
            )


            average = (
                total
                / len(subjects)
            )


            if average >= 90:
                grade = "A"

            elif average >= 80:
                grade = "B"

            elif average >= 70:
                grade = "C"

            elif average >= 60:
                grade = "D"

            else:
                grade = "F"


            print(
                f"{rank}. "
                f"{student['name']} | "
                f"Total: {total:.2f} | "
                f"Average: {average:.2f} | "
                f"Grade: {grade}"
            )


    # ========================================================
    # SUBJECT ANALYSIS
    # ========================================================

    elif choice == "8":

        if not students:

            print("No students available.")
            continue


        print("\n=== Subject Analysis ===")


        for subject in subjects:

            subject_total = sum(
                student["marks"][subject]
                for student in students
            )


            subject_average = (
                subject_total
                / len(students)
            )


            highest_student = max(
                students,
                key=lambda student:
                    student["marks"][subject]
            )


            lowest_student = min(
                students,
                key=lambda student:
                    student["marks"][subject]
            )


            print(
                f"\n{subject}"
            )

            print(
                f"  Class average: "
                f"{subject_average:.2f}"
            )

            print(
                f"  Highest: "
                f"{highest_student['name']} "
                f"({highest_student['marks'][subject]})"
            )

            print(
                f"  Lowest: "
                f"{lowest_student['name']} "
                f"({lowest_student['marks'][subject]})"
            )


    # ========================================================
    # CLASS STATISTICS
    # ========================================================

    elif choice == "9":

        if not students:

            print("No students available.")
            continue


        student_averages = {}


        for student in students:

            average = (
                sum(student["marks"].values())
                / len(subjects)
            )


            student_averages[student["id"]] = (
                average
            )


        class_average = (
            sum(student_averages.values())
            / len(students)
        )


        highest_student = max(
            students,
            key=lambda student:
                student_averages[student["id"]]
        )


        lowest_student = min(
            students,
            key=lambda student:
                student_averages[student["id"]]
        )


        grade_counts = {}


        for student in students:

            average = (
                student_averages[student["id"]]
            )


            if average >= 90:
                grade = "A"

            elif average >= 80:
                grade = "B"

            elif average >= 70:
                grade = "C"

            elif average >= 60:
                grade = "D"

            else:
                grade = "F"


            grade_counts[grade] = (
                grade_counts.get(grade, 0) + 1
            )


        print("\n=== Class Statistics ===")


        print(
            f"Total students: "
            f"{len(students)}"
        )


        print(
            f"Class average: "
            f"{class_average:.2f}"
        )


        print(
            f"Top student: "
            f"{highest_student['name']} "
            f"({student_averages[highest_student['id']]:.2f})"
        )


        print(
            f"Lowest student: "
            f"{lowest_student['name']} "
            f"({student_averages[lowest_student['id']]:.2f})"
        )


        print("\nStudents by grade:")


        for grade, count in sorted(
            grade_counts.items()
        ):

            print(
                f"- Grade {grade}: "
                f"{count}"
            )


    # ========================================================
    # DETAILED REPORT
    # ========================================================

    elif choice == "10":

        if not students:

            print("No students available.")
            continue


        class_average = sum(
            sum(student["marks"].values())
            / len(subjects)
            for student in students
        ) / len(students)


        ranked_students = sorted(
            students,
            key=lambda student:
                sum(student["marks"].values())
                / len(subjects),
            reverse=True
        )


        grade_counts = {}


        for student in students:

            average = (
                sum(student["marks"].values())
                / len(subjects)
            )


            if average >= 90:
                grade = "A"

            elif average >= 80:
                grade = "B"

            elif average >= 70:
                grade = "C"

            elif average >= 60:
                grade = "D"

            else:
                grade = "F"


            grade_counts[grade] = (
                grade_counts.get(grade, 0) + 1
            )


        print("\n========================================")
        print("       DETAILED CLASS REPORT")
        print("========================================")


        print(
            f"\nTotal students : "
            f"{len(students)}"
        )


        print(
            f"Class average  : "
            f"{class_average:.2f}"
        )


        print("\nStudents by grade:")


        for grade, count in sorted(
            grade_counts.items()
        ):

            print(
                f"- Grade {grade}: "
                f"{count}"
            )


        print("\nTop 3 students:")


        for rank, student in enumerate(
            ranked_students[:3],
            start=1
        ):

            total = sum(
                student["marks"].values()
            )


            average = (
                total
                / len(subjects)
            )


            print(
                f"{rank}. "
                f"{student['name']} — "
                f"Average: {average:.2f}"
            )


        print("\nSubject averages:")


        for subject in subjects:

            subject_average = (
                sum(
                    student["marks"][subject]
                    for student in students
                )
                / len(students)
            )


            print(
                f"- {subject}: "
                f"{subject_average:.2f}"
            )


    # ========================================================
    # EXIT
    # ========================================================

    elif choice == "11":

        print("\nGoodbye!")
        break


    # ========================================================
    # INVALID OPTION
    # ========================================================

    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 11."
        )