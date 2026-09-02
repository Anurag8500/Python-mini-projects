# Project #13: Student Records & Ranking System

A Python-based terminal application for managing student records, updating academic information, and generating class-level performance analytics.

The project combines **CRUD operations, nested dictionaries, sorting, filtering, aggregation, ranking, and statistical analysis** into a single interactive program.

It builds directly on concepts introduced in the earlier Student Performance Analyzer, Contact Management System, Inventory Analytics Engine, and Expense Categorization Engine.

## Features

* View all student records
* Add new students
* Update student names and marks
* Delete student records
* Search students by name
* Filter students by grade
* Rank students by average marks
* Analyze individual subjects
* Calculate class statistics
* Track grade distribution
* Generate a detailed class report
* Validate student marks between 0 and 100
* Maintain unique student IDs

## Concepts Practiced

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Nested dictionaries
* Dictionary values and items
* Sets indirectly through data-processing patterns

### Control Flow

* `while` loops
* `for` loops
* Nested loops
* `if / elif / else`
* `break`
* `continue`

### Data Processing

* `len()`
* `sum()`
* `max()`
* `min()`
* `sorted()`
* `enumerate()`
* List comprehensions
* Generator expressions
* Dictionary `.get()`
* Dictionary `.items()`
* List slicing

### Data Validation

* Numeric input validation
* Range validation
* Empty input checks
* Duplicate-name detection
* Student ID validation

### Ranking and Analytics

* Sorting records by calculated values
* Calculating averages
* Finding highest and lowest performers
* Grouping students by grade
* Calculating subject averages
* Aggregating class-level statistics

## Data Structure

Each student is represented by a dictionary:

```python
{
    "id": 1,
    "name": "Anurag Bardhan",
    "marks": {
        "Python": 91,
        "Math": 84,
        "Database": 88
    }
}
```

All student records are stored in a list:

```python
students = [
    {...},
    {...},
    {...}
]
```

The `marks` dictionary is nested inside each student record.

This gives the data a structure of:

```text
students
    ↓
student record
    ↓
marks
    ├── Python
    ├── Math
    └── Database
```

## Supported Subjects

The application currently tracks three subjects:

```text
Python
Math
Database
```

The subjects are stored separately so that the same processing logic can be reused throughout the program.

## Grade System

Students are assigned grades according to their average marks:

|  Average | Grade |
| -------: | :---: |
|   90–100 |   A   |
| 80–89.99 |   B   |
| 70–79.99 |   C   |
| 60–69.99 |   D   |
| Below 60 |   F   |

The grade is derived from the student's current marks rather than stored permanently in the record.

## Main Menu

```text
=== Menu ===
1. View all students
2. Add student
3. Update student
4. Delete student
5. Search students
6. Filter by grade
7. Rank students
8. Subject analysis
9. Class statistics
10. Detailed report
11. Exit
```

## View All Students

The program displays each student's:

* ID
* Name
* Subject marks
* Total marks
* Average marks
* Grade

Example:

```text
[1] Anurag Bardhan
  Python: 91
  Math: 84
  Database: 88
  Total: 263.00
  Average: 87.67
  Grade: B
```

The total and average are calculated from the student's marks when the record is displayed.

## Adding Students

New students can be added interactively.

The program asks for:

* Student name
* Python marks
* Math marks
* Database marks

Marks are validated so that only values between `0` and `100` are accepted.

Each new student receives a unique numeric ID.

Example:

```text
=== Add Student ===

Student name: Arjun Mehta
Python marks: 87
Math marks: 91
Database marks: 84

Student added successfully with ID 6.
```

## Updating Students

Existing student records can be modified using their ID.

The user can:

* Change the student's name
* Update individual subject marks
* Keep an existing value by pressing Enter

Example:

```text
Updating: Arjun Mehta

New name (press Enter to keep 'Arjun Mehta'):
Enter new marks.
Press Enter to keep the current mark.

Python (current 87): 90
Math (current 91):
Database (current 84): 88

Student updated successfully.
```

Only the fields that need to change have to be entered.

## Deleting Students

A student can be removed using their ID.

The selected record is located first and then removed from the list.

This reuses the list-removal pattern used in previous CRUD projects.

## Searching Students

The search feature matches student names case-insensitively.

For example, searching for:

```text
anurag
```

will match:

```text
Anurag Bardhan
```

The search is implemented using a list comprehension:

```python
matching_students = [
    student
    for student in students
    if search_term in student["name"].lower()
]
```

This reinforces the filtering pattern introduced in previous projects.

## Filtering by Grade

Students can be filtered according to their calculated grade.

For example:

```text
=== Grade A Students ===

[3] Priya Singh | Average: 92.67
```

The program recalculates the average for each student, determines the corresponding grade, and keeps only matching records.

## Student Rankings

Students can be ranked from highest to lowest average.

The program uses `sorted()` with a calculated average as the sorting key:

