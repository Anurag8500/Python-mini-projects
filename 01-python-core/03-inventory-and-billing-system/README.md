# Inventory & Billing System

A command-line Python application that manages a small product inventory, handles a shopping cart, processes purchases, and generates a final bill.

The project focuses on using Python data structures and control flow to model inventory, manage changing application state, and implement basic business rules.

## Features

* View available products and stock
* Search products by name
* Add products to a shopping cart
* Track quantities of products in the cart
* Prevent purchases beyond available stock
* View the current cart and total
* Remove products or quantities from the cart
* Apply discounts based on order value
* Generate a checkout bill
* Update inventory after checkout
* Handle invalid menu choices
* Handle empty cart situations

## Concepts Practiced

* Variables and data types
* Strings and string methods
* `.strip()`
* `.lower()`
* `.upper()`
* Lists
* Dictionaries
* Nested dictionaries
* Dictionary methods:

  * `.items()`
  * `.get()`
* Dictionary membership with `in` / `not in`
* Updating dictionary values
* `del`
* `while` loops
* `for` loops
* `if / elif / else`
* `break`
* `continue`
* Boolean flag variables
* Arithmetic operations
* Conditional business rules
* F-strings
* Number formatting with `:.2f`
* Managing program state
* Basic search and filtering
* Basic inventory and cart logic

## Data Structure

The inventory is represented as a dictionary where each product ID maps to another dictionary containing product information.

```python
inventory = {
    "P001": {
        "name": "Keyboard",
        "price": 1200.00,
        "stock": 10
    },
    "P002": {
        "name": "Mouse",
        "price": 700.00,
        "stock": 15
    }
}
```

The cart uses product IDs as keys and stores the quantity requested by the customer.

```python
cart = {
    "P001": 2,
    "P003": 1
}
```

This separates two different kinds of information:

* **Inventory:** what the store currently has
* **Cart:** what the customer currently wants

## Example

```text
=== Inventory & Billing System ===

=== Menu ===
1. View inventory
2. Search products
3. Add product to cart
4. View cart
5. Remove product from cart
6. Checkout
7. Exit

Choose an option: 3

Enter product ID: P003

Headphones | ₹1800.00 | Stock: 8

Enter quantity: 2

Added 2 x Headphones to the cart.
```

Viewing the cart:

```text
=== Cart ===
Headphones | 2 x ₹1800.00 = ₹3600.00

Cart total: ₹3600.00
```

Example checkout:

```text
=== Bill ===
Headphones | 2 x ₹1800.00 = ₹3600.00
Monitor | 1 x ₹12000.00 = ₹12000.00

Subtotal: ₹15600.00
Discount: 10%
Discount amount: ₹1560.00
Final total: ₹14040.00

Checkout successful.
Inventory updated.
```

## What I Learned

* How nested dictionaries can represent structured product data
* How dictionaries can be used to efficiently identify records with unique IDs
* How `.get()` can provide a default value when a dictionary key does not exist
* How to maintain changing application state
* How `while True` can be used to build an interactive menu
* The difference between `break` and `continue`
* How to search through dictionary data
* How to update and delete dictionary entries
* How to enforce simple business rules
* How to separate inventory data from cart data
* How user input can be normalized before processing
* How to calculate totals and discounts dynamically

## Example Business Rules

The application currently uses rules such as:

* A product must exist before it can be added to the cart
* Quantity must be greater than zero
* Cart quantity cannot exceed available inventory
* Orders of ₹5,000 or more receive a 5% discount
* Orders of ₹10,000 or more receive a 10% discount
* Inventory is reduced only after successful checkout

## Possible Improvements

* Add proper input validation with `try / except`
* Display `Out of stock` when inventory reaches zero
* Display low-stock warnings
* Allow sorting products by name, price, or stock
* Add product categories
* Add tax calculation
* Add customer information
* Generate a unique order ID
* Add timestamps to orders
* Save inventory and orders to files
* Load existing inventory when the program starts
* Refactor the program into reusable functions
* Rebuild the system using object-oriented programming
* Add automated tests
* Replace in-memory data with a database

## Project Structure

```text
03-inventory-and-billing-system/
│
├── main.py
└── README.md
```

## Status

**Completed — Phase 01: Python Core**

Project 03 of the Python Mini Projects curriculum.
