# Mini Task Manager

A command-line Python application for managing tasks through an interactive menu. The program supports creating, viewing, updating, deleting, searching, filtering, and analyzing tasks based on their status and priority.

The project focuses on practical data management, application state, CRUD operations, filtering, and maintaining structured records using Python's core data structures.

## Features

* Add new tasks
* Assign unique task IDs
* Assign task priorities:

  * Low
  * Medium
  * High
* Track task status
* Mark tasks as completed
* Delete tasks
* View all tasks
* Search tasks by title
* Filter tasks by status
* Filter tasks by priority
* Display task statistics
* Count completed and pending tasks
* Count tasks by priority
* Validate task input
* Handle invalid task IDs
* Handle invalid priorities
* Interactive command-line menu

## Concepts Practiced

* Variables and data types
* Strings and string methods
* `.strip()`
* `.lower()`
* `.title()`
* Lists
* Dictionaries
* Lists containing dictionaries
* Dictionary access and updates
* Dictionary membership with `in`
* `.append()`
* `.remove()`
* `.items()`
* `len()`
* `while True`
* `for` loops
* `if / elif / else`
* `break`
* `continue`
* `try / except`
* `ValueError`
* Boolean values
* Flag variables
* List comprehensions
* Searching
* Filtering
* Counting and aggregation
* State management
* Unique identifiers
* Basic CRUD operations

## Data Structure

Each task is represented as a dictionary:

```python
{
    "id": 1,
    "title": "Learn Python dictionaries",
    "priority": "high",
    "status": "pending"
}
```

All tasks are stored in a list:

```python
tasks = [
    {
        "id": 1,
        "title": "Learn Python dictionaries",
        "priority": "high",
        "status": "pending"
    },
    {
        "id": 2,
        "title": "Complete project",
        "priority": "medium",
        "status": "completed"
    }
]
```

A separate counter is used to generate unique task IDs:

```python
next_task_id = 1
```

## CRUD Operations

The project introduces the fundamental CRUD pattern:

```text
Create
  ↓
Add a new task

Read
  ↓
View, search, and filter tasks

Update
  ↓
Change task status

Delete
  ↓
Remove a task
```

This pattern is important because the same basic operations appear later when working with databases and APIs.

## How It Works

```text
Start application
      ↓
Initialize task list
      ↓
Display menu
      ↓
Choose an operation
      ↓
Process / validate input
      ↓
Modify or retrieve task data
      ↓
Display result
      ↓
Return to menu
      ↓
Exit when requested
```

## Example

```text
=== Mini Task Manager ===

=== Menu ===
1. View tasks
2. Add task
3. Mark task as completed
4. Delete task
5. Search tasks
6. Filter by status
7. Filter by priority
8. Show statistics
9. Exit

Choose an option: 2

Task title: Learn Python dictionaries
Priority (low / medium / high): high

Task #1 added successfully.
```

Viewing tasks:

```text
=== Tasks ===
[1] Learn Python dictionaries | Priority: High | Status: Pending
[2] Build next project | Priority: Medium | Status: Pending
```

Marking a task as completed:

```text
Choose an option: 3
Enter task ID: 1

Task marked as completed.
```

Statistics:

```text
=== Task Statistics ===
Total tasks: 2
Completed: 1
Pending: 1

By priority:
- Low: 0
- Medium: 1
- High: 1
```

## What I Learned

* How to represent real-world records using dictionaries
* How to manage multiple records using a list of dictionaries
* How to generate unique identifiers for records
* How to update existing dictionary data
* How to remove records from a list
* How to search structured data
* How to filter data using list comprehensions
* How to maintain application state while a program is running
* How to use `while True` to create an interactive CLI
* How to use `break` and `continue` to control program flow
* How to handle invalid numeric input with `try / except`
* How flag variables can track whether a record was found
* How to count and aggregate data using dictionaries
* How CRUD operations work at an application level
* How previously learned concepts such as `.get()`, loops, filtering, and frequency counting can be reused in a new problem

## Important Design Concepts

### Stable Task IDs

Tasks have their own IDs instead of using their position in the list.

For example:

```text
Task #1
Task #2
Task #3
```

If Task #2 is deleted, Task #3 remains Task #3.

This provides a stable identifier independent of the task's position in the list.

### Normalized Input

Priority and search input are normalized using `.strip()` and `.lower()` so that variations such as:

```text
HIGH
High
 high
```

are treated consistently.

The stored value can then be formatted using `.title()` when displayed.

### In-Memory State

All task data currently exists only while the program is running.

Closing the application removes the current task data because persistence has not yet been implemented.

## Possible Improvements

* Edit task titles and priorities
* Add due dates
* Add task descriptions
* Prevent duplicate task titles
* Sort tasks by priority or status
* Add completion percentages
* Add task creation timestamps
* Support multiple task lists or projects
* Save tasks to JSON
* Load tasks when the application starts
* Add persistent storage using SQLite
* Refactor the program using reusable functions
* Introduce object-oriented design
* Add automated tests

## Project Structure

```text
07-mini-task-manager/
│
├── main.py
└── README.md
```

## Status

**Completed — Phase 01: Python Core**

Project 07 of the Python Mini Projects curriculum.
