# Project #24: Reporting Engine

A Python-based reporting system that transforms structured sales data into reusable summaries, category reports, monthly reports, product rankings, and exportable text reports.

This project is part of **Phase 03 — Functions & Program Design** and focuses on combining small reusable functions to build larger reporting workflows.

The main goal is to learn how to separate **calculation, data transformation, report generation, display, and file output**.

## Features

* View raw sales data
* Calculate total revenue
* Calculate total units sold
* Calculate average revenue
* Group sales by category
* Group sales by month
* Rank top products by revenue
* Generate summary reports
* Generate category performance reports
* Generate monthly reports
* Generate top-product reports
* Combine multiple sections into a full report
* Export the full report to a text file

## Concepts Practiced

### Functions

* Function definitions
* Function calls
* Parameters
* Arguments
* Return values
* Default parameters
* Helper functions
* Function composition
* Reusable calculations
* Separation of responsibilities

### Data Processing

* Lists
* Dictionaries
* Lists of dictionaries
* Dictionary `.items()`
* Dictionary aggregation
* `sum()`
* `len()`
* `sorted()`
* `enumerate()`
* List slicing
* Generator expressions
* Lambda functions

### Reporting

* Calculating metrics
* Grouping data
* Ranking data
* Building report sections
* Combining report sections
* Formatting numerical values
* Generating text reports

### File Handling

* `pathlib.Path`
* `Path.write_text()`
* UTF-8 text encoding
* File error handling

## Why This Project Exists

Previous projects taught how to calculate and process data.

Project #24 focuses on turning those calculations into **reusable reports**.

Instead of putting all of the logic into one large block:

```text
Data
 ↓
Everything happens together
 ↓
Output
```

the project separates the workflow:

```text
Raw Data
   ↓
Calculations
   ↓
Grouping / Ranking
   ↓
Report Generation
   ↓
Display / Export
```

This makes the individual pieces easier to reuse.

## Sales Data Structure

Each sales record is stored as a dictionary:

```python
{
    "id": 1,
    "product": "Mechanical Keyboard",
    "category": "Peripherals",
    "month": "January",
    "units": 12,
    "revenue": 54000.00
}
```

All records are stored inside a list:

```python
sales = [
    {...},
    {...},
    {...}
]
```

## Main Menu

```text
=== Menu ===
1. View sales data
2. Sales summary
3. Category performance
4. Monthly report
5. Top products
6. Full report
7. Export full report
8. Exit
```

## Sales Summary

The summary report calculates:

* Number of sales records
* Total units sold
* Total revenue
* Average revenue per sales record

The calculations are separated into reusable functions:

```python
calculate_total_revenue()
calculate_total_units()
calculate_average_revenue()
calculate_summary()
```

Example:

```text
=== Sales Summary ===

Sales records: 10
Units sold: 124
Total revenue: ₹548,800.00
Average revenue per record: ₹54,880.00
```

## Category Performance

Sales can be grouped by category.

For every category, the program calculates:

* Total units
* Total revenue

The data is first grouped:

```python
group_by_category(data)
```

and then ranked by revenue.

Example:

```text
=== Category Performance ===

Displays: 5 units | ₹140,000.00
Storage: 24 units | ₹153,200.00
Peripherals: 42 units | ₹125,000.00
Accessories: 38 units | ₹91,600.00
Audio: 15 units | ₹69,000.00
```

## Monthly Performance

Sales are also grouped by month.

The program calculates:

* Units sold
* Revenue

for each month.

The same aggregation pattern used for categories is reused with a different grouping key.

This demonstrates that reusable processing functions can support different views of the same dataset.

## Top Products

Products can be ranked according to revenue:

```python
sorted(
    data,
    key=lambda record: record["revenue"],
    reverse=True
)
```

The top five records are then selected using:

```python
[:5]
```

Example:

```text
=== Top Products ===

1. 4K Monitor — ₹140,000.00
2. 2TB HDD — ₹81,200.00
3. 1TB SSD — ₹72,000.00
4. USB-C Hub — ₹52,000.00
5. Mechanical Keyboard — ₹54,000.00
```

The ranking is based on revenue rather than number of units sold.

## Report Generation

Instead of printing the report directly, the project first builds it as a string.

For example:

```python
report = build_full_report(sales)
```

The returned value contains the complete report.

This means the exact same report can then be:

```text
Displayed in the terminal
        OR
Saved to a text file
```

without rebuilding the report.

## Building Report Sections

Individual functions generate individual sections:

