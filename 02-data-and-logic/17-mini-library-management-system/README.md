# Project #17: Mini Library Management System

A Python-based terminal application for managing a small library collection, searching and filtering books, handling borrowing and returns, and generating library statistics.

This project is the final major project of **Phase 02 — Data & Logic**. It combines CRUD operations, nested data, searching, filtering, sorting, state management, validation, aggregation, and reporting into a single domain-oriented application.

## Features

* View all books
* Add new books
* Prevent duplicate book records
* Search books by title, author, or category
* Filter books by category
* Filter available books
* Filter borrowed books
* Filter books by publication year
* Sort books by title
* Sort books by author
* Sort books by publication year
* Sort in ascending or descending order
* Borrow books
* Prevent borrowing an already borrowed book
* Return books
* Prevent returning an already available book
* Track the current borrower
* View all borrowed books
* Calculate library statistics
* Analyze books by category
* Calculate borrowing rate
* Generate a detailed library report

## Concepts Practiced

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Nested collections
* Dictionary `.get()`
* Dictionary `.items()`

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
* `min()`
* `max()`
* `sorted()`
* `enumerate()`
* List comprehensions
* Generator expressions
* List slicing
* Aggregation
* Ranking

### CRUD Operations

* Create book
* Read book records
* Update borrowing state
* Delete is intentionally omitted from the current interface to keep the project focused on library circulation and state management.

### Validation

* Empty input validation
* Numeric input validation
* Publication year validation
* Category validation
* Duplicate book detection
* Book ID validation
* Borrowing-state validation

### State Management

The project introduces mutable record state:

```text
AVAILABLE
    ↓
BORROWED
    ↓
AVAILABLE
```

The state of a book determines which actions are currently valid.

## Book Data Structure

Each book is represented as a dictionary:

```python id="avw0gc"
{
    "id": "B001",
    "title": "Python Crash Course",
    "author": "Eric Matthes",
    "category": "programming",
    "year": 2019,
    "status": "available",
    "borrower": None
}
```

All books are stored in a list:

```python id="ek3u7j"
books = [
    {...},
    {...},
    {...}
]
```

The `status` and `borrower` fields represent the current circulation state of the book.

## Book Categories

The application supports:

```text id="e9h8i4"
Programming
Fiction
History
Self-help
Productivity
Science
Education
Other
```

Books can be filtered and grouped using these categories.

## Main Menu

```text id="1gqb97"
=== Menu ===
1. View all books
2. Add book
3. Search books
4. Filter books
5. Sort books
6. Borrow book
7. Return book
8. View borrowed books
9. Library statistics
10. Detailed report
11. Exit
```

## Viewing Books

The program displays:

* Book ID
* Title
* Author
* Category
* Publication year
* Current status
* Borrower, when applicable

Example:

```text id="jxxqkw"
[B001] Python Crash Course
  Author: Eric Matthes
  Category: Programming
  Year: 2019
  Status: Available

[B002] Clean Code
  Author: Robert C. Martin
  Category: Programming
  Year: 2008
  Status: Borrowed
  Borrower: Anurag Bardhan
```

## Adding Books

A new book requires:

* Title
* Author
* Category
* Publication year

The application checks whether the same title by the same author already exists.

New books begin in the available state:

```python id="wbnvha"
{
    "status": "available",
    "borrower": None
}
```

Each new book also receives a unique ID.

Example:

```text id="yo4v8q"
Book title: Designing Data-Intensive Applications
Author: Martin Kleppmann
Category: Programming
Publication year: 2017

Book added successfully with ID B009.
```

## Searching Books

Books can be searched using:

* Title
* Author
* Category

The search is case-insensitive and supports partial matching.

For example:

```text id="r0dssr"
Search by title, author, or category: python
```

can match:

```text id="70tzfs"
Python Crash Course
```

Input is normalized with:

```python id="qgk9er"
.strip().lower()
```

before searching.

