# Project #27: CSV Data Analyzer

A Python-based command-line tool for loading, searching, filtering, sorting, grouping, analyzing, and exporting structured CSV data.

This project is the first project of **Phase 04 — Files & Data Processing**.

The main focus is learning how structured data stored in a CSV file can be loaded into Python, converted into usable data types, processed with functions, and written back to a new CSV file.

No external data-analysis libraries are used.

## Features

* Load data from a CSV file
* Display CSV records
* Display column names
* Show dataset dimensions
* Search across all columns
* Filter employees by department
* Filter employees by salary range
* Sort records by name
* Sort records by salary
* Sort records by experience
* Calculate salary statistics
* Find highest-paid and lowest-paid employees
* Find the most experienced employee
* Group employees by department
* Calculate departmental salary statistics
* Export data back to CSV

## Concepts Practiced

### CSV Processing

* Python `csv` module
* `csv.DictReader`
* `csv.DictWriter`
* CSV rows
* CSV headers
* CSV columns
* Reading structured files
* Writing structured files

### Functions

* Function definitions
* Parameters
* Return values
* Helper functions
* Reusable processing functions
* Separation of responsibilities

### Data Conversion

* Converting strings to `int`
* Converting strings to `float`
* Handling invalid numeric values

### Data Analysis

* `len()`
* `sum()`
* `min()`
* `max()`
* `sorted()`
* `enumerate()`
* List comprehensions
* Generator expressions
* Dictionary aggregation
* Lambda functions

### Searching and Filtering

* Case-insensitive search
* Partial matching
* Exact filtering
* Numerical range filtering
* Multi-column searching

## Why This Project Exists

Earlier projects mostly stored data directly in Python:

```python
sales = [
    {...},
    {...}
]
```

Project #27 moves the data outside the program.

The workflow becomes:

```text
employees.csv
     ↓
csv.DictReader
     ↓
Python dictionaries
     ↓
Data conversion
     ↓
Filtering / sorting / grouping
     ↓
Statistics
     ↓
CSV export
```

This is the foundation of practical data-processing programs.

## Sample CSV

The project uses an employee dataset:

```csv
id,name,department,salary,experience
1,Anurag Bardhan,Engineering,65000,2
2,Rahul Sharma,Marketing,52000,3
3,Priya Singh,Engineering,78000,4
4,Rohan Das,Design,48000,1
5,Sneha Roy,Engineering,72000,3
```

The CSV contains:

* Employee ID
* Name
* Department
* Salary
* Experience

## Main Menu

```text
=== Menu ===
1. View records
2. Show columns
3. Dataset summary
4. Search records
5. Filter by department
6. Filter by salary
7. Sort records
8. Column statistics
9. Department summary
10. Export current data
11. Exit
```

## Loading CSV Data

The program uses:

```python
csv.DictReader(file)
```

to read the CSV.

Each row becomes a dictionary.

For example:

```csv
1,Anurag Bardhan,Engineering,65000,2
```

becomes conceptually:

```python
{
    "id": "1",
    "name": "Anurag Bardhan",
    "department": "Engineering",
    "salary": "65000",
    "experience": "2"
}
```

The column names from the first row become dictionary keys.

## Important: CSV Values Are Strings

A key lesson in this project is that values read from a CSV are initially strings.

For example:

```python
"65000"
```

is text, not a number.

The program therefore converts numeric columns:

```python
row["salary"] = float(row["salary"])
row["experience"] = int(row["experience"])
```

After conversion:

```python
65000.0
```

can be used in numerical calculations.

This is an important difference between **reading data** and **preparing data for analysis**.

## Viewing Records

The program displays each employee in a readable format:

```text
=== Records ===

[1] Anurag Bardhan | Engineering | ₹65,000.00 | 2 years
[2] Rahul Sharma | Marketing | ₹52,000.00 | 3 years
[3] Priya Singh | Engineering | ₹78,000.00 | 4 years
```

## Dataset Summary

The summary provides basic information about the loaded dataset:

* Number of rows
* Number of columns
* Column names

Example:

```text
=== Dataset Summary ===

Rows: 10
Columns: 5
Column names: id, name, department, salary, experience
```

This is a basic form of dataset inspection.

## Showing Columns

The program reads the keys from the first record:

```python
rows[0].keys()
```

and displays the available columns.

This demonstrates how a program can work with a CSV without hard-coding every column name into the display logic.

## Searching Records

The search function checks all columns for a keyword.

For example:

```text
Enter search keyword: engineering
```

can return employees belonging to the Engineering department.

The comparison is case-insensitive.

The search works across:

* ID
* Name
* Department
* Salary
* Experience

This demonstrates searching structured records rather than only searching one field.

## Filtering by Department

The department filter performs an exact match:

```python
row["department"].lower() == department
```

For example:

```text
Department: engineering
```

returns all Engineering employees.

## Filtering by Salary Range

The salary filter accepts a minimum and maximum value.

For example:

```text
Minimum salary: ₹60000
Maximum salary: ₹80000
```