```python
ranked_students = sorted(
    students,
    key=lambda student:
        sum(student["marks"].values())
        / len(subjects),
    reverse=True
)
```

Example:

```text
=== Student Rankings ===

1. Priya Singh | Total: 278.00 | Average: 92.67 | Grade: A
2. Anurag Bardhan | Total: 263.00 | Average: 87.67 | Grade: B
3. Sneha Roy | Total: 249.00 | Average: 83.00 | Grade: B
```

This demonstrates how `sorted()` can rank complex records using a value that is calculated dynamically.

## Subject Analysis

Instead of analyzing students individually, the program can analyze the class from a subject perspective.

For every subject it calculates:

* Class average
* Highest-scoring student
* Lowest-scoring student

Example:

```text
=== Subject Analysis ===

Python
  Class average: 83.40
  Highest: Priya Singh (95)
  Lowest: Rohan Das (67)

Math
  Class average: 83.60
  Highest: Rahul Sharma (92)
  Lowest: Rohan Das (74)
```

This introduces an important analytical pattern:

```text
Student-centered analysis
        ↓
Subject-centered analysis
```

The same dataset is being viewed from different perspectives.

## Class Statistics

The class statistics section calculates overall performance information:

* Total number of students
* Class average
* Top student
* Lowest student
* Number of students in each grade

Example:

```text
=== Class Statistics ===

Total students: 5
Class average: 85.40
Top student: Priya Singh (92.67)
Lowest student: Rohan Das (70.33)

Students by grade:
- Grade A: 1
- Grade B: 3
- Grade C: 1
```

## Grade Distribution

The program uses a dictionary as a counter:

```python
grade_counts[grade] = (
    grade_counts.get(grade, 0) + 1
)
```

For example:

```python
{
    "A": 1,
    "B": 3,
    "C": 1
}
```

This converts individual student records into a compact class-level distribution.

## Detailed Report

The detailed report combines several statistics into one summary.

It includes:

### Class Overview

* Total students
* Class average

### Grade Distribution

* Number of students in each grade

### Top Performers

* Top three students
* Their average marks

### Subject Performance

* Average marks for every subject

Example:

```text
========================================
       DETAILED CLASS REPORT
========================================

Total students : 5
Class average  : 85.40

Students by grade:
- Grade A: 1
- Grade B: 3
- Grade C: 1

Top 3 students:
1. Priya Singh — Average: 92.67
2. Anurag Bardhan — Average: 87.67
3. Sneha Roy — Average: 83.00

Subject averages:
- Python: 83.40
- Math: 83.60
- Database: 83.40
```

## Derived Data

One important design choice in this project is that values such as:

```text
Total
Average
Grade
```

are calculated when needed rather than permanently stored inside each student dictionary.

For example, the raw record contains:

```python
{
    "id": 1,
    "name": "Anurag Bardhan",
    "marks": {
        "Python": 91,
        "Math": 84,
        "Database": 88
    }
}
```

The average is derived from:

```python
sum(student["marks"].values()) / len(subjects)
```

This means the displayed results always reflect the latest marks after an update.

## Why This Project Matters

This project moves beyond simple record management.

The program can now answer questions such as:

```text
Who is the top student?
What is the class average?
Which subject is performing best?
Who scored the highest in Python?
How many students received each grade?
Which students belong to grade A?
```

This is the transition from **CRUD-based programs** toward **data-driven applications**.

## Project Structure

```text
13-student-records-ranking-system/
│
├── main.py
└── README.md
```

The project intentionally remains a single-file application at this stage.

The next phase of the roadmap will introduce functions and modular design so that repeated logic can be separated into reusable components.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure your Python virtual environment is activated before running the project.

## Example Workflow

A typical session can follow this sequence:

```text
View existing students
        ↓
Add or update records
        ↓
Search / filter students
        ↓
Rank the class
        ↓
Analyze individual subjects
        ↓
View class statistics
        ↓
Generate detailed report
```

## Learning Progression

Project #13 combines patterns from several earlier projects:

```text
Project #02
Student records + nested marks
        ↓
Project #07
CRUD + IDs + filtering
        ↓
Project #09
Search + update + delete
        ↓
Project #10
Ranking + aggregation
        ↓
Project #11
Grouping + statistical analysis
        ↓
Project #13
Student management + academic analytics
```

The purpose is to repeatedly reuse concepts instead of learning each programming technique in isolation.

## Future Improvements

Possible extensions include:

* Store grade and average as calculated properties
* Add more subjects
* Track attendance
* Add semester-wise performance
* Import student records from CSV or JSON
* Export class reports
* Add subject-specific rankings
* Add pass/fail statistics
* Compare multiple classes
* Persist data using a database
* Add automated tests
* Refactor repeated calculations into functions

These improvements are intentionally reserved for later stages of the roadmap.

## Development Philosophy

This repository follows:

```text
Learn
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Understand
  ↓
Repeat
```

The goal is not simply to make the program work, but to understand the data structures, control flow, and logic behind it.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
