# Project #18: Modular Expense Tracker

A Python-based terminal expense management application redesigned around **functions and modular program structure**.

This project marks the beginning of **Phase 03 — Functions & Program Design**. Instead of placing all application logic directly inside the main menu, the program separates responsibilities into reusable functions.

The application supports expense management, searching, filtering, summaries, budget analysis, and detailed reporting.

## Features

* View all expenses
* Add new expenses
* Update existing expenses
* Delete expenses
* Search expenses by description or category
* Filter expenses by category
* Generate overall expense summaries
* Generate monthly spending summaries
* Generate category spending summaries
* Compare spending against a user-defined budget
* Calculate spending percentage
* Identify highest and lowest expenses
* Generate detailed expense reports
* Reuse common logic through functions
* Separate calculation logic from display logic

## Concepts Practiced

### Functions

* Defining functions with `def`
* Calling functions
* Parameters
* Arguments
* Return values
* Local variables
* Global variables
* Function responsibilities
* Reusing functions
* Separating calculation from presentation

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Nested dictionaries
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
* `max()`
* `min()`
* `sorted()`
* `enumerate()`
* List comprehensions
* Generator expressions
* List slicing
* Aggregation
* Ranking

### Input Validation

* Empty input validation
* Numeric validation
* Range validation
* Category validation
* Month validation
* Expense ID validation

## Why This Project Exists

Earlier projects were intentionally implemented as large single-file programs.

As functionality grew, the same kinds of logic began appearing repeatedly:

```text
Find a record
Validate input
Calculate totals
Group data
Sort results
Generate reports
```

Putting all of this directly inside the menu makes the program harder to read, modify, and reuse.

Project #18 introduces functions to solve that problem.

## Program Structure

The application is divided into logical responsibilities:

```text
Main Program
     │
     ├── Expense Management
     │     ├── add_expense()
     │     ├── update_expense()
     │     └── delete_expense()
     │
     ├── Search / Filtering
     │     ├── search_expenses()
     │     └── filter_expenses_by_category()
     │
     ├── Calculations
     │     ├── calculate_expense_summary()
     │     ├── calculate_monthly_summary()
     │     └── calculate_category_summary()
     │
     └── Reports
           ├── show_expense_summary()
           ├── show_monthly_summary()
           ├── show_category_summary()
           ├── show_budget_analysis()
           └── show_detailed_report()
```

This structure makes the application easier to understand and provides a foundation for more modular projects later in the roadmap.

## Main Menu

```text
=== Menu ===
1. View expenses
2. Add expense
3. Update expense
4. Delete expense
5. Search expenses
6. Filter by category
7. Expense summary
8. Monthly summary
9. Category summary
10. Budget analysis
11. Detailed report
12. Exit
```

## Finding an Expense with a Function

Instead of repeating the same search logic in multiple places, the program defines:

```python
def find_expense(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense

    return None
```

The function either returns the matching expense or returns `None` when it cannot find one.

This can then be reused:

```python
expense = find_expense(expense_id)
```

Both updating and deleting expenses use this shared functionality.

## Return Values

One of the most important concepts introduced in this project is returning data from functions.

For example:

```python
def calculate_expense_summary():
    ...
    return {
        "count": count,
        "total": total,
        "average": average
    }
```

The function calculates the result but does not print it.

Another function can then use the returned value:

```python
summary = calculate_expense_summary()
```

This creates a separation between:

```text
Calculation
    ↓
Return data
    ↓
Display result
```

This pattern becomes especially important in larger applications where the same calculated data may be needed by multiple parts of the program.

## Expense Management

### Add Expense

The application allows users to create new expense records.

Each expense contains:

```python
{
    "id": 11,
    "description": "Coffee",
    "amount": 250.00,
    "category": "food",
    "month": "March"
}
```

### Update Expense

Existing expenses can be modified by ID.

Users can change:

* Description
* Amount
* Category
* Month

Pressing Enter keeps the existing value.

### Delete Expense

Expenses can be removed by ID.

The program first finds the record using:

```python
find_expense()
```

and then removes the matching dictionary from the list.

## Search

Expenses can be searched by:

* Description
* Category

The search is case-insensitive and supports partial matches.

For example:

```text
Search by description or category: food
```

can return every expense belonging to the Food category.

## Filtering

Expenses can be filtered by category.

Example:

```text
=== Food Expenses ===

[1] Grocery Shopping | ₹2,400.00 | January
[5] Restaurant Dinner | ₹1,200.00 | February
[10] Monthly Groceries | ₹3,100.00 | March

Category total: ₹6,700.00
```

The filtering logic is isolated inside:

```python
filter_expenses_by_category()
```

rather than being embedded directly into the main menu.

## Expense Summary

The overall expense summary calculates:

* Number of expenses
* Total spending
* Average expense
* Highest expense
* Lowest expense