matches records where:

```text
60,000 ≤ salary ≤ 80,000
```

This reinforces numerical range filtering from earlier projects while applying it to data loaded from a file.

## Sorting

The dataset can be sorted by:

* Name
* Salary
* Experience

The user can choose:

* Ascending
* Descending

For example:

```python
sorted(
    rows,
    key=lambda row: float(row["salary"]),
    reverse=True
)
```

ranks employees from highest salary to lowest.

## Column Statistics

The statistics section calculates:

* Employee count
* Average salary
* Highest salary
* Lowest salary
* Most experienced employee

Example:

```text
=== Column Statistics ===

Employee count: 10
Average salary: ₹62,700.00
Highest salary: Aditya Roy (₹85,000.00)
Lowest salary: Rohan Das (₹48,000.00)
Highest experience: Vikram Singh (7 years)
```

The calculations are performed on the loaded dataset rather than hard-coded values.

## Department Summary

The program groups employees by department.

For each department it calculates:

* Number of employees
* Total salary
* Average salary

For example:

```text
=== Department Summary ===

Engineering
  Employees: 4
  Salary total: ₹300,000.00
  Average salary: ₹75,000.00

HR
  Employees: 2
  Salary total: ₹112,000.00
  Average salary: ₹56,000.00
```

This reuses the dictionary aggregation techniques learned in previous projects.

## Grouping Data

The grouping structure is created dynamically:

```python
department_data = {}
```

When a department is encountered for the first time, its statistics are initialized.

Conceptually:

```python
{
    "Engineering": {
        "employees": 4,
        "salary_total": 300000
    }
}
```

This turns individual CSV records into aggregated information.

## Exporting Data

The project can write the loaded data back to a CSV file using:

```python
csv.DictWriter
```

The field names are taken from the first record:

```python
fieldnames=rows[0].keys()
```

The writer then outputs:

```python
writer.writeheader()
writer.writerows(rows)
```

This demonstrates the complete CSV processing cycle:

```text
CSV file
   ↓
Read
   ↓
Python data
   ↓
Process
   ↓
Write
   ↓
CSV file
```

## Search, Filter, Sort, Analyze

The core processing workflow of this project is:

```text
Load
  ↓
Inspect
  ↓
Search
  ↓
Filter
  ↓
Sort
  ↓
Group
  ↓
Analyze
  ↓
Export
```

This is a fundamental pattern for data-processing applications.

## Error Handling

The program checks for common filesystem problems:

* Missing file
* Path that is not a file
* File-reading errors
* File-writing errors
* Invalid numeric input

CSV loading and writing are wrapped with:

```python
try:
    ...
except OSError:
    ...
```

This prevents common filesystem failures from terminating the program unexpectedly.

## Project Structure

```text
27-csv-data-analyzer/
│
├── main.py
├── README.md
└── data/
    └── employees.csv
```

## How to Run

From the project directory:

```bash
python main.py
```

When prompted for the CSV path, enter:

```text
data/employees.csv
```

Example:

```text
Enter CSV file path (example: data/employees.csv): data/employees.csv
```

## Example Workflow

```text
Load employees.csv
        ↓
View records
        ↓
Inspect columns
        ↓
Search employees
        ↓
Filter by department or salary
        ↓
Sort records
        ↓
Calculate statistics
        ↓
Analyze departments
        ↓
Export processed data
```

## Learning Progression

Project #27 begins Phase 04 and builds on the function and filesystem concepts from Phase 03:

```text
Project #18
Functions + modular design
        ↓
Project #21
Filesystem operations
        ↓
Project #23
JSON persistence
        ↓
Project #24
Reporting pipelines
        ↓
Project #27
CSV structured-data processing
```

The important new transition is:

```text
Python data structures
        ↓
External structured data
        ↓
Data conversion
        ↓
Data analysis
        ↓
Processed output
```

## Why This Project Matters

CSV is one of the most common formats for exchanging structured tabular data.

It is frequently used for:

```text
Spreadsheets
Datasets
Business reports
Exports
Imports
Data migrations
Analytics pipelines
```

Understanding how CSV data is represented internally is valuable before moving to higher-level tools such as pandas and database systems.

The goal of this project is to understand the underlying process first:

```text
File
  ↓
Rows
  ↓
Records
  ↓
Python data structures
  ↓
Analysis
```

## Future Improvements

Possible extensions include:

* Support arbitrary CSV column names
* Add dynamic numeric-column detection
* Filter by any column
* Support multiple simultaneous filters
* Add missing-value handling
* Add duplicate-record detection
* Add CSV comparison
* Add column-level statistics
* Export filtered results instead of the full dataset
* Support JSON conversion
* Process multiple CSV files
* Build reusable CSV-processing modules
* Add automated tests
* Introduce pandas after understanding the underlying CSV workflow

These improvements will be introduced progressively throughout the Files & Data Processing phase.

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

The goal is to understand how structured data moves between a CSV file and Python, how values are converted into useful types, and how reusable functions can process that data.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
