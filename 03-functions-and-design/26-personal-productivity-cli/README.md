# Project #26: Personal Productivity CLI

A command-driven Python productivity application that combines task management, notes, expense tracking, searching, and basic statistics.

This is the final project of **Phase 03 — Functions & Program Design**.

The project is intentionally compact and focuses on applying the design principles learned throughout the phase rather than introducing a large number of new features.

## Features

* Add tasks
* List tasks
* Complete tasks
* Delete tasks
* Add notes
* List notes
* Add expenses
* List expenses
* Search across tasks, notes, and expenses
* Display productivity statistics
* Command-based interface
* Dictionary-based command routing
* Reusable helper functions

## Commands

```text
add-task <title> | <priority>
list-tasks
complete <id>
delete-task <id>

add-note <title> | <content>
list-notes

add-expense <description> | <amount> | <category>
list-expenses

search <keyword>
stats
help
exit
```

## Example

```text
> add-task Learn Python functions | high
Task added with ID 1.

> add-note Python Ideas | Build a CLI project
Note added with ID 1.

> add-expense Coffee | 180 | food
Expense added with ID 1.

> list-tasks

=== Tasks ===
[1] Learn Python functions | High | Pending

> search python

=== Search Results ===
Task: [1] Learn Python functions | High | Pending

> stats

=== Statistics ===
Tasks: 1
Completed tasks: 0
Notes: 1
Expenses: 1
Total spending: ₹180.00
```

## Concepts Practiced

### Functions

* Function definitions
* Parameters
* Arguments
* Return values
* Helper functions
* Function composition
* Reusable functions
* Single-responsibility functions

### Command-Line Design

* Command parsing
* Command arguments
* Command dispatch
* Dynamic function lookup
* Command validation
* Interactive command loops

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Dictionary `.get()`
* Dictionary `.items()`

### Data Processing

* `len()`
* `sum()`
* List comprehensions
* Generator expressions
* String searching
* Aggregation

### Input Processing

* `.strip()`
* `.lower()`
* `.split()`
* `maxsplit`
* Numeric conversion
* Input validation

## Application Structure

The application contains three main types of data:

```text
Personal Productivity CLI
        │
        ├── Tasks
        ├── Notes
        └── Expenses
```

Each type has its own functions, while common utilities are shared.

## Tasks

Tasks contain:

```python
{
    "id": 1,
    "title": "Learn Python functions",
    "priority": "high",
    "status": "pending"
}
```

Supported task operations include:

```text
add-task
list-tasks
complete
delete-task
```

## Notes

Notes contain:

```python
{
    "id": 1,
    "title": "Python Ideas",
    "content": "Build a CLI project"
}
```

The application supports:

```text
add-note
list-notes
```

## Expenses

Expenses contain:

```python
{
    "id": 1,
    "description": "Coffee",
    "amount": 180,
    "category": "food"
}
```

Supported operations include:

```text
add-expense
list-expenses
```

The application also calculates total spending.

## Command Routing

The main design pattern comes from the command dictionary:

```python
commands = {
    "add-task": add_task,
    "complete": complete_task,
    "search": search,
    "stats": ...
}
```

A command entered by the user is looked up in this dictionary.

For example:

```text
> search python
```

is processed as:

```text
command_name → search
arguments     → python
        ↓
commands["search"]
        ↓
search()
```

This avoids creating a large `if / elif` chain for every command.

## Shared Helper Functions

The project uses:

```python
find_by_id(records, record_id)
```

to search different collections.

The same function can therefore work with:

```text
tasks
notes
expenses
```

as long as the records contain an `id` field.

This demonstrates the benefit of writing generic functions instead of repeating the same logic.

## Search

The `search` command searches across all three data types:

```text
> search python
```

It checks:

* Task titles
* Note titles
* Note content
* Expense descriptions
* Expense categories

This demonstrates how one function can coordinate searches across multiple collections.

## Statistics

The `stats` command combines information from the different parts of the application.

It reports:

* Total tasks
* Completed tasks
* Total notes
* Total expenses
* Total spending

Example:

```text
=== Statistics ===

Tasks: 5
Completed tasks: 2
Notes: 3
Expenses: 4
Total spending: ₹2,450.00
```

## Function Responsibilities

The project deliberately separates responsibilities.

Examples:

```text
add_task()
    → create a task

complete_task()
    → change task state

find_by_id()
    → locate a record

search()
    → search across collections

show_stats()
    → calculate application statistics

show_help()
    → display available commands
```

The main command loop is therefore responsible primarily for:

```text
Read command
    ↓
Parse command
    ↓
Find handler
    ↓
Call handler
```

## Functions as Values

The project continues the function-dispatch concept introduced in Project #22.

Functions are stored inside a dictionary:

```python
commands = {
    "add-task": add_task,
    "search": search
}
```

They can then be retrieved dynamically:

```python
command_function = commands.get(command_name)
```

and called:

```python
command_function(arguments)
```

This is an important Python concept used in command-line tools, event systems, and other dispatch-based designs.

## Project Structure

```text
26-personal-productivity-cli/
│
├── main.py
└── README.md
```

The project intentionally remains a single-file application.

The focus is on applying modular function design rather than introducing a larger package structure.

## How to Run

From the project directory:

```bash
python main.py
```

After starting the application, type:

```text
help
```

to see all available commands.

## Example Workflow

```text
Start application
      ↓
Create tasks
      ↓
Create notes
      ↓
Record expenses
      ↓
Search across all data
      ↓
Complete tasks
      ↓
View statistics
      ↓
Exit
```

## Learning Progression

Project #26 combines the major lessons of Phase 03:

```text
Project #18
Functions + modular workflows
        ↓
Project #19
Reusable validation functions
        ↓
Project #20
Reusable text-processing functions
        ↓
Project #21
Filesystem utilities
        ↓
Project #22
Command parsing + dynamic dispatch
        ↓
Project #23
Configuration + JSON persistence
        ↓
Project #24
Reusable reporting functions
        ↓
Project #25
Refactoring existing code
        ↓
Project #26
New application designed with functions
```

## Phase 03 Milestone

With Project #26 completed, the Phase 03 goal is to be comfortable with:

```text
Functions
Parameters
Arguments
Return values
Helper functions
Function composition
Reusable utilities
Command routing
Shared state
Validation
File interaction
JSON data
Report generation
Refactoring
```

The next phase will shift the focus from program structure toward **Files & Data Processing**.

## Why This Project Matters

This project represents an important transition in the learning roadmap.

Earlier projects primarily focused on:

```text
"What can Python do?"
```

Phase 03 focuses more on:

```text
"How should I structure my Python program?"
```

Project #26 puts that principle into practice by building a fresh application from the beginning with functions, shared utilities, and a command-dispatch architecture.

## Future Improvements

Possible extensions include:

* Persist tasks, notes, and expenses
* Add update commands
* Add filtering
* Add due dates
* Add expense summaries
* Add configuration support
* Add report generation
* Split functionality into modules
* Add automated tests
* Introduce classes where appropriate
* Package the CLI for installation

These improvements will be introduced in later phases rather than making this project unnecessarily large.

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

The goal is to understand not only how individual functions work, but how multiple functions can be combined into a coherent application architecture.
