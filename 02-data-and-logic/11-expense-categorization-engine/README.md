# Project #11: Expense Categorization Engine

A Python-based terminal application for recording, categorizing, searching, and analyzing personal expenses.

This project builds on the data-processing patterns learned in earlier projects and introduces more structured **grouping, aggregation, filtering, sorting, and statistical analysis**.

The program works entirely in memory and uses Python's built-in data structures and operations.

## Features

* View all recorded expenses
* Add new expenses
* Assign expenses to categories
* Update an expense category
* View spending summaries by category
* View spending summaries by month
* Find the highest expenses
* Search expenses by description or category
* Filter expenses by category
* Calculate overall expense statistics
* Generate a detailed expense report
* Track total spending and average expense values

## Concepts Practiced

This project reinforces and combines several Python concepts learned throughout previous projects.

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Nested dictionaries

### Control Flow

* `while` loops
* `for` loops
* `if / elif / else`
* `break`
* `continue`

### Data Processing

* `sum()`
* `len()`
* `max()`
* `min()`
* `sorted()`
* List comprehensions
* Generator expressions
* Dictionary `.get()`
* Dictionary `.items()`
* `enumerate()`
* List slicing

### Functions Used in Data Analysis

The project frequently uses `lambda` functions with `sorted()`, `max()`, and `min()` to determine how expenses should be ranked.

### Input Handling

* `input()`
* `.strip()`
* `.lower()`
* `.title()`
* `try / except`
* Input validation

### Output Formatting

Currency and numerical values are displayed using formatted strings such as:

```python
f"₹{amount:,.2f}"
```

This produces output such as:

```text
₹12,450.00
```

## Data Structure

Each expense is stored as a dictionary:

```python
{
    "id": 1,
    "description": "Grocery Shopping",
    "amount": 2400.00,
    "category": "food",
    "month": "January"
}
```

All expenses are stored inside a list:

```python
expenses = [
    {...},
    {...},
    {...}
]
```

This structure makes it possible to process every expense consistently while still allowing each record to contain multiple pieces of information.

## Expense Categories

The application supports the following categories:

```text
Food
Transport
Entertainment
Shopping
Utilities
Health
Education
Other
```

These categories can be used to group expenses and calculate category-level statistics.

## Main Menu

The program provides the following options:

```text
=== Menu ===
1. View all expenses
2. Add expense
3. Update expense category
4. Category summary
5. Highest expenses
6. Monthly analysis
7. Search expenses
8. Filter by category
9. Expense statistics
10. Detailed expense report
11. Exit
```

## Category Analysis

The category summary groups expenses and calculates:

* Number of expenses
* Total amount spent
* Average expense

For example:

```text
=== Category Summary ===

Food
  Expenses: 3
  Total: ₹6,700.00
  Average: ₹2,233.33

Transport
  Expenses: 2
  Total: ₹1,300.00
  Average: ₹650.00
```

The categories are ranked by total spending, allowing the user to quickly identify where most money is being spent.

## Monthly Analysis

The same aggregation idea is applied to months.

The program calculates:

* Number of expenses
* Total monthly spending
* Average expense for the month

Example:

```text
=== Monthly Analysis ===

March
  Expenses: 2
  Total: ₹4,000.00
  Average: ₹2,000.00

February
  Expenses: 4
  Total: ₹5,849.00
  Average: ₹1,462.25
```

This demonstrates that the same data-processing technique can be applied using a different grouping key.

## Expense Ranking

Expenses can be sorted from highest to lowest amount:

```python
ranked_expenses = sorted(
    expenses,
    key=lambda expense: expense["amount"],
    reverse=True
)
```

The program then displays the top five expenses.

Example:

```text
=== Highest Expenses ===

1. New Headphones | ₹3,200.00 | Shopping | February
2. Monthly Groceries | ₹3,100.00 | Food | March
3. Grocery Shopping | ₹2,400.00 | Food | January
```

## Search

Expenses can be searched using their:

* Description
* Category

The search is case-insensitive, so searches such as:

```text
food
Food
FOOD
```

produce the same results.

The program uses string normalization with:

```python
.strip().lower()
```

before performing the search.

## Filtering

The filter option allows the user to select a specific category and display only expenses belonging to that category.

For example:

```text
=== Food Expenses ===

[1] Grocery Shopping | ₹2,400.00 | January
[5] Restaurant Dinner | ₹1,200.00 | February
[10] Monthly Groceries | ₹3,100.00 | March

Category total: ₹6,700.00
```

This demonstrates the use of list comprehensions to create a filtered dataset.

## Expense Statistics

The statistics section calculates overall spending information:

```text
=== Expense Statistics ===

Number of expenses: 10
Total spending: ₹15,148.00
Average expense: ₹1,514.80
Highest expense: New Headphones (₹3,200.00)
Lowest expense: Uber Ride (₹450.00)
```

These values are calculated directly from the expense dataset.

## Grouping with Dictionaries

One of the most important patterns introduced in this project is building summary dictionaries dynamically.

For example:

```python
category_data = {}
```

starts with an empty dictionary.

When an expense is processed, its category becomes a key:

```text
food
transport
shopping
utilities
```

Each category then stores its own statistics:

```python
{
    "food": {
        "expense_count": 3,
        "total_amount": 6700
    }
}
```

This allows many individual records to be transformed into a useful summary.

## Dictionary `.get()` Pattern

The project also reinforces the counting pattern:

```python
category_counts[category] = (
    category_counts.get(category, 0) + 1
)
```

`.get(category, 0)` means:

* use the existing count if the category already exists
* otherwise start from `0`

Then `1` is added to the count.

This is a common pattern for counting values while processing data.

## Project Structure

```text
11-expense-categorization-engine/
│
├── main.py
└── README.md
```

At this stage, the project intentionally remains a single-file application. Functions and larger modular structures will be introduced in later stages of the roadmap.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure your Python virtual environment is activated before running the project.

## Example Workflow

A typical session might look like:

```text
1. View existing expenses
2. Add a new expense
3. Update its category if necessary
4. Search or filter expenses
5. Check category spending
6. Check monthly spending
7. View highest expenses
8. Generate the detailed report
```

## What This Project Teaches

The main purpose of this project is to move from simply storing data to **understanding and summarizing data**.

Instead of only asking:

> "What expenses exist?"

the program can answer questions such as:

* Where is most money being spent?
* Which category has the most expenses?
* Which month had the highest spending?
* What are the largest individual expenses?
* What is the average expense?
* How many expenses belong to each category?

These are fundamental data-processing patterns that appear in larger applications, analytics systems, backend services, and database-driven software.

## Learning Progression

Project #11 intentionally reuses concepts from previous projects:

```text
Project #01
Expense data + totals
        ↓
Project #06
Frequency counting + text processing
        ↓
Project #07
Dynamic dictionary counting
        ↓
Project #09
Search + filtering
        ↓
Project #10
Aggregation + ranking
        ↓
Project #11
Expense categorization + multi-level analysis
```

The goal is not to learn every concept in isolation, but to repeatedly apply older concepts in increasingly realistic problems.

## Future Improvements

Possible future extensions include:

* Delete expenses
* Edit all expense fields
* Add yearly analysis
* Add budget limits
* Compare budget vs actual spending
* Import expenses from CSV
* Import expenses from JSON
* Export reports to files
* Persist data using a database
* Add recurring expenses
* Track spending trends
* Add visual charts

These improvements are intentionally left for future projects as the roadmap progresses toward file processing, databases, testing, APIs, and backend development.

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

The goal is to understand the code rather than simply produce working output.

> Never commit code you cannot explain.

AI may be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer building it.
