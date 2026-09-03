# Project #16: Search & Filtering Engine

A Python-based terminal application that searches, filters, sorts, and analyzes a structured product dataset using multiple search criteria.

This project focuses on turning simple filtering into a more flexible **query-style system** where users can combine keywords, categories, brands, price ranges, ratings, and stock conditions.

It builds on the searching, filtering, sorting, and aggregation concepts developed in the previous projects.

## Features

* View all products
* Search products by keyword
* Search across product name, category, and brand
* Filter products by category
* Filter products by price range
* Filter products by stock range
* Apply multiple filters simultaneously
* Use optional filters by skipping criteria
* Sort products by price
* Sort products by rating
* Sort products by stock
* Sort products by name
* Sort results in ascending or descending order
* Combine keyword search with additional filters
* Calculate search and product statistics
* Generate a detailed search report

## Concepts Practiced

### Data Structures

* Lists
* Dictionaries
* Lists of dictionaries
* Dictionary `.get()`
* Dictionary `.items()`

### Control Flow

* `while` loops
* `for` loops
* Nested loops
* `if / elif / else`
* `break`
* `continue`

### Search and Filtering

* Exact matching
* Partial matching
* Case-insensitive searching
* Multiple filtering conditions
* Optional filtering
* Range filtering
* Boolean logic
* Filtering pipelines

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

### Input Validation

* Empty input validation
* Numeric validation
* Range validation
* Rating validation
* Minimum/maximum range validation

### Sorting

* Sorting by numeric fields
* Sorting by text fields
* Ascending order
* Descending order
* Custom sorting keys with `lambda`

## Product Data Structure

Each product is represented by a dictionary:

```python
{
    "id": "P001",
    "name": "Mechanical Keyboard",
    "category": "peripherals",
    "brand": "Logitech",
    "price": 4500.00,
    "rating": 4.5,
    "stock": 12
}
```

The complete dataset is stored in a list:

```python
products = [
    {...},
    {...},
    {...}
]
```

Each product therefore contains several searchable and filterable properties.

## Searchable Fields

Keyword searches can match against:

* Product name
* Category
* Brand

For example, searching for:

```text
logitech
```

can return products whose brand is Logitech.

Searching for:

```text
gaming
```

can return products whose name contains the word "gaming".

The search is case-insensitive.

## Main Menu

```text
=== Menu ===
1. View all products
2. Search by keyword
3. Filter by category
4. Filter by price range
5. Filter by stock range
6. Advanced filter
7. Sort products
8. Search + filters
9. Search statistics
10. Detailed report
11. Exit
```

## Keyword Search

The keyword search checks multiple product fields.

Conceptually:

```text
Search term
    ↓
Product name?
    OR
Category?
    OR
Brand?
```

A product is included when the search term appears in at least one of those fields.

For example:

```text
Search: samsung
```

can match:

```text
Samsung 4K Monitor
Samsung 1TB SSD
```

## Category Filtering

Category filtering returns products belonging to an exact category.

For example:

```text
Category: audio
```

returns products such as:

```text
Gaming Headset
USB Microphone
Bluetooth Speaker
```

The comparison is performed after converting the user's input to lowercase.

## Price Range Filtering

The user can provide a minimum and maximum price.

For example:

```text
Minimum price: ₹2000
Maximum price: ₹6000
```

The program applies:

```text
2000 ≤ price ≤ 6000
```

Products outside the specified range are excluded.

The program also validates that the maximum price is not smaller than the minimum price.

## Stock Range Filtering

The same range-filtering idea is applied to stock quantities.

For example:

```text
Minimum stock: 5
Maximum stock: 15
```

matches products where:

```text
5 ≤ stock ≤ 15
```

This reinforces the idea that the same filtering pattern can be reused for different numerical fields.

## Advanced Filtering

The advanced filter allows multiple criteria to be entered at once.

Available criteria include:

* Category
* Brand
* Minimum price
* Maximum price
* Minimum rating
* Minimum stock

Any criterion can be skipped by pressing Enter.

For example:

```text
Category: peripherals
Brand: Logitech
Minimum price: ₹2000
Maximum price: ₹5000
Minimum rating: 4
Minimum stock: 5
```

The program keeps only products that satisfy **all active filters**.

## Optional Filters

A major concept introduced in this project is optional criteria.

For example:

```python
minimum_price = None
```

means that the user did not provide a minimum price.

The program checks:

```python
if minimum_price is not None:
```

before applying that filter.

This allows one search operation to support many different combinations without requiring a separate menu option for every possible combination.

## Filtering with `continue`

The advanced filtering logic checks each product one condition at a time.

Conceptually:

```text
Product
   ↓
Pass category?
   ↓ yes
Pass brand?
   ↓ yes
Pass price?
   ↓ yes
Pass rating?
   ↓ yes
Pass stock?
   ↓ yes
Keep product
```

If a product fails one condition:

```python
continue
```

immediately skips that product and moves to the next one.

This creates a simple filtering pipeline.

