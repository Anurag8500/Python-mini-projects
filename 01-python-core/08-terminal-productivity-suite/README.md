# Terminal Productivity Suite

A command-line productivity application that combines task management, note management, expense tracking, dashboard statistics, and global search into a single Python program.

This project is the final project of **Phase 01 — Python Core** and combines patterns and concepts learned throughout the previous projects.

## Features

### Task Manager

* Add tasks
* Assign unique task IDs
* Set task priority
* Track pending and completed tasks
* Mark tasks as completed
* Delete tasks
* Validate task input

### Notes Manager

* Create notes
* Store note titles and content
* View saved notes
* Delete notes
* Validate note input

### Expense Tracker

* Record expenses
* Assign expense categories
* View recorded expenses
* Calculate total spending
* Delete expenses
* Validate expense input

### Dashboard

Displays an overview of the current application state:

* Total tasks
* Completed tasks
* Pending tasks
* Tasks by priority
* Total notes
* Number of expense transactions
* Total spending

### Global Search

Searches across:

* Task titles
* Note titles
* Note content

Search input is normalized to make matching case-insensitive.

## Concepts Practiced

* Variables and data types
* Strings and string methods
* `.strip()`
* `.lower()`
* `.title()`
* `.upper()`
* Lists
* Dictionaries
* Lists containing dictionaries
* Nested data structures
* Dictionary access and updates
* Dictionary `.items()`
* Dictionary `.get()`
* `append()`
* `remove()`
* `len()`
* `sum()`
* `while True`
* `for` loops
* Nested loops
* `if / elif / else`
* `break`
* `continue`
* `try / except`
* `ValueError`
* Boolean values
* Flag variables
* List comprehensions
* Membership testing with `in`
* Input validation
* Searching
* Filtering
* Aggregation
* Frequency counting
* Unique identifiers
* Application state management
* Basic CRUD operations
* F-strings
* Number formatting with `:.2f`

## Data Models

The application maintains three separate collections.

### Tasks

```python
{
    "id": 1,
    "title": "Learn Python",
    "priority": "high",
    "status": "pending"
}
```

### Notes

```python
{
    "id": 1,
    "title": "Python Notes",
    "content": "Review dictionary methods."
}
```

### Expenses

```python
{
    "id": 1,
    "category": "food",
    "amount": 450.00
}
```

Each type of record is stored in its own list:

```python
tasks = []
notes = []
expenses = []
```

This keeps the three domains separate while allowing the dashboard and search functionality to work across them.

## CRUD Pattern

The project brings together the CRUD operations practiced throughout the earlier projects:

```text
CREATE
  ↓
Add tasks, notes, and expenses

READ
  ↓
View, search, and analyze data

UPDATE
  ↓
Change task status

DELETE
  ↓
Remove tasks, notes, or expenses
```

This pattern will become especially important later when working with databases and APIs.

## How It Works

```text
Start Application
       ↓
Initialize Application Data
       ↓
Display Main Menu
       ↓
Choose a Module
       ↓
Manage Tasks / Notes / Expenses
       ↓
Return to Main Menu
       ↓
Dashboard / Global Search
       ↓
Exit
```

## Example

```text
=== Terminal Productivity Suite ===

=== Main Menu ===
1. Task Manager
2. Notes Manager
3. Expense Tracker
4. Dashboard
5. Search Everything
6. Exit

Choose an option: 1

=== Task Manager ===
1. View tasks
2. Add task
3. Mark task as completed
4. Delete task
5. Back

Choose an option: 2

Task title: Complete Python project
Priority (low / medium / high): high

Task #1 added successfully.
```

Adding an expense:

```text
=== Expense Tracker ===

1. View expenses
2. Add expense
3. Delete expense
4. Back

Choose an option: 2

Category: food
Amount: ₹650

Expense #1 added successfully.
```

Dashboard:

```text
=== Productivity Dashboard ===

Tasks
Total: 1
Completed: 0
Pending: 1
By priority:
- Low: 0
- Medium: 0
- High: 1

Notes
Total notes: 2

Expenses
Transactions: 1
Total spent: ₹650.00
```

## What I Learned

* How multiple data models can coexist inside one application
* How to manage application state across different features
* How to build nested menu systems using loops
* How to perform CRUD operations on in-memory data
* How stable IDs can identify records independently of their position in a list
* How to reuse earlier patterns such as searching, filtering, aggregation, and frequency counting
* How to combine data from different parts of an application into a dashboard
* How to perform a search across multiple types of records
* How input validation prevents invalid data from entering the application
* How larger applications begin to require better code organization

## Important Design Concepts

### Separate Data Models

Tasks, notes, and expenses are stored separately because they represent different types of information.

### Stable IDs

Each record receives its own ID instead of relying on its position in a list.

This means deleting one record does not change the identity of the remaining records.

### Normalized Input

User input is normalized before being stored or searched.

For example:

```text
Food
food
FOOD
```

are treated consistently as:

```text
food
```

and formatted as `Food` when displayed.

### In-Memory State

All application data currently exists only while the program is running.

Closing the application clears the data because persistent storage has not yet been implemented.

## Limitations

* Data is not persisted between program runs
* The application is currently implemented in a single Python file
* The menu and business logic are not yet separated into reusable functions
* No automated tests are included
* Search is limited to tasks and notes

These limitations are intentional at this stage of the curriculum.

The purpose of this project is to complete the **core Python phase** before introducing more structured program design.

## Possible Improvements

* Refactor the application using functions
* Separate features into modules
* Add persistent JSON or CSV storage
* Add SQLite database support
* Add task deadlines and timestamps
* Add note search and filtering
* Add expense categories and reports to the dashboard
* Add sorting for tasks and expenses
* Add edit functionality for tasks and notes
* Add automated tests
* Build a GUI or web interface
* Convert the application into an API-backed system

## Project Structure

```text
08-terminal-productivity-suite/
│
├── main.py
└── README.md
```

## Phase Milestone

This project completes:

**Phase 01 — Python Core**

Projects completed:

```text
01 — Personal Finance Analyzer
02 — Student Performance Analyzer
03 — Inventory & Billing System
04 — CLI Quiz Engine
05 — Bank Account Simulator
06 — Text Analyzer
07 — Mini Task Manager
08 — Terminal Productivity Suite
```

The next stage of the curriculum moves beyond large single-file procedural programs and focuses on **functions, abstraction, modularity, and program design**.

## Status

**Completed — Phase 01: Python Core**

Project 08 of the Python Mini Projects curriculum.