```text
build_summary_report()
build_category_report()
build_monthly_report()
build_top_products_report()
```

The complete report then combines those sections:

```python
def build_full_report(data):
    ...
```

Conceptually:

```text
Full Report
    │
    ├── Summary
    ├── Category Performance
    ├── Monthly Performance
    └── Top Products
```

This is an example of **function composition**.

## Report as Data

One of the most important design choices in this project is that report functions return strings instead of printing directly.

For example:

```python
def build_summary_report(data):
    ...
    return "\n".join(lines)
```

The function creates report content and returns it.

Another part of the program can decide what to do with that content.

This separation allows the report to be reused for multiple outputs.

## Exporting Reports

The full report can be exported to:

```text
sales_report.txt
```

The project uses:

```python
REPORT_FILE = Path("sales_report.txt")
```

and:

```python
REPORT_FILE.write_text(
    report,
    encoding="utf-8"
)
```

The generated report therefore becomes a real file on the filesystem.

## Project Architecture

The reporting flow is:

```text
Sales Data
    ↓
Calculation Functions
    ↓
Aggregation / Ranking
    ↓
Report-Building Functions
    ↓
Complete Report String
    ├── Terminal
    └── Text File
```

Each layer has a different responsibility.

## Separation of Responsibilities

The project separates four major jobs.

### Calculation

Functions such as:

```python
calculate_total_revenue()
calculate_total_units()
calculate_average_revenue()
```

calculate values.

### Transformation

Functions such as:

```python
group_by_category()
group_by_month()
get_top_products()
```

transform or organize the data.

### Report Generation

Functions such as:

```python
build_summary_report()
build_category_report()
build_full_report()
```

turn processed data into formatted report text.

### Output

Functions such as:

```python
show_full_report()
save_report()
```

decide where the result should go.

This separation is one of the main lessons of the project.

## Function Composition

The full report demonstrates multiple functions working together.

For example:

```text
build_full_report()
       ↓
calculate_summary()
       ↓
calculate_total_revenue()
calculate_total_units()
calculate_average_revenue()

build_category_report()
       ↓
group_by_category()

build_monthly_report()
       ↓
group_by_month()

build_top_products_report()
       ↓
get_top_products()
```

A larger operation can therefore be assembled from smaller reusable operations.

## Project Structure

```text
24-reporting-engine/
│
├── main.py
└── README.md
```

After exporting a report, the program also creates:

```text
sales_report.txt
```

The generated report file is an output of the program rather than source code.

## How to Run

From the project directory:

```bash
python main.py
```

Use the menu to view the different reports.

Selecting:

```text
7. Export full report
```

creates or replaces:

```text
sales_report.txt
```

## Example Workflow

```text
View sales data
      ↓
Calculate overall summary
      ↓
Analyze categories
      ↓
Analyze months
      ↓
Rank products
      ↓
Generate complete report
      ↓
Export report
```

## Learning Progression

Project #24 builds directly on the function-design work from earlier Phase 03 projects:

```text
Project #18
Modular program structure
        ↓
Project #19
Reusable validation functions
        ↓
Project #20
Reusable processing utilities
        ↓
Project #21
Filesystem utilities
        ↓
Project #22
Function dispatch
        ↓
Project #23
Configuration + JSON persistence
        ↓
Project #24
Reusable reporting pipeline
```

The important progression is:

```text
Functions
   ↓
Reusable functions
   ↓
Functions working together
   ↓
Functions producing reusable data
   ↓
Functions producing reusable reports
```

## Why This Project Matters

Reporting appears in many real applications:

```text
Business dashboards
Financial systems
Analytics platforms
Inventory systems
Monitoring tools
Data pipelines
Backend services
Administrative systems
```

The underlying pattern is usually:

```text
Raw Data
   ↓
Process
   ↓
Calculate
   ↓
Aggregate
   ↓
Format
   ↓
Deliver
```

Project #24 gives a simple implementation of that pattern using only core Python.

## Future Improvements

Possible extensions include:

* Add date-based filtering
* Add custom report parameters
* Generate CSV reports
* Generate JSON reports
* Generate HTML reports
* Add report templates
* Add multiple datasets
* Add comparison reports
* Add charts later
* Separate calculations into modules
* Add automated tests
* Support configurable report formats

These improvements will become easier after the next project, which focuses on refactoring an earlier application using the design principles learned throughout Phase 03.

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

The goal is to understand how reusable functions can transform raw data into structured, reusable reports.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
