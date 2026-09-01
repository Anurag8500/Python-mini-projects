# Project #10: Inventory Analytics Engine

A Python-based inventory analysis program that processes product data and generates useful business insights through a terminal interface.

The project focuses on working with **lists of dictionaries**, **derived metrics**, **sorting**, **filtering**, **aggregation**, **searching**, and **data analysis** using core Python.

## Features

* View all products
* Generate an inventory overview
* Identify low-stock products
* Rank products by total inventory value
* Analyze inventory by category
* Analyze product prices
* Analyze stock levels
* Search products by name or category
* Generate a detailed inventory report
* Display totals, averages, rankings, and category statistics

## Concepts Practiced

* Lists of dictionaries
* Nested dictionaries
* Variables and constants
* `while` loops
* `for` loops
* Conditional statements
* List comprehensions
* Dictionary `.get()`
* Dictionary `.items()`
* `sum()`
* `max()` and `min()`
* `sorted()`
* `lambda`
* `enumerate()`
* List slicing
* Generator expressions
* String normalization with `.strip()` and `.lower()`
* Formatted output
* Derived metrics and aggregation

## Data Structure

Each product is stored as a dictionary:

```python
{
    "id": "P001",
    "name": "Mechanical Keyboard",
    "category": "peripherals",
    "price": 4500.00,
    "stock": 12
}
```

All products are stored inside a list:

```python
products = [
    {...},
    {...},
    {...}
]
```

This structure makes it possible to loop through products and calculate different statistics from the same dataset.

## Important Calculations

### Total Inventory Value

The value of each product's inventory is calculated as:

```text
price × stock
```

The total inventory value is then calculated by adding the values of all products.

### Low-Stock Detection

Products with stock less than or equal to the configured threshold are considered low-stock items.

```python
LOW_STOCK_LIMIT = 5
```

### Category Analysis

The program groups products by category and calculates:

* Number of products
* Total units
* Total inventory value

### Product Ranking

Products can be sorted using different metrics such as:

* Price
* Stock quantity
* Total inventory value

For inventory value, the program uses:

```python
product["price"] * product["stock"]
```

## Example

```text
=== Inventory Analytics Engine ===

=== Menu ===
1. View all products
2. Inventory overview
3. Low-stock products
4. Most valuable inventory
5. Category analysis
6. Price analysis
7. Stock analysis
8. Search products
9. Detailed inventory report
10. Exit
```

Example inventory overview:

```text
=== Inventory Overview ===

Total products: 10
Total units: 123
Total inventory value: ₹566,800.00
Average product price: ₹6,500.00
Average stock per product: 12.30

Most expensive product: 4K Monitor (₹28,000.00)
Cheapest product: Wireless Mouse (₹1,800.00)
Highest inventory value: 4K Monitor (₹140,000.00)
```

## Project Structure

```text
10-inventory-analytics-engine/
│
├── main.py
└── README.md
```

## How to Run

From the project directory:

```bash
python main.py
```

## What This Project Teaches

This project moves beyond simply storing and displaying data.

The main goal is to learn how to take a collection of structured data and **extract meaningful information from it**.

The same patterns used here—filtering, sorting, aggregation, grouping, and calculating derived values—appear frequently in real-world applications and form an important foundation for later projects involving files, databases, APIs, and backend systems.

## Future Improvements

Possible extensions include:

* Add products dynamically
* Update product stock
* Remove products
* Import inventory from CSV or JSON
* Export reports to files
* Add price-range filtering
* Add category filtering
* Track stock changes over time
* Build charts and visual reports

These improvements are intentionally left for later stages of the learning roadmap.