## Filtering Books

The application provides multiple filtering modes.

### By Category

Shows books belonging to a selected category.

### Available Books

Returns only:

```python id="5f94wb"
book["status"] == "available"
```

### Borrowed Books

Returns only:

```python id="rwmw2n"
book["status"] == "borrowed"
```

### Published After a Year

The user enters a year and the application keeps books published after that year.

This reinforces range-based filtering.

## Sorting Books

Books can be sorted by:

* Title
* Author
* Publication year

The user can choose ascending or descending order.

Example:

```python id="8n1wyj"
sorted_books = sorted(
    books,
    key=lambda book: book["year"],
    reverse=True
)
```

This produces a list ordered from newest to oldest.

For text fields, the program uses normalized lowercase values for predictable alphabetical sorting.

## Borrowing Books

A book can be borrowed using its ID.

Before changing the state, the program checks whether the book is already borrowed.

If the book is available:

```text id="3z8yvq"
AVAILABLE
    ↓
BORROW
    ↓
BORROWED
```

The program changes:

```python id="lpdqwg"
selected_book["status"] = "borrowed"
selected_book["borrower"] = borrower_name
```

This represents a state transition.

## Preventing Double Borrowing

A borrowed book cannot be borrowed again.

The program checks:

```python id="f5u0yk"
if selected_book["status"] == "borrowed":
```

and stops the operation.

Example:

```text id="u1n7je"
Book is already borrowed by Anurag Bardhan.
```

This introduces a basic business rule.

## Returning Books

A borrowed book can be returned.

The program changes:

```python id="0j7igp"
selected_book["status"] = "available"
selected_book["borrower"] = None
```

The state becomes:

```text id="dngkq2"
BORROWED
    ↓
RETURN
    ↓
AVAILABLE
```

A book that is already available cannot be returned again.

## Viewing Borrowed Books

The application creates a filtered list containing only borrowed books.

Example:

```text id="lx9i3e"
=== Borrowed Books ===

1. Clean Code | Borrower: Anurag Bardhan
2. Deep Work | Borrower: Priya Singh

Total borrowed books: 2
```

This is another practical use of list comprehensions:

```python id="aa5w8u"
borrowed_books = [
    book
    for book in books
    if book["status"] == "borrowed"
]
```

## Library Statistics

The statistics section calculates:

* Total books
* Available books
* Borrowed books
* Oldest book
* Newest book
* Most common category
* Books per category

Example:

```text id="yq8r08"
=== Library Statistics ===

Total books: 8
Available books: 6
Borrowed books: 2
Oldest book: The Alchemist (1988)
Newest book: Atomic Habits Workbook (2020)
Most common category: Programming (3 books)

Books by category:
- Fiction: 1
- History: 1
- Productivity: 1
- Programming: 3
- Self-Help: 2
```

## Category Counting

The application uses a dictionary to count books by category:

```python id="5qhaxm"
category_counts[category] = (
    category_counts.get(category, 0) + 1
)
```

This converts individual book records into an aggregated summary.

For example:

```python id="0h39oe"
{
    "programming": 3,
    "fiction": 1,
    "history": 1
}
```

## Borrowing Rate

The borrowing rate indicates what percentage of the library is currently borrowed.

It is calculated as:

```text id="cgd8d5"
Borrowed Books
──────────────── × 100
Total Books
```

For example:

```text id="b1b5bj"
2 borrowed
8 total

2 / 8 × 100 = 25%
```

This is a derived metric rather than a value stored in each book.

## Detailed Report

The detailed report combines the major library statistics.

It includes:

### Library Overview

* Total books
* Available books
* Borrowed books
* Borrowing rate

### Category Summary

* Number of books per category

### Current Circulation

* Currently borrowed books
* Current borrowers

### Recent Publications

* Top five most recently published books

Example:

