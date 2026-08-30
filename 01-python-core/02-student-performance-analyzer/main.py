print("=== Student Performance Analyzer ===")

number_of_students = int(input("Number of students: "))

students = []

subjects = ["Python", "Math", "Database"]

for i in range(number_of_students):
    print(f"\nStudent {i + 1}")

    name = input("Name: ").strip()

    marks = {}

    for subject in subjects:
        score = float(input(f"{subject} marks: "))
        marks[subject] = score

    students.append({
        "name": name,
        "marks": marks
    })


# Calculate individual student results
for student in students:
    total = sum(student["marks"].values())
    average = total / len(subjects)

    student["total"] = total
    student["average"] = average

    if average >= 90:
        student["grade"] = "A"
    elif average >= 80:
        student["grade"] = "B"
    elif average >= 70:
        student["grade"] = "C"
    elif average >= 60:
        student["grade"] = "D"
    else:
        student["grade"] = "F"


# Rank students by average
ranked_students = sorted(
    students,
    key=lambda student: student["average"],
    reverse=True
)


# Class average
class_total = sum(student["average"] for student in students)
class_average = class_total / len(students)


# Subject averages
subject_averages = {}

for subject in subjects:
    total = sum(student["marks"][subject] for student in students)
    subject_averages[subject] = total / len(students)


# Display report
print("\n=== Performance Report ===")

for rank, student in enumerate(ranked_students, start=1):
    print(
        f"\n{rank}. {student['name']}"
        f"\n   Total: {student['total']:.2f}"
        f"\n   Average: {student['average']:.2f}"
        f"\n   Grade: {student['grade']}"
    )


print(f"\nClass average: {class_average:.2f}")

print(f"Top student: {ranked_students[0]['name']}")
print(f"Lowest student: {ranked_students[-1]['name']}")


print("\nSubject averages:")

for subject, average in subject_averages.items():
    print(f"- {subject}: {average:.2f}")