## Sorting

The program supports sorting by:

* Price
* Rating
* Stock
* Name

The user can also select:

* Ascending order
* Descending order

For example:

```python
sorted_products = sorted(
    products,
    key=lambda product: product["rating"],
    reverse=True
)
```

sorts products from highest rating to lowest rating.

For text sorting, the program uses normalized names so that capitalization does not affect the ordering.

## Search + Filters

The combined search option allows a keyword and additional filters to be applied together.

For example:

```text
Keyword: gaming
Category: peripherals
Brand: Razer
Minimum price: ₹2000
Maximum price: ₹5000
Minimum rating: 4.5
```

The program progressively eliminates products that do not satisfy the selected conditions.

This is the closest part of the project to a basic query engine.

## Search Statistics

The statistics section provides an overview of the dataset.

It calculates:

* Total number of products
* Average product price
* Average rating
* Average stock
* Highest-rated product
* Lowest-priced product
* Highest-priced product
* Number of in-stock products
* Number of out-of-stock products
* Number of products in each category

Example:

```text
=== Search Statistics ===

Total products: 12
Average price: ₹5,725.00
Average rating: 4.52
Average stock: 12.33
Highest rated: 1TB SSD (4.9)
Lowest price: Wireless Mouse (₹1,800.00)
Highest price: 4K Monitor (₹28,000.00)
In-stock products: 12
Out-of-stock products: 0
```

## Detailed Report

The detailed report combines the main dataset statistics into a single summary.

It includes:

### Overall Statistics

* Total products
* Average price
* Average rating
* Average stock

### Product Extremes

* Highest-rated product
* Most expensive product
* Cheapest product
* Most-stocked product

### Category Distribution

The report counts the number of products belonging to each category.

### Top-Rated Products

The top five products are ranked by rating.

Example:

```text
========================================
       DETAILED SEARCH REPORT
========================================

Total products : 12
Average price  : ₹5,725.00
Average rating : 4.52
Average stock  : 12.33

Highest rated  : 1TB SSD (4.9)
Most expensive: 4K Monitor (₹28,000.00)
Cheapest       : Wireless Mouse (₹1,800.00)
Most stocked   : Wireless Mouse (25 units)

Products by category:
- Accessories: 2
- Audio: 3
- Displays: 1
- Peripherals: 4
- Storage: 2

Top 5 rated products:
1. 1TB SSD — 4.9
2. 4K Monitor — 4.8
3. USB Microphone — 4.7
4. Bluetooth Speaker — 4.7
5. Gaming Headset — 4.6
```

## Filtering Pipeline

One of the main ideas in this project is thinking about filtering as a pipeline:

```text
All Products
     ↓
Keyword Search
     ↓
Category Filter
     ↓
Brand Filter
     ↓
Price Filter
     ↓
Rating Filter
     ↓
Stock Filter
     ↓
Final Results
```

Every active condition reduces the result set.

For example:

```text
12 products
     ↓ keyword
5 products
     ↓ category
3 products
     ↓ rating
2 products
```

This way of thinking becomes especially useful later when working with databases, APIs, query parameters, and backend systems.

## Why This Project Matters

Earlier projects used simple searches such as:

```python
product["category"] == category
```

Project #16 takes that idea further.

A user can now combine multiple conditions:

```text
Search
+ Category
+ Brand
+ Price
+ Rating
+ Stock
```

This introduces the thinking behind real search and filtering systems without yet requiring a database or external search library.

## Project Structure

```text
16-search-filtering-engine/
│
├── main.py
└── README.md
```

The project intentionally remains a single-file program at this stage.

The repeated filtering logic will provide strong motivation for the next phase, where functions and modular design are introduced.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure your Python virtual environment is activated before running the program.

## Example Workflow

```text
View the dataset
      ↓
Search by keyword
      ↓
Apply category / price / stock filters
      ↓
Try advanced multi-condition filtering
      ↓
Sort the results
      ↓
Combine search with filters
      ↓
Analyze search statistics
      ↓
Generate the detailed report
```

## Learning Progression

Project #16 brings together several patterns from earlier projects:

```text
Project #09
Search + filtering
        ↓
Project #10
Product analysis + sorting
        ↓
Project #11
Grouping + statistics
        ↓
Project #13
Record filtering + ranking
        ↓
Project #15
Structured data traversal
        ↓
Project #16
Multi-criteria search + filtering pipelines
```

The project is intentionally designed as a bridge between simple Python collections and the query-style thinking used in larger applications.

## Future Improvements

Possible extensions include:

* Add more filter types
* Filter by rating range
* Filter by available stock
* Combine multiple sort fields
* Allow saved searches
* Display result counts after each filter
* Add pagination
* Import product data from CSV or JSON
* Persist product data using a database
* Convert filters into reusable functions
* Build a database-backed query engine
* Expose the search system through an API

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

The goal is not simply to make the program work, but to understand the data structures, control flow, search logic, and filtering decisions behind it.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
