# Project #25: Rebuild Inventory & Billing System

A refactored version of the original Inventory & Billing System from Project #03.

This project is a deliberate **refactoring exercise** rather than a brand-new application. The original functionality is rebuilt using the function-based design principles learned throughout Phase 03.

The goal is to improve structure, readability, reuse, and separation of responsibilities without changing the core purpose of the application.

## Why This Project Exists

Project #03 was one of the first substantial programs in the repository.

At that stage, most of the program logic lived directly inside a large `while` loop:

```text
Main Menu
   ↓
Everything handled inside the loop
```

That worked, but as more functionality was added, the code became increasingly difficult to maintain.

After learning functions in Projects #18–#24, the same application can now be structured as:

```text
Main Program
    │
    ├── Product operations
    ├── Cart operations
    ├── Calculations
    └── Checkout
```

This project demonstrates the difference between **making code work** and **structuring working code well**.

## Features

* View inventory
* Search products by ID or name
* Add products to cart
* Validate requested quantities
* Prevent adding more than available stock
* View cart contents
* Calculate cart subtotal
* Calculate discounts
* Remove products from cart
* Complete checkout
* Update inventory after checkout
* Clear the cart after successful checkout

## Concepts Practiced

### Refactoring

* Function extraction
* Breaking large logic into smaller functions
* Removing duplicated logic
* Improving readability
* Separation of responsibilities
* Reusing existing functions

### Functions

* Function definitions
* Parameters
* Arguments
* Return values
* Helper functions
* Function composition
* Functions calling other functions

### Data Structures

* Dictionaries
* Nested dictionaries
* Dictionary `.get()`
* Dictionary `.items()`
* Dictionary `.clear()`
* Dictionary deletion with `del`
* List comprehensions

### Data Processing

* `sum()`
* `len()`
* `sorted()` patterns from earlier projects
* Calculated values
* Aggregation

### Validation

* Empty input validation
* Numeric validation
* Quantity validation
* Stock validation
* Product ID validation
* Checkout confirmation

## Original Project vs Refactored Project

### Project #03

The original application placed most behavior directly inside the menu loop.

Conceptually:

```text
while True:
    show menu

    if choice == "1":
        inventory logic

    elif choice == "2":
        search logic

    elif choice == "3":
        cart logic

    elif choice == "4":
        more cart logic

    ...
```

As functionality increased, the main loop became responsible for too many things.

### Project #25

The refactored application delegates those responsibilities:

```text
while True:
    show menu

    if choice == "1":
        display_inventory()

    elif choice == "2":
        search_products()

    elif choice == "3":
        add_to_cart()

    ...
```

The main loop now primarily handles **navigation**, while individual functions handle the actual work.

## Function Structure

The application is divided into several responsibilities.

### Product Functions

```text
find_product()
display_inventory()
search_products()
```

These functions deal with finding and displaying product information.

### Cart Functions

```text
add_to_cart()
remove_from_cart()
calculate_cart_total()
display_cart()
```

These functions manage the shopping cart.

### Calculation Functions

```text
calculate_cart_total()
calculate_discount()
```

These functions calculate values without owning the entire application flow.

### Checkout

```text
checkout()
```

coordinates the final purchase process.

It reuses existing functions instead of duplicating their logic.

## Finding Products

Instead of repeatedly searching the inventory:

```python
for product_id, product in inventory.items():
    ...
```

the project introduces:

```python
def find_product(product_id):
    return inventory.get(product_id)
```

Now other functions can simply do:

```python
product = find_product(product_id)
```

This is a simple example of extracting repeated logic into a reusable helper.

## Cart Representation

The cart uses a dictionary:

```python
cart = {}
```

The product ID is used as the key and the requested quantity as the value.

For example:

```python
{
    "P001": 2,
    "P003": 1
}
```

represents:

```text
2 × Keyboard
1 × Headphones
```

This makes it easy to look up the product and its requested quantity.

## Adding to Cart

The `add_to_cart()` function:

1. Reads a product ID
2. Finds the product
3. Validates that it exists
4. Checks stock
5. Reads the requested quantity
6. Checks the requested quantity against available stock
7. Updates the cart

The current quantity is retrieved using:

```python
cart.get(product_id, 0)
```

This returns the existing quantity or `0` when the product is not yet in the cart.

## Inventory Validation

The program prevents the user from requesting more items than are currently available.

For example:

```text
Stock: 10
Already in cart: 3
Requested: 8
```

The total requested quantity would be:

```text
3 + 8 = 11
```

Since only 10 are available, the operation is rejected.

This validation happens before modifying the cart.

## Calculating Cart Total

The function:

```python
calculate_cart_total()
```

loops through the cart and retrieves the corresponding product price from the inventory.

For each item:

```text
price × quantity
```

is calculated and added to the total.