```text id="ro0u7g"
========================================
        DETAILED LIBRARY REPORT
========================================

Total books     : 8
Available books : 6
Borrowed books  : 2
Borrowing rate  : 25.00%

Categories:
- Programming: 3
- Self-Help: 2
- Fiction: 1
- History: 1
- Productivity: 1

Currently borrowed:
- Clean Code → Anurag Bardhan
- Deep Work → Priya Singh

Recently published books:
1. Atomic Habits Workbook (2020)
2. Python Crash Course (2019)
3. The Pragmatic Programmer (2019)
4. Atomic Habits (2018)
5. Deep Work (2016)
```

## State Management

The central concept of this project is managing the state of a domain object.

A book moves between states:

```text id="j7c0xx"
AVAILABLE
    │
    │ borrow
    ▼
BORROWED
    │
    │ return
    ▼
AVAILABLE
```

The current state determines which actions are valid.

For example:

```text id="ov2t9v"
AVAILABLE → can borrow
BORROWED  → cannot borrow again
BORROWED  → can return
AVAILABLE → cannot return
```

This type of state transition appears in many real applications such as orders, reservations, accounts, tasks, tickets, and workflows.

## Derived Data

The project calculates values such as:

* Available book count
* Borrowed book count
* Borrowing rate
* Most common category
* Oldest and newest book

rather than storing these values permanently.

This means that after a book is borrowed or returned, the statistics automatically reflect the new state.

## Why This Project Matters

This project brings together nearly all of the data and logic patterns from Phase 02.

The program now works with:

```text id="z6i7vn"
Raw records
    ↓
CRUD
    ↓
Search
    ↓
Filtering
    ↓
Sorting
    ↓
State changes
    ↓
Aggregation
    ↓
Derived metrics
    ↓
Reports
```

The key transition is from processing isolated data to managing a small **domain system with rules and changing state**.

## Project Structure

```text id="wd0s6a"
17-mini-library-management-system/
│
├── main.py
└── README.md
```

The project intentionally remains a single-file application.

The repeated logic throughout this project is one of the reasons the next phase introduces **functions and modular program design**.

## How to Run

From the project directory:

```bash id="a2j0to"
python main.py
```

Make sure your Python virtual environment is activated before running the project.

## Example Workflow

```text id="m7ry2r"
View library
      ↓
Search or filter books
      ↓
Add a new book
      ↓
Borrow a book
      ↓
View current borrowers
      ↓
Return a book
      ↓
Check library statistics
      ↓
Generate detailed report
```

## Learning Progression

Project #17 completes the second major phase of the roadmap:

```text id="djd7p0"
Project #09
CRUD + search + filtering
        ↓
Project #10
Aggregation + ranking
        ↓
Project #11
Grouping + statistics
        ↓
Project #12
Document parsing + text analytics
        ↓
Project #13
Nested records + academic analytics
        ↓
Project #14
Relationships + capacity management
        ↓
Project #15
Graph structures + BFS traversal
        ↓
Project #16
Multi-criteria search + filtering
        ↓
Project #17
State management + complete domain system
```

## Phase 02 Milestone

With Project #17 completed, the Phase 02 objective is to be comfortable with:

```text
Lists
Dictionaries
Nested data
Loops
Conditionals
CRUD
Searching
Filtering
Sorting
Aggregation
Ranking
State management
Basic algorithms
Data validation
Derived metrics
```

The next phase will focus on **Functions & Program Design**, where these growing programs will be refactored into reusable and maintainable components.

## Future Improvements

Possible extensions include:

* Delete books
* Update book metadata
* Track borrowing dates
* Track return deadlines
* Detect overdue books
* Maintain borrowing history
* Track multiple copies of the same book
* Add member records
* Add reservation / waitlist support
* Persist data using CSV or JSON
* Move data into a database
* Add automated tests
* Refactor repeated logic into reusable functions
* Split the application into multiple modules

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

The goal is not simply to make the program work, but to understand the data structures, business rules, state transitions, and logic behind it.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