The calculation is handled by:

```python
calculate_expense_summary()
```

while the presentation is handled by:

```python
show_expense_summary()
```

This is an intentional separation of responsibilities.

## Monthly Summary

Expenses can be grouped by month.

For each month the program calculates:

* Number of expenses
* Total spending
* Average expense

The calculation function returns a dictionary containing the aggregated data.

The results are then sorted by total spending.

Example:

```text
=== Monthly Summary ===

March
  Expenses: 2
  Total: ₹4,000.00
  Average: ₹2,000.00

February
  Expenses: 4
  Total: ₹5,849.00
  Average: ₹1,462.25
```

## Category Summary

Expenses are also grouped by category.

For every category the program calculates:

* Number of expenses
* Total spending
* Average expense

Categories are ranked from highest to lowest spending.

This reuses the aggregation patterns learned in earlier projects while placing the calculation inside a dedicated function.

## Budget Analysis

The user can enter a budget and compare it with total spending.

The program calculates:

```text
Spending percentage =
Total Spending / Budget × 100
```

It also calculates the remaining amount.

Example:

```text
Budget: ₹20,000.00
Total spending: ₹15,148.00
Spending percentage: 75.74%
Remaining budget: ₹4,852.00
```

If spending exceeds the budget, the application reports the amount exceeded instead.

## Spending Level

The project includes a small helper function:

```python
calculate_grade_from_spending()
```

which classifies total spending into:

```text
Low
Medium
High
```

based on predefined thresholds.

The purpose of this helper is to reinforce how a function can receive data and return a meaningful result.

## Detailed Report

The detailed report combines:

### Overall Statistics

* Total expenses
* Total spending
* Average expense
* Highest expense
* Lowest expense

### Category Breakdown

* Spending by category

### Monthly Breakdown

* Spending by month

### Top Expenses

* Top three expenses ranked by amount

Example:

```text
========================================
       DETAILED EXPENSE REPORT
========================================

Total expenses   : 10
Total spending   : ₹15,148.00
Average expense  : ₹1,514.80
Highest expense  : New Headphones (₹3,200.00)
Lowest expense   : Uber Ride (₹450.00)

Category breakdown:
- Food: ₹6,700.00
- Shopping: ₹3,200.00
- Utilities: ₹2,399.00
- Entertainment: ₹1,549.00
- Transport: ₹1,300.00

Top 3 expenses:
1. New Headphones — ₹3,200.00
2. Monthly Groceries — ₹3,100.00
3. Grocery Shopping — ₹2,400.00
```

## Function Design

The project introduces the idea that a function should have a clear responsibility.

For example:

```text
find_expense()
    → Find a specific expense

add_expense()
    → Create a new expense

delete_expense()
    → Remove an expense

calculate_expense_summary()
    → Calculate summary data

show_expense_summary()
    → Display summary data
```

This is more maintainable than placing unrelated logic inside one large menu block.

## Global vs Local Data

The expense list exists outside the functions:

```python
expenses = [...]
```

Functions such as:

```python
view_expenses()
search_expenses()
calculate_category_summary()
```

can read the existing list.

The `add_expense()` function modifies the `next_expense_id` variable using:

```python
global next_expense_id
```

This is intentionally included as part of the learning process.

Later projects will explore cleaner ways to manage shared state and reduce reliance on global variables.

## Project Structure

```text
18-modular-expense-tracker/
│
├── main.py
└── README.md
```

The project remains in a single file for now, but its internal logic is divided into functions.

Later projects will further separate functionality into modules and reusable packages.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure the Python virtual environment is activated before running the program.

## Example Workflow

```text
View existing expenses
        ↓
Add / update / delete records
        ↓
Search or filter expenses
        ↓
Generate summaries
        ↓
Analyze spending against a budget
        ↓
Generate detailed report
```

## Learning Progression

Project #18 marks the transition from writing larger programs directly inside the main loop to designing programs using reusable functions.

```text
Phase 02
Data structures + logic
        ↓
Project #17
Large single-file domain system
        ↓
Project #18
Functions + separation of responsibilities
        ↓
Future projects
Reusable components + modular architecture
```

The goal is not simply to learn the `def` keyword, but to understand **when a piece of logic deserves to become a function and what that function should be responsible for**.

## Future Improvements

Possible extensions include:

* Move functions into separate modules
* Create reusable validation functions
* Create reusable display functions
* Remove global state
* Add persistent storage
* Import and export CSV/JSON data
* Add recurring expenses
* Add multiple budgets
* Add date-based analysis
* Add automated tests
* Package the expense tracker as a reusable application

These improvements will be introduced progressively throughout Phase 03 and the later phases of the roadmap.

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

The objective is to understand the structure and reasoning behind the program rather than simply producing working code.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