For example:

```text
Keyboard
₹1,200 × 2 = ₹2,400

Headphones
₹1,800 × 1 = ₹1,800

Subtotal = ₹4,200
```

The function returns the total instead of directly printing it.

## Discount Calculation

The function:

```python
calculate_discount(total)
```

determines the discount based on the subtotal:

```text
₹10,000 or more → 10%
₹5,000 or more  → 5%
Below ₹5,000    → 0%
```

The function returns the discount amount.

This keeps discount logic separate from cart display and checkout.

## Display vs Calculation

A major refactoring principle in this project is separating calculation from presentation.

For example:

```text
calculate_cart_total()
        ↓
returns number
        ↓
display_cart()
        ↓
formats and prints number
```

The calculation function does not need to know anything about the terminal interface.

This makes it easier to reuse later.

## Checkout Workflow

The checkout process is handled by:

```python
checkout()
```

The function:

1. Checks that the cart is not empty
2. Displays the cart
3. Requests confirmation
4. Updates inventory
5. Calculates the final amount
6. Displays the receipt
7. Clears the cart

The overall workflow is:

```text
Cart
 ↓
Confirm
 ↓
Update inventory
 ↓
Calculate totals
 ↓
Apply discount
 ↓
Complete purchase
 ↓
Clear cart
```

## Updating Inventory

After checkout, the purchased quantity is removed from stock:

```python
inventory[product_id]["stock"] -= quantity
```

For example:

```text
Before checkout:
Stock = 10

Purchased:
Quantity = 3

After checkout:
Stock = 7
```

This demonstrates mutation of nested dictionary data.

## Clearing the Cart

After a successful checkout:

```python
cart.clear()
```

removes all items from the cart while keeping the same dictionary object.

Conceptually:

```text
Before:
{
    "P001": 2,
    "P003": 1
}

After:
{}
```

## Function Composition

The project demonstrates multiple functions working together.

For example:

```text
checkout()
   │
   ├── display_cart()
   │      │
   │      ├── calculate_cart_total()
   │      └── calculate_discount()
   │
   ├── update inventory
   │
   ├── calculate_cart_total()
   │
   └── calculate_discount()
```

A larger operation therefore becomes a combination of smaller operations.

## Separation of Responsibilities

The refactored structure follows this general principle:

```text
Function
   ↓
One clear responsibility
```

Examples:

```text
find_product()
    → Find a product

add_to_cart()
    → Add a product to the cart

calculate_cart_total()
    → Calculate subtotal

calculate_discount()
    → Calculate discount

display_cart()
    → Display cart

checkout()
    → Coordinate the purchase
```

This makes each part easier to understand independently.

## What Was Intentionally Not Changed

This project is a refactor, not a feature expansion.

The goal is to preserve the original application's basic behavior while improving its internal structure.

New systems such as:

* Databases
* File persistence
* Authentication
* Advanced product management

are intentionally left for later projects.

## Project Structure

```text
25-rebuild-inventory-billing/
│
├── main.py
└── README.md
```

The project remains a single file because the primary goal is **function decomposition**.

Later projects will introduce additional modularization and separate Python files.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure your Python virtual environment is activated before running the program.

## Example Workflow

```text
View inventory
      ↓
Search products
      ↓
Add products to cart
      ↓
Review cart
      ↓
Remove items if necessary
      ↓
Checkout
      ↓
Inventory stock updated
      ↓
Cart cleared
```

## Learning Progression

Project #25 is different from the previous projects because the primary goal is improvement of existing code.

```text
Project #03
Working single-file application
        ↓
Projects #18–#24
Functions + reusable utilities
        ↓
Project #25
Refactor the earlier application
        ↓
Cleaner structure + reusable logic
```

This is the first deliberate opportunity to apply the new design principles to code you have already written.

## What This Project Teaches

The central lesson is:

> Working code is not necessarily well-structured code.

A program can produce the correct output while still having:

* Repeated logic
* Large functions
* Poor separation of responsibilities
* Difficult-to-maintain code

Refactoring improves those properties without changing the application's fundamental purpose.

The project therefore introduces a critical software-development cycle:

```text
Build
  ↓
Understand
  ↓
Identify repetition
  ↓
Refactor
  ↓
Test behavior again
```

## Future Improvements

Possible future improvements include:

* Split functions into modules
* Create separate inventory and cart components
* Add reusable input-validation helpers
* Add a proper product management layer
* Add persistent inventory storage
* Add automated tests
* Introduce classes for products and carts
* Replace global state with cleaner dependency management

These improvements will be introduced progressively as the roadmap moves toward modular architecture, testing, OOP, and production-oriented Python development.

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

Project #25 adds another step:

```text
Refactor
```

The goal is not only to make programs work, but to learn how to continuously improve the structure of working code.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.
