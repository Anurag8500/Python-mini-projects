# Personal Finance Analyzer

A command-line Python application that records and analyzes personal expenses and generates a basic spending summary.

## Features

* Record multiple expenses
* Normalize expense categories for consistent data
* Calculate total spending
* Calculate average expense
* Find the highest expense
* Find the lowest expense
* Group spending by category
* Display formatted financial results

## Concepts Practiced

* Variables and data types
* User input with `input()`
* Type conversion with `int()` and `float()`
* Strings and string methods
* `.strip()` for removing surrounding whitespace
* `.lower()` for normalizing input
* `.title()` for formatted output
* Lists
* Dictionaries
* List of dictionaries
* `for` loops
* `if` conditions
* Dictionary membership with `in`
* Dictionary methods such as `.items()`
* Built-in functions: `sum()`, `max()`, and `min()`
* `lambda` functions with `key=`
* Basic data processing
* F-strings and number formatting with `:.2f`

## Example

```text
=== Personal Finance Analyzer ===

How many expenses do you want to enter? 5

Expense 1
Category: Food
Amount: ₹450

Expense 2
Category: transport
Amount: ₹200

Expense 3
Category: FOOD
Amount: ₹300

Expense 4
Category: Shopping
Amount: ₹1000

Expense 5
Category: transport
Amount: ₹150

=== Financial Summary ===
Total spending: ₹2100.00
Average expense: ₹420.00
Highest expense: Shopping - ₹1000.00
Lowest expense: Transport - ₹150.00

Spending by category:
- Food: ₹750.00
- Transport: ₹350.00
- Shopping: ₹1000.00
```

## What I Learned

* How to represent a single expense using a dictionary
* How to store multiple structured records in a list
* How to normalize user input before storing it
* How `.strip()` removes surrounding whitespace
* How `.lower()` helps treat inputs such as `Food`, `food`, and `FOOD` consistently
* How `.title()` can format normalized data for display
* How to iterate through a collection with a `for` loop
* How to calculate values from a collection
* How to group data by category using dictionaries
* How `max()` and `min()` can use a `key` function
* How f-strings can format numbers to two decimal places

## Possible Improvements

* Validate invalid or negative expense amounts
* Handle invalid user input with `try` / `except`
* Add monthly budgets
* Add budget warnings
* Show percentage spent by category
* Add expense dates
* Filter expenses by category
* Save expenses to a file
* Load previously saved expenses
* Refactor the program into reusable functions

## Project Status

**Completed — Phase 1: Python Core**
