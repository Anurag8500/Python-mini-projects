# Student Performance Analyzer

A command-line Python application that collects student marks and generates a performance report with individual results, rankings, and subject-level statistics.

## Features

* Record multiple students
* Record marks for multiple subjects
* Calculate each student's total marks
* Calculate each student's average
* Assign a grade based on average marks
* Rank students from highest to lowest performance
* Calculate the overall class average
* Calculate average marks for each subject
* Identify the highest-performing student
* Identify the lowest-performing student

## Concepts Practiced

* Variables and data types
* User input with `input()`
* Type conversion with `int()` and `float()`
* Strings and `.strip()`
* Lists
* Dictionaries
* Nested dictionaries
* Lists containing dictionaries
* `for` loops
* Nested loops
* Conditional statements
* Dictionary methods:

  * `.values()`
  * `.items()`
* Built-in functions:

  * `sum()`
  * `len()`
  * `sorted()`
* `lambda` functions
* `key=` for sorting
* `reverse=True`
* `enumerate()`
* List indexing and negative indexing
* F-strings
* Number formatting with `:.2f`
* Basic data processing and aggregation

## Data Structure

Each student is represented using a dictionary containing their name, subject marks, total, average, and grade.

```python
{
    "name": "Anurag",
    "marks": {
        "Python": 85.0,
        "Math": 78.0,
        "Database": 91.0
    },
    "total": 254.0,
    "average": 84.67,
    "grade": "B"
}
```

Multiple student dictionaries are stored inside a list:

```python
students = [
    student_1,
    student_2,
    student_3
]
```

## Example

```text
=== Student Performance Analyzer ===

Number of students: 3

Student 1
Name: Anurag
Python marks: 85
Math marks: 78
Database marks: 91

Student 2
Name: Rahul
Python marks: 72
Math marks: 88
Database marks: 79

Student 3
Name: Priya
Python marks: 95
Math marks: 91
Database marks: 94

=== Performance Report ===

1. Priya
   Total: 280.00
   Average: 93.33
   Grade: A

2. Anurag
   Total: 254.00
   Average: 84.67
   Grade: B

3. Rahul
   Total: 239.00
   Average: 79.67
   Grade: C

Class average: 85.89
Top student: Priya
Lowest student: Rahul

Subject averages:
- Python: 84.00
- Math: 85.67
- Database: 88.00
```

## What I Learned

* How to represent structured information using dictionaries
* How to store multiple records using a list of dictionaries
* How nested dictionaries can represent related data
* How nested loops can process multiple students and subjects
* How to calculate statistics from collections of data
* How `.values()` retrieves dictionary values
* How `.items()` provides dictionary keys and values together
* How `sorted()` can sort structured data
* How `lambda` and `key=` can control sorting
* How `enumerate()` can be used to generate rankings
* How to add calculated information to existing dictionaries
* How to transform raw input into useful summary information

## Possible Improvements

* Validate student names and marks
* Prevent marks outside the valid range
* Add pass/fail status
* Find the highest score in each subject
* Identify the best-performing subject
* Search for a student by name
* Support a variable number of subjects
* Export the report to a file
* Save and load student data
* Refactor the program using functions
* Add automated tests

## Status

**Completed — Phase 01: Python Core**

Project 02 of the Python Mini Projects curriculum.
